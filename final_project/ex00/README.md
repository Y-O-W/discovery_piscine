# Terminal Tic-Tac-Toe — Project Defense

Two-player tic-tac-toe for the terminal (stdlib only). Written for the Discovery
Piscine final project. Specs: [`openspec/specs/tic-tac-toe-game`](openspec/specs/tic-tac-toe-game/spec.md),
[`openspec/specs/tic-tac-toe-terminal-ui`](openspec/specs/tic-tac-toe-terminal-ui/spec.md).

## What it does

- Prompts for two player names once, at startup — names persist for the whole session.
- Runs a **session loop** (persisted names, win tally, rounds-played counter) wrapping a
  **round loop** (fresh empty board every round).
- Players alternate turns entering a space 1-9; invalid input (out of range, non-numeric,
  already occupied) is rejected and re-prompted without ending the round.
- After every move: check for a win (3-in-a-row on any of the 8 lines), then a draw
  (board full, no winner).
- `STOP` is a single keyword scoped by *where* it's typed: mid-round it abandons just that
  round (no winner, not counted in rounds-played); at the round-boundary prompt it ends
  the whole session.
- Terminal UI: ASCII banner, box-drawn board, persistent per-player color for name/prompt/
  mark, and visually distinct treatment for win (highlighted line, bold), draw (neutral),
  and stopped (dimmed) outcomes.

## Key design decisions (and why)

**Board is a dict keyed 1-9, not a list/2D array.**
The space numbers a player types are used directly as dict keys (`board[5]`, etc.), so
there's no index-translation layer between what the player sees and what the code stores.
The trade-off: it only reads naturally because the board is small and fixed-size (9 cells)
— this wouldn't scale to an NxN board without other changes.

**`other_player(player)` is `3 - player`, not a lookup table or `if/else`.**
With exactly two players numbered 1 and 2, `3 - 1 = 2` and `3 - 2 = 1` — one line of
arithmetic replaces a branch. This only works *because* there are exactly two players;
it's a small trick worth being able to explain rather than defend as "obviously correct."

**`is_draw()` is only ever called after `check_win()` returns `None`.**
Order matters: a full board that also completes a winning line is a win, not a draw. The
`play_round` loop checks the win condition first and only falls through to the draw check
if there's no winner — a full board isn't sufficient on its own to justify a draw.

**`STOP` deliberately overloads one keyword rather than using two.**
Its meaning is entirely contextual — which prompt it's entered at, not the word itself,
decides "abandon this round" vs. "end the session." This keeps the player-facing surface
area small (one word to remember) at the cost of the two behaviors living in different
functions (`get_move` vs. `play_session`) that a reader has to connect mentally.

**Per-player color is assigned once and threaded everywhere**, rather than derived from
whose turn it is. `players[n]["color"]` is looked up by player number in every place a
mark, name, or prompt is styled, so the color identity is a property of the *player*, not
of the *moment* — satisfying the spec's "persistent per-player color identity" requirement
directly rather than incidentally.

## Spec traceability

- Player setup, board state, move validation, win/draw detection, mid-round `STOP`,
  round-boundary flow, and both tallies (wins vs. rounds-played) map 1:1 to the
  requirements in `tic-tac-toe-game/spec.md`.
- Banner, box-drawn board, color identity, score line, turn-prompt styling, and the three
  distinct outcome visuals map 1:1 to `tic-tac-toe-terminal-ui/spec.md`.
- Full history: GitHub epic [#1](https://github.com/Y-O-W/discovery_piscine/issues/1) and
  its linked issues (#2–#8), each scoped to one slice of the spec and wired with native
  GitHub blocked-by/blocking dependencies.

## Out of scope (by design)

- Web version of the game.
- External color/UI libraries (`colorama`, `rich`) — styling is hand-rolled ANSI codes.
- Accessibility fallback for color (e.g. colorblind-safe marks) — not required by spec.
