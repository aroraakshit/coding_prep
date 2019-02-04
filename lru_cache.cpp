class LRUCache { // beats 13.51% of solutions, 112 ms and 10.8 MB
public:
    unordered_map<int, int> d;
    vector<int> queue;
    int capacity;
    
    LRUCache(int cap) {
        capacity = cap;
    }
    
    int get(int key) {
        if(d.find(key) == d.end()){
            return -1;
        }
        int val = d[key];
        queue.erase(remove(queue.begin(), queue.end(), key), queue.end()); // Erase-remove idiom
        queue.push_back(key);
        // cout<<"get"<<" "<<key<<endl;
        // for(auto i:queue){
        //     cout<<i<<endl;
        // }
        // cout<<" dict below:";
        // for(auto i:d){
        //     cout<<i.first<<":"<<i.second<<endl;
        // }
        // cout<<endl;
        return val;
    }
    
    void put(int key, int value) {
        if(d.find(key) != d.end()){
            d.erase(key);
            queue.erase(remove(queue.begin(), queue.end(), key), queue.end());
        }
        if(d.size() == capacity){
            // cout<<"hit capacity! del: "<<*queue.begin()<<endl;
            d.erase(*queue.begin());
            queue.erase(queue.begin());
        }
        d.insert(make_pair(key,value));
        queue.push_back(key);
        // cout<<"put"<<" "<<key<<" "<<value<<endl;
        // for(auto i:queue){
        //     cout<<i<<endl;
        // }
        // cout<<" dict below:";
        // for(auto i:d){
        //     cout<<i.first<<":"<<i.second<<endl;
        // }
        // cout<<endl;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

// could have used doubly linked list

// class LRUCache { // Credits - Leetcode
// public:
//     LRUCache(int capacity) : capacity_(capacity), head_(nullptr), tail_(nullptr) {}

//     int get(int key) {
//         // key not exists
//         auto it = hash_.find(key);
//         if (it == hash_.end())
//             return -1;

//         // key exists
//         // 1. get the node
//         // 2. move the node to the head
//         int ret = it->second->value;
//         move2head(it->second);
//         return ret;
//     }

//     void put(int key, int value) {
//         // key exists
//         auto it = hash_.find(key);
//         if (it != hash_.end()) {
//             Node* node = it->second;
//             node->value = value;
//             move2head(node);
//             return;
//         }

//         // key not exists
//         // 1. enough capacify
//         if (hash_.size() < capacity_) {
//             Node* node = new Node(key, value);
//             hash_[key] = node;
//             move2head(node);
//             return;
//         }
//         // 2. not enough capacity
//         Node* node = tail_;
//         removetail();
//         node->key = key;
//         node->value = value;
//         move2head(node);
//         hash_[key] = node;
//     }

// private:
//     struct Node {
//         int key;
//         int value;
//         Node* prev;
//         Node* next;

//         Node(): prev(nullptr), next(nullptr) {}
//         Node(int k, int v): key(k), value(v), prev(nullptr), next(nullptr) {}
//     };

//     // 1. tail_ cannot be nullptr
//     // 2. remove it from the linkedlist
//     // 3. remove it from hash table
//     void removetail() {
//         hash_.erase(tail_->key);
//         if (tail_->prev == nullptr) {
//             head_ = nullptr;
//             tail_ = nullptr;
//         } else {
//             Node* prev = tail_->prev;
//             prev->next = nullptr;
//             tail_->prev = nullptr;
//             tail_ = prev;
//         }
//     }

//     // 1. delete this node from linked list
//     //    there's a case the node is not in the linked list
//     // 2. add it into head
//     void move2head(Node* node) {
//         if (head_ == nullptr) {
//             head_ = tail_ = node;
//             return;
//         }
//         if (node == head_)
//             return;
//         if (node == tail_) {
//             node->prev->next = nullptr;
//             tail_ = node->prev;
//             node->prev = nullptr;
//             node->next = head_;
//             head_->prev = node;
//             head_ = node;
//             return;
//         }
//         if (node->prev == nullptr && node->next == nullptr) {
//             head_->prev = node;
//             node->next = head_;
//             head_ = node;
//             return;
//         }
//         node->prev->next = node->next;
//         node->next->prev = node->prev;
//         node->prev = nullptr;
//         node->next = head_;
//         head_->prev = node;
//         head_ = node;
//     }

//     int capacity_;
//     Node* head_;
//     Node* tail_;    // delete from the tail
//     unordered_map<int, Node*> hash_;
// };