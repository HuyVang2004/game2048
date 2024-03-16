import random


def init():
    broad = [[0 for _ in range(4)] for _ in range(4)]
    broad = random_value(broad, True)
    return broad


def random_value(broad, moved):
    if not moved:
        return None
    i = random.choice((0, 1, 2, 3))
    j = random.choice((0, 1, 2, 3))

    while broad[i][j] != 0:
        i = random.choice((0, 1, 2, 3))
        j = random.choice((0, 1, 2, 3))

    broad[i][j] = random.choice((2, 2, 2, 2, 2, 2, 2, 2, 2, 4))

    return broad


def left_move(board, score):
    "Array lưu trữ các ô đã có sự di chuyển"
    merged = [[False for _ in range(4)] for _ in range(4)]
    "Đánh dấu hướng đi này có thể di chuyển để sử dụng cho hàm random_value"
    moved = False
    for i in range(4):
        for j in range(1, 4):
            s = 0
            for q in range(j):
                if board[i][q] == 0:
                    s += 1
            "Tìm số ô trống -> đẩy ô hiện tại về vị trí trống cuối cùng nếu có"
            if s > 0 and board[i][j] != 0:
                board[i][j - s] = board[i][j]
                board[i][j] = 0
                moved = True
            "Nếu 2 ô gần nhau bằng nhau và cả 2 ô đểu chưa có sự di chuyển -> gộp lại"
            if board[i][j - s] == board[i][j - s - 1] and not merged[i][j - s] and not merged[i][j - s - 1]:
                board[i][j - s - 1] *= 2
                score += board[i][j - s - 1]
                board[i][j - s] = 0
                merged[i][j - s - 1] = True
                moved = True
    return board, moved, score


def right_move(board, score):
    merged = [[False for _ in range(4)] for _ in range(4)]
    moved = False
    for i in range(4):
        for j in range(2, -1, -1):
            s = 0
            for q in range(3, j, -1):
                if board[i][q] == 0:
                    s += 1

            if s > 0 and board[i][j] != 0:
                board[i][j + s] = board[i][j]
                board[i][j] = 0
                moved = True

            if j + s + 1 <= 3:
                if board[i][j + s] == board[i][j + s + 1] and not merged[i][j + s] and not merged[i][j + s + 1]:
                    board[i][j + s + 1] *= 2
                    score += board[i][j + s + 1]
                    board[i][j + s] = 0
                    merged[i][j + s + 1] = True
                    moved = True

    return board, moved, score


def down_move(board, score):
    merged = [[False for _ in range(4)] for _ in range(4)]
    moved = False
    for i in range(2, -1, -1):
        for j in range(4):
            s = 0
            for q in range(3, i, -1):
                if board[q][j] == 0:
                    s += 1

            if s > 0 and board[i][j] != 0:
                board[i + s][j] = board[i][j]
                board[i][j] = 0
                moved = True

            if i + s + 1 <= 3:
                if board[i + s][j] == board[i + s + 1][j] and not merged[i + s][j] and not merged[i + s + 1][j]:
                    board[i + s + 1][j] *= 2
                    score += board[i + s + 1][j]
                    board[i + s][j] = 0
                    merged[i + s + 1][j] = True
                    moved = True

    return board, moved, score


def up_move(board, score):
    merged = [[False for _ in range(4)] for _ in range(4)]
    moved = False
    for i in range(1, 4):
        for j in range(4):
            s = 0
            for q in range(i):
                if board[q][j] == 0:
                    s += 1

            if s > 0 and board[i][j] != 0:
                board[i - s][j] = board[i][j]
                board[i][j] = 0
                moved = True

            if board[i - s][j] == board[i - s - 1][j] and not merged[i - s][j] and not merged[i - s - 1][j]:
                board[i - s - 1][j] *= 2
                score += board[i - s - 1][j]
                board[i - s][j] = 0
                merged[i - s - 1][j] = True
                moved = True

    return board, moved, score


def move(board, score, dir):
    if dir == "left":
        return left_move(board, score)
    elif dir == "right":
        return right_move(board, score)
    elif dir == "up":
        return up_move(board, score)
    elif dir == "down":
        return down_move(board, score)


def end(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False

    return True
