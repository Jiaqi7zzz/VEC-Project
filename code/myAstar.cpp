#include<iostream>
#include<vector>
#include<cmath>
#include<queue>
#include<algorithm>
#include<unordered_set>
using namespace std;

class Node{
public:
    int m_g = 0;
    int m_h = 0;
    int m_f = m_g + m_h;
    Node* m_parent;
    pair<int,int> m_pos;
    Node(pair<int,int> pos):m_pos(pos),m_parent(nullptr){ m_f = m_g + m_h;}
    Node(pair<int,int> pos,Node* parent):m_pos(pos),m_parent(parent){m_f = m_g + m_h;}
    bool operator<(const Node& other) const{
        return this -> m_f < other.m_f;
    }
    bool operator==(const Node& other) const{
        return this -> m_pos.first == other.m_pos.first 
        && this -> m_pos.second == other.m_pos.second;
    }
    bool operator!=(const Node& other) const{
        return this -> m_pos.first != other.m_pos.first
        || this -> m_pos.second != other.m_pos.second;
    }
};

double get_distance(const Node& Node1 , const Node& Node2){
    double res = sqrt(pow(Node1.m_pos.first - Node2.m_pos.first,2) 
                 + pow(Node1.m_pos.second - Node2.m_pos.second,2));
    return res;
}

// class Heap_cmp{
// public:
//     bool operator()(const Node& Node1,const Node& Node2){
//         return Node1.m_f > Node2.m_f;
//     }
// };

vector<Node> Astar(pair<int,int> & start , pair<int,int> & goal , vector<vector<int>> & map){
    // vector<Node> open_list;
    priority_queue<Node> heap;
    // unordered_set<Node> set;
    vector<Node> open_list;
    vector<Node> close_list;
    Node start_node = Node(start);
    Node goal_node = Node(goal);
    heap.push(start_node);
    // set.insert(start_node);
    open_list.emplace_back(start_node);

    vector<vector<int>> directions({{0,1},{0,-1},{1,0},{-1,0}});
    while(!heap.empty()){
        // && find(open_list.begin(),open_list.end(),goal_node) == open_list.end()
        Node current_node = heap.top();
        heap.pop();
        open_list.erase(remove(open_list.begin(),open_list.end(),current_node),open_list.end());
        // open_list.erase(std::remove_if(open_list.begin(),open_list.end(),[&](const Node& Node1){return Node1.m_pos == current_node.m_pos;}),open_list.end());
        // set.erase(current_node);
        open_list.erase(remove(open_list.begin(),open_list.end(),current_node),open_list.end());
        close_list.emplace_back(current_node);
        if(current_node == goal_node){
            vector<Node> path;
            while(*current_node.m_parent != start_node){
                path.emplace_back(current_node);
                current_node = *current_node.m_parent;
            }
            path.emplace_back(start_node);
            std::reverse(path.begin(),path.end());
            return path;
        }

        for(auto dir : directions){
            int next_x = current_node.m_pos.first + dir[0];
            int next_y = current_node.m_pos.second + dir[1];
            Node next_node = Node(make_pair(next_x,next_y),&current_node);

            if(next_x < 0 || next_x >= map.size() || next_y < 0 
            || next_y >= map[0].size() || map[next_x][next_y] == 1){
                continue;
            }
            next_node.m_g = current_node.m_g + get_distance(current_node,next_node);
            next_node.m_h = abs(next_x - goal_node.m_pos.first) + abs(next_y - goal_node.m_pos.second);
            next_node.m_f = next_node.m_g + next_node.m_h;

            if(find(close_list.begin(),close_list.end(),next_node) != close_list.end()){
                continue;
            }

            if(find(open_list.begin(),open_list.end(),next_node) != open_list.end()){
                for(auto node : open_list){
                    if(node == next_node && node.m_f > next_node.m_f){
                        open_list.erase(remove(open_list.begin(),open_list.end(),node),open_list.end());
                        // open_list.push_back(next_node);
                        break;
                    }
                }
            }
            heap.push(next_node);
            open_list.push_back(next_node);
        }
    }
    return {};
}

int main(){
    vector<vector<int>> map = {
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 1, 1, 0}
    };
    pair<int,int> start = make_pair(0,0);
    pair<int,int> goal = make_pair(2,2);
    vector<Node> res = Astar(start , goal , map);
    // for(auto node : res){
    //     cout << node.m_pos.first << node.m_pos.second << " ";
    // }
    // cout << endl;
    cout << res.size();
}