class Player :

  def __init__(self, name, color) :
    self.__name = name
    self.__player_color = color
    self.__enemy_color = 'Black' if self.__player_color == 'White' else 'White'
    self.__piece_count = 30
    self.__play_squares = []
    self.__flip_squares = []

  def print_piece_count(self) :
    return self.__piece_count

  def print_player_color(self) :
    return self.__player_color

  def grid_point(self, row, index) :
    return (row + 1) * 8 - (8 - (index + 1))

  def choices(self) :
    return self.__play_squares

  def flips(self) :
    return self.__flip_squares

  def remove_player_piece(self) :
    self.__piece_count -= 1
    return self.__piece_count

  def reset_logic(self) :
    self.__play_squares = []
    self.__flip_squares = []

  def left(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index > 0 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index -= 1
      self.left(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def right(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index < 7 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index += 1
      self.right(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def left_top_diag(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index > 0 and row > 0 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index -= 1
      row -= 1
      self.left_top_diag(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def top(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if row > 0 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      self.grid_point(row, index)
      row -= 1
      self.top(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def right_top_diag(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index < 7 and row > 0 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index += 1
      row -= 1
      self.right_top_diag(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def right_bottom_diag(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index < 7 and row < 7 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index += 1
      row += 1
      self.right_bottom_diag(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def bottom(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if row < 7 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      row += 1
      self.bottom(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def left_bottom_diag(self, board, row, index, flip_squares, play_square, counter) :
    check = board[row][index]
    grid_point = self.grid_point(row, index)
    if index > 0 and row < 7 and check == self.__enemy_color :
      counter += 1
      flip_squares.append(grid_point)
      index -= 1
      row += 1
      self.left_bottom_diag(board, row, index, flip_squares, play_square, counter)
    elif counter >= 1 and type(check) is int and len(flip_squares) > 0:
      play_square.append(grid_point)

  def logic_test(self, board, row=0) :
    for index, value in enumerate(board[row], start = 0) :
      left_index = index - 1
      top_row = row - 1
      right_index = index + 1
      bottom_row = row + 1
      if value == self.__player_color :
        if index > 0 :
          flip_squares = []
          play_square = []
          self.left(board, row, left_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if row > 0 :
          flip_squares = []
          play_square = []
          self.top(board, top_row, index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if index < 7 :
          flip_squares = []
          play_square = []
          self.right(board, row, right_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if row < 7 :
          flip_squares = []
          play_square = []
          self.bottom(board, bottom_row, index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if index > 0 and row > 0 :
          flip_squares = []
          play_square = []
          self.left_top_diag(board, top_row, left_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if index < 7 and row > 0 :
          flip_squares = []
          play_square = []
          self.right_top_diag(board, top_row, right_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if index < 7 and row < 7 :
          flip_squares = []
          play_square = []
          self.right_bottom_diag(board, bottom_row, right_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
        if index > 0 and row < 7 :
          flip_squares = []
          play_square = []
          self.left_bottom_diag(board, bottom_row, left_index, flip_squares, play_square, 0)
          if len(play_square) > 0 :
            self.__flip_squares.append(flip_squares)
            self.__play_squares.append(play_square[0])
    if row < 7 :
      row += 1
      return self.logic_test(board, row)
