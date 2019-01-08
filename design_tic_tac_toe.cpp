#include <iostream>

// Square NxN board, win with N consecutive.
class TicTacToe {
 public:
  TicTacToe(){
      
  }
  ///
  /// \brief MakeMove Interface for the game playing system to add a new move to
  /// the game.
  /// \param player   Player making this move.
  /// \param location The selected location on the board.
  /// \return Result of the move, including the new game status such as Win, Invalid, etc.
  ///
  //Result MakeMove(Player player, Location location);

private:
  int n;

  /// Create a representation of the game state and any internal structures to help
  /// determine win conditions. The implementation should easily extend to different
  /// board sizes and run time should scale linearly (or better) with N.
};


int main(int argc, char** argv) {
  std::cout << "Starting test!" << std::endl;

 // Add some useful test cases.
  // result = game.MakeMove(Player, Location)
  // Check result is correct.

 return 0;
}