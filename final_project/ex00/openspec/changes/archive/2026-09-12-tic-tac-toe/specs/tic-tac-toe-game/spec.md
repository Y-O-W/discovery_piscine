## ADDED Requirements

### Requirement: Player setup
The system SHALL prompt for a Player 1 name and a Player 2 name once at program start, and SHALL use those names for the remainder of the session (across all rounds).

#### Scenario: Names collected at startup
- **WHEN** the program starts
- **THEN** it prompts "Player 1, what is your name?:" then "Player 2, what is your name?:" and stores both names before any round begins

### Requirement: Board state per round
The system SHALL track the occupancy of the 9 board spaces (numbered 1-9) for the current round, starting empty, and SHALL reset to a fully empty board at the start of every new round.

#### Scenario: Fresh board each round
- **WHEN** a new round begins (session start, or after a previous round ends)
- **THEN** all 9 spaces are unoccupied

### Requirement: Turn-based move input
The system SHALL alternate turns between Player 1 and Player 2, prompting the current player with "Choose a space (1-9) or type 'STOP':" on their turn.

#### Scenario: Turns alternate
- **WHEN** Player 1 completes a valid move
- **THEN** the next prompt is addressed to Player 2, and vice versa

### Requirement: Move validation
The system SHALL reject a move and re-prompt without ending the round or crashing when the input is not a number 1-9, or refers to a space that is already occupied.

#### Scenario: Out-of-range or non-numeric input
- **WHEN** a player enters something other than an integer 1-9 or the word STOP
- **THEN** the system shows an error and re-prompts the same player without changing the board or advancing the turn

#### Scenario: Occupied space
- **WHEN** a player enters the number of a space that already holds a mark
- **THEN** the system shows an error and re-prompts the same player without changing the board or advancing the turn

### Requirement: Win detection
After each valid move, the system SHALL check all 8 winning lines (3 rows, 3 columns, 2 diagonals) and SHALL end the round as a win for the moving player if their mark occupies all 3 spaces of any winning line.

#### Scenario: Three in a row
- **WHEN** a player's move completes a full row, column, or diagonal of their own mark
- **THEN** the round ends immediately as a win for that player, without prompting further moves

### Requirement: Draw detection
The system SHALL end the round as a draw if all 9 spaces become occupied without any winning line being completed.

#### Scenario: Full board, no winner
- **WHEN** the 9th space is filled and no winning line is present
- **THEN** the round ends as a draw

### Requirement: Mid-round STOP
The system SHALL end the current round immediately, with no winner, when a player enters STOP instead of a move, and SHALL NOT count that round toward the rounds-played total.

#### Scenario: STOP during a move
- **WHEN** a player enters STOP at the move prompt
- **THEN** the round ends with no winner, a "round stopped" message is shown, and the rounds-played counter is not incremented

### Requirement: Round-boundary prompt
After every round ends (win, draw, or mid-round STOP), the system SHALL show the current tally and prompt whether to play another round or to end the session by entering STOP.

#### Scenario: Continue after a round
- **WHEN** a round has just ended
- **THEN** the system displays the updated score/rounds-played and prompts "Play again, or type STOP to end:"

#### Scenario: STOP at the round boundary
- **WHEN** a player enters STOP at the round-boundary prompt
- **THEN** the session ends: a final tally is shown and the program exits

### Requirement: Cross-round win tally
The system SHALL maintain a running count of rounds won by each player, incremented only when a round ends in a win, and persisting for the life of the session.

#### Scenario: Tally increments on win
- **WHEN** a round ends in a win for a player
- **THEN** that player's win count increases by 1 and is reflected in the next round-boundary display

### Requirement: Rounds-played counter
The system SHALL maintain a count of rounds that reached a conclusion (win or draw), incremented for wins and draws but NOT for rounds ended early via STOP.

#### Scenario: Draw counts, early STOP does not
- **WHEN** one round ends in a draw and a separate round ends via mid-round STOP
- **THEN** the rounds-played counter increases by 1 for the draw and is unaffected by the STOP-ended round
