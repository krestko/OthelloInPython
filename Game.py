from Components.Player import Player
from Components.Pieces import Pieces
from Components.Board import Board

class Game :

  def __init__(self, player_one, player_two) :
    self.__player_one = player_one
    self.__player_two = player_two
    self.__turn = self.__player_one
    self.__pieces = Pieces()
    self.__board = Board()
    self.__poss_player_moves = []

  def toggle_turn(self) :
    self.__turn = self.__player_two if self.__turn == self.__player_one else self.__player_one

  def player_piece_count(self) :
    if self.__turn.print_piece_count() == 0 :
      return True

  def calculate_score(self) :
    black = 0
    white = 0
    for index, value in enumerate(self.__board.return_board()) :
      for ind, val in enumerate(value) :
        if val == 'Black' :
          black += 1
        elif val == 'White' :
          white += 1
    if black > white :
      print('BLACK WINS!')
    elif white > black :
      print('WHITE WINS!')
    else :
      print('TIE GAME')

  def prep_turn(self) :
    self.__board.display_board()
    self.__pieces.remove_game_pieces()
    self.__turn.reset_logic()
    self.__turn.logic_test(self.__board.return_board(), row=0)

  def play_turn(self) :
    self.prep_turn()
    if self.player_piece_count() or len(self.__turn.choices()) == 0:
      return self.calculate_score()
    player = 'Player One ({}):'.format(self.__player_one.print_player_color()) if self.__turn == self.__player_one else 'Player Two ({}):'.format(self.__player_two.print_player_color())
    move = input(player)
    self.__board.change(float(move), self.__turn.print_player_color(), self.__turn)
    self.toggle_turn()
    self.play_turn()

test_game = Game(Player('Kat', 'Black'), Player('Ghazal', 'White'))
print(test_game.play_turn())