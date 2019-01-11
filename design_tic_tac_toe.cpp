// https://leetcode.com/problems/design-tic-tac-toe/
#include <vector>
class TicTacToe {
public:
    /** Initialize your data structure here. */
    int n_;
    vector<int> diagonal_1{0,0};
    vector<int> diagonal_2{0,0};
    vector<vector<int>> rows;
    vector<vector<int>> cols;
    
    TicTacToe(int n) {
        n_ = n;
        for (int i = 0; i < 2; i++) { 
            vector<int> arr;
            for (int j = 0; j < n; j++){
                arr.push_back(0);
            }
            rows.push_back(arr);
        }
        for (int i = 0; i < 2; i++) { 
            vector<int> arr;
            for (int j = 0; j < n; j++){
                arr.push_back(0);
            }
            cols.push_back(arr);
        }
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        if (row == col){
            diagonal_1[player-1] += 1;
        }
        
        if (col == n_ - 1 - row){
            diagonal_2[player-1] += 1;
        }
        
        rows[player-1][row] += 1;
        cols[player-1][col] += 1;
        
        if( (rows[player-1][row] == n_) or\ // dsfd
           (cols[player-1][col] == n_) or (diagonal_1[player-1] == n_) or (diagonal_2[player-1] == n_) ){
            return player;
        }
        else {
            return 0;
        }
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */