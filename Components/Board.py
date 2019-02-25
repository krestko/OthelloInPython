import math

class Board :

  def __init__(self) :
    self.__board = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 'Black', 'White', 5, 6, 7], [0, 1, 2, 'White', 'Black', 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]

  def return_board(self) :
    return self.__board

  def flip(self, row, index, color) :
    if index == 0 :
      self.__board[row - 1][index + 7] = color
    else :
      self.__board[row][index - 1] = color

  def change(self, piece, color, player) :
    player.remove_player_piece()
    row = math.trunc(piece / 8)
    index = math.trunc(piece - row * 8)
    self.flip(row, index, color)
    indices = [index for index, x in enumerate(player.choices()) if x == math.trunc(piece)]
    for index, value in enumerate(indices) :
      flips = player.flips()[value]
      for index, value in enumerate(flips) :
        row = math.trunc(value / 8)
        index = math.trunc(value - row * 8)
        self.flip(row, index, color)

  def display_board(self) :
    for index, value in enumerate(self.__board) :
      row = []
      for ind, val in enumerate(self.__board[index]) :
        if type(val) is str :
          row.append(val)
        else :
          row.append((index + 1) * 8 - (8 - (ind + 1)))
      space = ' '
      for item in row :
        if item == 'Black' or item == 'White' :
          space += str(item) + '  '
        elif len(str(item)) == 1 :
          space += str(item) + '      '
        else :
          space += str(item) + '     '
      print(space)