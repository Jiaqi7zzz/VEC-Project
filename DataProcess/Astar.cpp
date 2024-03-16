#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

class Node {
public:
    pair<int, int> position;
    Node* parent;
    int g;
    int h;
    int f;

    Node(pair<int, int> pos, Node* par = nullptr) : position(pos), parent(par), g(0), h(0), f(0) {
        f = g + h;
    }

    bool operator<(const Node& other) const {
        return f < other.f;
    }

    bool operator==(const Node& other) const {
        return position == other.position;
    }
};

double get_distance(pair<int, int> pos1, pair<int, int> pos2) {
    return sqrt(pow(pos1.first - pos2.first, 2) + pow(pos1.second - pos2.second, 2));
}

vector<pair<int, int>> Astar(pair<int, int> start, pair<int, int> goal, vector<vector<int>>& grid) {
    vector<Node*> open_list;
    vector<Node*> closed_list;
    Node* start_node = new Node(start);
    Node* goal_node = new Node(goal);
    open_list.push_back(start_node);
    vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    while (!open_list.empty()) {
        Node* current_node = *min_element(open_list.begin(), open_list.end(), [](const Node* a, const Node* b) {
            return a->f < b->f;
        });
        open_list.erase(remove(open_list.begin(), open_list.end(), current_node), open_list.end());
        closed_list.push_back(current_node);

        if (current_node->position == goal_node->position) {
            vector<pair<int, int>> path;
            while (current_node->parent) {
                path.push_back(current_node->position);
                current_node = current_node->parent;
            }
            path.push_back(start_node->position);
            reverse(path.begin(), path.end());
            return path;
        }

        for (auto direction : directions) {
            int next_x = current_node->position.first + direction.first;
            int next_y = current_node->position.second + direction.second;
            Node* next_node = new Node({next_x, next_y}, current_node);

            if (next_x < 0 || next_x >= grid.size() || next_y < 0 || next_y >= grid[0].size() || grid[next_x][next_y] == 1) {
                continue;
            }

            next_node->g = current_node->g + get_distance(next_node->position, current_node->position);
            next_node->h = abs(next_x - goal_node->position.first) + abs(next_y - goal_node->position.second);
            next_node->f = next_node->g + next_node->h;

            auto it_closed = find_if(closed_list.begin(), closed_list.end(), [&](Node* n) { return *n == *next_node; });
            if (it_closed != closed_list.end()) {
                continue;
            }

            auto it_open = find_if(open_list.begin(), open_list.end(), [&](Node* n) { return *n == *next_node; });
            if (it_open != open_list.end()) {
                Node* existing_node = *it_open;
                if (existing_node->f > next_node->f) {
                    open_list.erase(remove(open_list.begin(), open_list.end(), existing_node), open_list.end());
                }
            }

            open_list.push_back(next_node);
        }
    }

    return vector<pair<int, int>>();
}

ostream& operator<<(ostream& cout , const pair<int,int>& point){
    cout << "(" << point.first << "," << point.second << ")" << " -> ";
    return cout;
}

// vector<vector<int>> read_map(string filename) {
//        //
// }
vector<vector<int>> map = {

};

int main() {
    vector<vector<int>> map = {
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 1, 1, 0}
    };
    pair<int, int> start = make_pair(0, 0);
    pair<int, int> goal = make_pair(2, 3);
    vector<pair<int, int>> res = Astar(start, goal, map);
    for(pair<int,int> p : res){
        cout << p;
    }

    return 0;
}
