class Pieces :

  def __init__(self) :
    self.__pieces = 60

  def remove_game_pieces(self) :
    self.__pieces -= 1
    return self.__pieces

  def print_pieces(self) :
    return self.__pieces