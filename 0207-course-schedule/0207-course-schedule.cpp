class Solution {
public:
    bool find(int course_num, 
              const int numCourses, 
              const vector<vector<int>>& prerequisites, 
              unordered_map<int, vector<int>> &courses_with_prereqs,
              unordered_set<int> visited) {
        if (visited.find(course_num) != visited.end()) {
            return false;
        }
        if (courses_with_prereqs.find(course_num) != courses_with_prereqs.end()) {
            vector<int> prereqs = courses_with_prereqs[course_num];
            visited.insert(course_num);
            courses_with_prereqs.erase(course_num);
            for (int prereq : prereqs) {
                if (!find(prereq, numCourses, prerequisites, courses_with_prereqs, visited)) {
                    return false;
                }
            }
            return true;
        }
        // else
        return true;
    }
    
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // list of all courses you can't finish automatically and all their prereqs
        // course_num : prereqs
        unordered_map<int, vector<int>> courses_with_prereqs;
        vector<int> courses;
        
        // fill the map
        for (vector<int> &p : prerequisites) {
            if (courses_with_prereqs.find(p[0]) != courses_with_prereqs.end()) {
                courses_with_prereqs[p[0]].push_back(p[1]);
            }
            else {
                courses_with_prereqs[p[0]] = {p[1]};
                courses.push_back(p[0]);
            }
        }
        
        for (int course : courses) {
            unordered_set<int> visited;
            if (!find(course, numCourses, prerequisites, courses_with_prereqs, visited)) {
                return false;
            }
        }
        return true;
    }
};