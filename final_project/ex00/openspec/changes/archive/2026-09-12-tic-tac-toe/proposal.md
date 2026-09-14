## Why

The Discovery Piscine final weekend project requires a single deliverable: a fully playable, visually engaging, terminal-based tic-tac-toe game at `final_project/ex00/tic_tac_toe.py` that demonstrates variables, conditions, loops, lists/dicts, and is presented live (data structure and logic choices must be defendable). Nothing exists yet beyond an empty placeholder file.

## What Changes

- Add `tic_tac_toe.py`: an executable Python script implementing a two-player tic-tac-toe game with a styled ANSI terminal interface.
- Board state stored as a dict keyed 1-9 (matches the numbers players type and see, no index translation).
- Two-level game loop: a session (persists player names, win tallies, and a rounds-played counter) containing repeated rounds (a fresh board each time).
- A single `STOP` keyword used contextually: mid-round it abandons just that round (no winner, does not count toward rounds-played); at the round-boundary prompt it ends the session for good.
- Move validation that rejects out-of-range, non-numeric, and already-occupied inputs without crashing the loop.
- ANSI-colored terminal presentation (stdlib only, no external color library): a startup title banner, box-drawn board, per-player persistent colors used consistently for names/turn-prompts/marks, and visually distinct win/draw/stopped-round outcomes (win highlights the winning line in the winner's color; draw and stop use neutral/dim tones).

## Capabilities

### New Capabilities
- `tic-tac-toe-game`: Two-player terminal tic-tac-toe — board state, turn/move handling, win/draw detection, the session/round loop structure, and the STOP-driven exit flow.
- `tic-tac-toe-terminal-ui`: The ANSI-styled terminal presentation layer — title banner, box-drawn board rendering, score line, turn prompts, and the distinct win/draw/stopped visual treatments.

### Modified Capabilities
(none — greenfield project, no existing specs)

## Impact

- New file: `final_project/ex00/tic_tac_toe.py` (must be made executable per spec).
- No dependencies added (Python standard library only).
- Out of scope for this change: a web version of the game and any external styling library (e.g. colorama/rich) — noted as future iterations, not part of this proposal.
