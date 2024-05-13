class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return false;
        }


        int lowRow, highRow;
        for (lowRow = 0, highRow = matrix.size() - 1; lowRow <= highRow;) {
            int mid = (lowRow + highRow) / 2;
            if (matrix[mid][0] < target) {
                lowRow = mid + 1;
            } else if (matrix[mid][0] > target) {
                highRow = mid - 1;
            } else {
                return true;
            }
        }

        for (int low = 0, high = matrix[highRow].size() - 1; low <= high;) {
            int midIdx = (low + high) / 2;
            if (matrix[highRow][midIdx] < target) {
                low = midIdx + 1;
            } else if (matrix[highRow][midIdx] > target) {
                high = midIdx - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
