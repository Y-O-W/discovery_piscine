## 1. Scaffolding

- [x] 1.1 Add shebang (`#!/usr/bin/env python3`) to `tic_tac_toe.py` and make it executable (`chmod +x`)
- [x] 1.2 Define constants: `WINNING_LINES` (8 key-triples over 1-9), player color codes, outcome color codes

## 2. Core board & move logic

- [x] 2.1 Implement board creation as a dict keyed 1-9, all values empty at round start
- [x] 2.2 Implement move validation: reject non-numeric/out-of-range input and already-occupied spaces, re-prompting the same player without state changes
- [x] 2.3 Implement turn alternation between Player 1 and Player 2
- [x] 2.4 Implement win-check over `WINNING_LINES` that returns the matching line (not just a boolean) when a win is found
- [x] 2.5 Implement draw-check (all 9 spaces filled, no winning line)

## 3. Session & round control flow

- [x] 3.1 Implement startup name prompts (Player 1, Player 2) run once per session
- [x] 3.2 Implement the round loop: fresh board, alternating move prompts, exits on win/draw/mid-round STOP
- [x] 3.3 Implement mid-round STOP handling: end round with no winner, show "round stopped" message, do not increment rounds-played
- [x] 3.4 Implement per-player win tally, incremented only on a round ending in a win
- [x] 3.5 Implement rounds-played counter, incremented only on win or draw (not on STOP)
- [x] 3.6 Implement the round-boundary prompt ("Play again, or type STOP to end:") that loops back into a new round or ends the session
- [x] 3.7 Implement session exit: print final tally and terminate on STOP at the round-boundary prompt

## 4. Terminal UI — structure

- [x] 4.1 Implement a small ANSI helper (e.g. `colorize(text, code)`) used by all styled output
- [x] 4.2 Implement the startup title banner, printed once before name prompts
- [x] 4.3 Implement box-drawn board rendering (numbers when empty, marks when filled), redrawn after every valid move
- [x] 4.4 Implement the score line (per-player win counts in their colors + rounds-played in neutral color)
- [x] 4.5 Implement the turn prompt styled in the current player's assigned color

## 5. Terminal UI — outcome visuals

- [x] 5.1 Implement win rendering: highlight the three winning cells and the win message in the winning player's color, bolded
- [x] 5.2 Implement draw rendering: neutral-colored board and message, not tied to either player's color
- [x] 5.3 Implement stopped-round rendering: dimmed board (frozen as-is) and distinct "round stopped, no winner" message

## 6. Verification

- [x] 6.1 Manually play through: a full win, a full draw, a mid-round STOP, and a full session-ending STOP, confirming tally/rounds-played update exactly as specified
- [x] 6.2 Confirm invalid inputs (letters, out-of-range numbers, occupied spaces) never crash the program and always re-prompt the same player
- [x] 6.3 Confirm the mid-move prompt text always reads exactly `Choose a space (1-9) or type 'STOP':` regardless of round state
- [x] 6.4 Confirm the file is executable and runs directly via `./tic_tac_toe.py`
