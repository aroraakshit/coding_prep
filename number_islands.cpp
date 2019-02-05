class Solution { // based on dfs
public:
    void mark(vector<vector<char>>& grid, vector<vector<int>>& visited, int i, int j){
        if(j<0 || i<0 || i>=visited.size() || j >= visited[i].size() || visited[i][j] || grid[i][j] != '1' ){
            return;
        }
        visited[i][j] = 1;
        mark(grid, visited, i, j+1);
        mark(grid, visited, i+1, j);
        mark(grid, visited, i, j-1);
        mark(grid, visited, i-1, j);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<int>> visited{};
        for(int i=0; i<grid.size(); i++){
            vector<int> row{};
            for(int j = 0; j < grid[i].size(); j++){
                row.push_back(0);
            }
            visited.push_back(row);
        }
        
        int num_islands = 0;
        
        for(int i=0; i<grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
             if( visited[i][j] == 0 and grid[i][j] == '1'){
                 num_islands++;
                 mark(grid, visited, i, j);
             }   
            } 
        }
        return num_islands;
    }
};