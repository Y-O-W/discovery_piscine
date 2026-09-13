#!/usr/bin/env python3
# A text-based tic-tac-toe game.

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

PLAYER_1_COLOR = "\033[36m"
PLAYER_2_COLOR = "\033[35m"
DRAW_COLOR = "\033[37m"
STOP_COLOR = "\033[90m"
PLAYER_1_MARK = "X"
PLAYER_2_MARK = "O"

WINNING_LINES = (
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (1, 4, 7), (2, 5, 8), (3, 6, 9),
    (1, 5, 9), (3, 5, 7),
)

TITLE = "THE REAL TIC-TAC-TOE"
BANNER_WIDTH = 24


def colorize(text, code):
    return f"{code}{text}{RESET}"


def print_banner():
    top = "╔" + "═" * BANNER_WIDTH + "╗"
    middle = "║" + TITLE.center(BANNER_WIDTH) + "║"
    bottom = "╚" + "═" * BANNER_WIDTH + "╝"
    print(colorize(top, BOLD))
    print(colorize(middle, BOLD))
    print(colorize(bottom, BOLD))


def render_board(board, highlight=(), highlight_color="", dim=False):
    rows = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    lines = ["┌───┬───┬───┐"]
    for i, row in enumerate(rows):
        cells = []
        for n in row:
            mark = board[n] if board[n] != "" else str(n)
            if n in highlight:
                mark = colorize(mark, BOLD + highlight_color)
            cells.append(mark)
        lines.append(f"│ {' │ '.join(cells)} │")
        if i < len(rows) - 1:
            lines.append("├───┼───┼───┤")
    lines.append("└───┴───┴───┘")

    for line in lines:
        print(colorize(line, DIM) if dim else line)


def score_line(players, rounds_played):
    p1 = colorize(f"{players[1]['name']}: {players[1]['wins']}", players[1]["color"])
    p2 = colorize(f"{players[2]['name']}: {players[2]['wins']}", players[2]["color"])
    rounds = colorize(f"Rounds played: {rounds_played}", DRAW_COLOR)
    print(f"{p1}   {p2}   {rounds}")


def create_board():
    return {space: "" for space in range(1, 10)}


def other_player(player):
    return 3 - player


def get_move(board, players, current_player):
    player = players[current_player]
    print(colorize(f"{player['name']}'s turn!", player["color"]))
    while True:
        raw = input("Choose a space (1-9) or type 'STOP': ").strip()
        if raw.upper() == "STOP":
            return "STOP"
        elif raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw)] == "":
            return int(raw)
        else:
            print("This move is not allowed.")


def check_win(board):
    for line in WINNING_LINES:
        a, b, c = line
        if board[a] == board[b] == board[c] != "":
            return line
    return None


def is_draw(board):
    return all(mark != "" for mark in board.values())


def create_players():
    name1 = input("Player 1, what is your name?: ").strip()
    name2 = input("Player 2, what is your name?: ").strip()
    return {
        1: {"name": name1, "wins": 0, "color": PLAYER_1_COLOR, "mark": PLAYER_1_MARK},
        2: {"name": name2, "wins": 0, "color": PLAYER_2_COLOR, "mark": PLAYER_2_MARK}
    }


def play_round(players, current_player):
    board = create_board()
    render_board(board)
    while True:
        move = get_move(board, players, current_player)
        if move == "STOP":
            return "STOP", None, None, board

        board[move] = players[current_player]["mark"]
        render_board(board)
        line = check_win(board)
        if line:
            return "WIN", current_player, line, board
        if is_draw(board):
            return "DRAW", None, None, board

        current_player = other_player(current_player)


def play_session():
    print_banner()
    players = create_players()
    rounds_played = 0
    starting_player = 1

    while True:
        outcome, winner, line, board = play_round(players, starting_player)

        if outcome == "WIN":
            players[winner]["wins"] += 1
            rounds_played += 1
            render_board(board, highlight=line, highlight_color=players[winner]["color"])
            print(colorize(f"{players[winner]['name']} wins!", BOLD + players[winner]["color"]))
        elif outcome == "DRAW":
            rounds_played += 1
            print(colorize("It's a draw!", DRAW_COLOR))
        else:
            render_board(board, dim=True)
            print(colorize("Round stopped — no winner.", STOP_COLOR))

        score_line(players, rounds_played)

        answer = input("Play again, or type STOP to end:")
        if answer.upper() == "STOP":
            break


if __name__ == "__main__":
    play_session()

