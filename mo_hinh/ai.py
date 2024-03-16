import copy
from mo_hinh import model

# Tính giá trị của các trạng thái
def evaluate(board):
    "Có 8 hướng di chuyển để dồn các ô lớn nhất về các góc"
    paths = [
        [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (2, 3),
         (1, 3), (0, 3)],
        [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (3, 2),
         (3, 1), (3, 0)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (3, 1), (3, 0), (2, 0),
         (1, 0), (0, 0)],
        [(0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (2, 2), (2, 1), (2, 0), (3, 0), (3, 1),
         (3, 2), (3, 3)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1), (1, 2), (1, 3), (0, 3), (0, 2),
         (0, 1), (0, 0)],
        [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (1, 3),
         (2, 3), (3, 3)],
        [(3, 3), (3, 2), (3, 1), (3, 0), (2, 0), (2, 1), (2, 2), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0), (0, 0), (0, 1),
         (0, 2), (0, 3)],
        [(3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (1, 2), (2, 2), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0),
         (2, 0), (3, 0)]]
    max_score = -1
    " Đánh giá xem hướng di chuyển nào là tốt nhất"
    for path in paths:
        eval = 0
        c = 1

        for tile in path:
            eval += board[tile[0]][tile[1]] * c
            c *= 2
        if eval > max_score:
            max_score = eval

    return max_score


# Tìm nước đi tốt nhất cho bước đi tiếp theo
def expectiminimax(board, depth, is_max):
    # depth là độ sâu của cây tím kiếm, nếu depth == 0 (đã duyệt hết) thì trả về giá trị của trạng thái, hướng di chuyển là None
    if depth == 0:
        return evaluate(board), None
    # Nếu là node Max thì thưc hiện di chuyển trạng thái hiện tại theo 4 hướng và trả về hướng tốt nhất
    if is_max:
        max_score = -1
        dir = None
        for action in ["left", "right", "up", "down"]:
            new_board, has_move, _ = model.move(copy.deepcopy(board), 0, action)
            if has_move:
                eval = expectiminimax(new_board, depth - 1, False)[0]
                if eval > max_score:
                    max_score = eval
                    dir = action
        return max_score, dir
    # nếu là node chance (node đại diện cho việc random)
    else:
        # Lấy ra vị trí các ô trống
        empty_tile = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
        # Cần phải tính giá trị trung bình của tất cả các trường hợp random có thể xảy ra
        total = 0
        for tile in empty_tile:
            new_board = copy.deepcopy(board)
            new_board[tile[0]][tile[1]] = 2
            # số 2 xuất hiện với xác xuất p = 0.9
            eval_2 = expectiminimax(new_board, depth - 1, True)[0] * 0.9

            new_board[tile[0]][tile[1]] = 4
            # số 4 xuất hiện với xác xuất p = 0.1
            eval_4 = expectiminimax(new_board, depth - 1, True)[0] * 0.1
            total += eval_2 + eval_4
        p = 1 / len(empty_tile) if len(empty_tile) != 0 else 1
        return total * p, None
