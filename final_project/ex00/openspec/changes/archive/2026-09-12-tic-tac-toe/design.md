## Context

This is the sole deliverable of the Discovery Piscine final weekend project: a single-file, terminal tic-tac-toe game (`tic_tac_toe.py`). The spec (see `ex00/42-berlin_piscine-python_final-project.pdf`) gives a minimum interface example but full creative freedom on visuals, and states the project will be presented live — the author must be able to defend data structure and logic choices, not just produce working output.

Two sentences in the spec create a real tension that shaped several decisions here:
- "The main game must run continuously without exiting. It should only stop and exit when a player wins, the board is full (a draw), or if a user inputs STOP."
- "Keep a running tally of how many times Player 1 and Player 2 have won across multiple rounds."

Read literally, the first sentence implies the *program* exits on a single win — which makes "tally across multiple rounds" meaningless. This design resolves that by treating "the main game" in the first sentence as scoped to one *round*, with an outer session loop supplying the "multiple rounds" the tally requires.

## Goals / Non-Goals

**Goals:**
- Satisfy every literal requirement in the spec (name prompts, dict/list board state, continuous play, valid-move enforcement, win/draw/STOP handling, cross-round tally) with a design that is internally consistent (no contradictory requirements) and easy to explain live.
- Terminal presentation that clears the spec's minimum bar (box-drawn board, clean prompts) and goes further with a styled, colored interface as requested.
- Keep the whole thing dependency-free (Python standard library only).

**Non-Goals (this change):**
- Web version of the game.
- Any external color/UI library (colorama, rich, etc.).
- Accessibility fallbacks for color (e.g. colorblind-safe palette, no-color mode) — noted as a future-iteration idea, not required now.
- AI opponent / single-player mode — spec requires two named human players only.

## Decisions

**Board representation: dict keyed 1-9, not a flat list or 3x3 grid.**
The board is always addressed by the number a player types (1-9) — both on input and on screen. A dict (`{1: "", ..., 9: ""}`) makes `board[n]` identical to "space n" everywhere, with no off-by-one translation to introduce or explain. A flat 0-indexed list would need `board[space - 1]` at every touch point; a 3x3 list-of-lists would need a 1-9 → (row, col) conversion for every input and every render, which buys nothing here since the game is never played or displayed in row/col terms. Chosen specifically because it's the easiest of the three to defend live.

**Win-check returns the matching line, not just a boolean.**
`WINNING_LINES` is the 8 key-triples (3 rows, 3 columns, 2 diagonals) over the same 1-9 keyspace. Checking `board[a] == board[b] == board[c] != ""` for each triple yields both "is there a winner" and "which three cells to highlight" in one pass — needed for the win visual (see below), and a direct payoff of the dict keying decision.

**Two nested loops: SESSION (outer) and ROUND (inner).**
Session asks for both player names once and persists them, the per-player win tally, and a rounds-played counter for the life of the program. Round owns one board and one sequence of alternating turns. This is what reconciles the spec tension described in Context: every round-ending event (win, draw, or an early STOP) returns control to the session loop, which is the only place the program can actually terminate.

**`STOP` is one keyword with two scopes, not two different keywords.**
Typed during a move, `STOP` ends only the current round (no winner; prints "Round stopped — no winner, moving to next round"; does **not** increment rounds-played, since the round never reached a conclusion) and always falls through to the round-boundary prompt. Typed at that round-boundary prompt ("Play again, or type STOP to end:"), it ends the session — final tally is printed and the program exits.
Alternatives considered: (a) two distinct words (e.g. `EXIT` mid-round, `STOP` at the boundary) — rejected because it would make the mid-move prompt read `...or type 'EXIT':`, diverging from the spec's own screenshot which shows `...or type 'STOP':` at that exact prompt; (b) `STOP` mid-move ending the entire program immediately — rejected because it collapses back into the literal-reading contradiction described in Context (tally across multiple rounds would never be reachable). The chosen design keeps the visible prompt text matching the spec's example at every point in the program, with the word's effective scope determined by where the player is instead of which word they type.

**Rounds-played counts only completed rounds (win or draw).**
An early-STOP round is explicitly excluded from this counter, since it never reached a result — counting it would make "rounds played" mean two different things depending on how a round ended.

**Terminal styling: raw ANSI escape codes, standard 16-color palette, no external library.**
This is a "build it from what you learned this week" exercise (variables/conditions/loops/lists/dicts) — a hand-rolled `colorize(text, code)`-style helper fits that spirit, has zero installation risk during a live presentation, and the standard 16 colors render correctly on any terminal likely to be used for the demo.
Alternative considered: `colorama` or `rich` for richer effects — rejected for this change due to the added dependency and no functional requirement it satisfies that raw ANSI codes can't.

**Visual principle: color encodes player identity; weight/emphasis encodes event.**
Each player is assigned one persistent color (e.g. Player 1/X = cyan, Player 2/O = magenta) used consistently for their name, turn prompt, and board mark throughout the session. Round outcomes reuse identity color rather than introducing an unrelated palette:
- **Win**: the winner's own color, bolded, applied only to the three winning cells (from the win-check's returned line) plus a highlighted win message.
- **Draw**: a neutral color (not either player's), full board shown in default styling — deliberately not "owned" by either player.
- **Stopped early**: dimmed/gray, board frozen exactly as it stood.
This keeps the palette coherent (two meanings — who / what happened — rather than an arbitrary color per state) and was chosen directly in response to the requirement that all three outcomes be visually distinguishable from each other.

**Player identity as one nested dict (`PLAYERS[n]`), not parallel constants.**
Settled during implementation (issues #2/#5), after starting from a standalone `PLAYER_COLORS` constant. `PLAYERS` is keyed by player number, same as `PLAYER_COLORS`/`WINNING_LINES`, but each value is itself a dict holding everything about that player: `{"name": ..., "wins": 0, "color": ..., "mark": ...}`. This groups "everything about one entity" under a single lookup (`PLAYERS[current]["color"]` reads next to `PLAYERS[current]["name"]`) instead of separate parallel dicts keyed the same way.
Trade-off accepted knowingly: `color` and `mark` are fixed for the life of the session (assigned once, at player creation) while `wins` mutates every round — so this dict mixes a constant-ish field with genuinely-changing state. Not wrong in Python (no type distinction enforced), but worth being able to explain live if asked why some fields never change while others do. The alternative — separate `PLAYER_COLORS`/`PLAYER_MARKS` module constants plus a `PLAYERS` dict for just name/wins — was rejected because it splits per-player facts across three lookups instead of one, for no functional gain.

**`play_round()` returns a consistent 4-tuple regardless of outcome.**
`(outcome, winner, line, board)` is always the shape, with unused slots as `None` (e.g. `("STOP", None, None, board)`, `("DRAW", None, None, board)`). This lets `play_session()` always unpack the same four names after every call, rather than branching on how many values come back depending on what happened. It also keeps `play_round()` focused purely on round mechanics — it never touches the tally or prints anything outcome-specific; that's entirely `play_session()`'s job, matching the SESSION/ROUND loop separation described above.

## Risks / Trade-offs

- **STOP's context-dependent scope could read as non-compliant to a literal-minded grader** (the spec sentence "stop and exit... if a user inputs STOP" could be read as "exits the whole program immediately") → Mitigation: this is precisely the tension flagged in Context; the presentation should lead with *why* the two-scope reading was chosen (it's the only reading under which the cross-round tally requirement is satisfiable at all).
- **Raw ANSI codes assume a VT100-compatible terminal** → Mitigation: acceptable for this project (presented live from the author's own terminal); no Windows `cmd.exe` support required or claimed.
- **Color-only differentiation between outcomes is not colorblind-safe** → Accepted as a known limitation for this iteration; text messages ("★ ALICE WINS ★" / "IT'S A DRAW" / "ROUND STOPPED") remain the primary, color-independent signal, so the game stays fully legible without color.

## Open Questions

- Assumed terminal width for the box-drawn board — standard 80 columns is more than sufficient for a 3x3 board and not expected to be a constraint.

**Resolved during implementation:** exact color codes (Player 1/X = cyan `\033[36m`, Player 2/O = magenta `\033[35m`, draw = white `\033[37m`, stop = gray `\033[90m`) and banner wording — both settled as ordinary implementation choices, no design-level tension involved. See the `PLAYERS` nested-dict decision above for where the colors actually live at runtime.
