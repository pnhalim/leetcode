class Solution {
public:  
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // indegree list
        vector<int> indegree(numCourses);
        // adj list
        unordered_map<int, vector<int>> adj;
        
        for (const vector<int> &prereq : prerequisites) {
            indegree[prereq[1]]++;
            if (adj.find(prereq[0]) != adj.end()) {
                adj[prereq[0]].push_back(prereq[1]);
            }
            else {
                adj[prereq[0]] = {prereq[1]};
            }
        }
        
        // bfs
        int nodesVisited = 0;
        queue<int> bfs;
        for (int course = 0; course < numCourses; course++) {
            if (indegree[course] == 0) {
                bfs.push(course);
            }
        }
        while (!bfs.empty()) {
            int course = bfs.front();
            bfs.pop();
            nodesVisited++;
            // subtract from indegree list
            for (int prereq : adj[course]) {
                indegree[prereq]--;
                if (indegree[prereq] == 0) {
                    bfs.push(prereq);
                }
            }
        }
        
        return nodesVisited == numCourses;
    }
};