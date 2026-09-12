## ADDED Requirements

### Requirement: Startup banner
The system SHALL display an ASCII-art title banner once, before the player-name prompts, on program start.

#### Scenario: Banner shown before name prompts
- **WHEN** the program starts
- **THEN** the title banner is printed before the "Player 1, what is your name?:" prompt

### Requirement: Box-drawn board rendering
The system SHALL render the board using box-drawing characters, showing each space's number when empty and the occupying player's mark when filled, and SHALL re-render the full board after every valid move.

#### Scenario: Board reflects latest move
- **WHEN** a player completes a valid move
- **THEN** the redrawn board shows that player's mark in the chosen space and all other spaces unchanged

### Requirement: Persistent per-player color identity
The system SHALL assign each player one color at the start of the session and SHALL use that same color consistently for their name, their turn prompt, and their mark on the board for the rest of the session.

#### Scenario: Same color throughout
- **WHEN** Player 1 is assigned a color at session start
- **THEN** every later display of Player 1's name, turn prompt, and board mark uses that same color

### Requirement: Score line display
The system SHALL display, at the round boundary, each player's win count in their own color and a rounds-played count in a neutral color.

#### Scenario: Score line after a round
- **WHEN** the round-boundary prompt is shown
- **THEN** it includes both players' current win counts (each in their assigned color) and the current rounds-played count

### Requirement: Styled turn prompt
The system SHALL display the current player's turn prompt (e.g. "Alice's turn!") in that player's assigned color.

#### Scenario: Turn prompt matches active player's color
- **WHEN** it becomes Player 2's turn
- **THEN** the turn prompt is shown in Player 2's assigned color, distinct from Player 1's color

### Requirement: Distinct outcome visuals
The system SHALL visually distinguish a win, a draw, and a mid-round STOP from one another, using color/emphasis in addition to differing text.

#### Scenario: Win highlights the winning line
- **WHEN** a round ends in a win
- **THEN** the three winning cells are shown highlighted in the winning player's color, and a win message is shown in that color with added emphasis

#### Scenario: Draw uses a neutral treatment
- **WHEN** a round ends in a draw
- **THEN** the full board is shown in default/neutral styling (not either player's color) with a draw message in a neutral color

#### Scenario: Stopped round uses a dimmed treatment
- **WHEN** a round ends via mid-round STOP
- **THEN** the board is shown frozen as it stood, in a dimmed/muted style, with a distinct "round stopped, no winner" message
