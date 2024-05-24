class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<int>> rows(9), cols(9), blocks(9);

        for (int col = 0; col < 9; col++) {
            for (int row = 0; row < 9; row++) {
                if (board[col][row] == '.') {
                    continue;
                }

                int curr = board[col][row] - '0';
                int currBox = (col / 3) * 3 + (row / 3);
                if (rows[row].count(curr) || cols[col].count(curr) || blocks[currBox].count(curr)) {
                    return false;
                }

                rows[row].insert(curr);
                cols[col].insert(curr);
                blocks[currBox].insert(curr);
            }
        }
        return true;
    }
};
