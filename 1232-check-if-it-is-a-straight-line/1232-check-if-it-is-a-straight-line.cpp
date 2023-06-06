class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        // special case (div by 0)
        int x = coordinates[0][0];
        bool vertical = true;
        for (vector<int> &point : coordinates) {
            if (point[0] != x) {
                vertical = false;
                break;
            }
        }
        if (vertical) {
            return true;
        }

        // normal case
        double slope = (double)(coordinates[0][1] - coordinates[1][1]) 
                        / (coordinates[0][0] - coordinates[1][0]);
        for (int i = 2; i < coordinates.size(); i++) {
            double curr_slope = (double)(coordinates[0][1] - coordinates[i][1]) 
                        / (coordinates[0][0] - coordinates[i][0]);
            if (curr_slope != slope) {
                return false;
            }
        }
        return true;
    }
};