class Solution { // 12ms
public:
    bool validUtf8(vector<int>& data) {
        int num_bytes = 0;
        int mask1 = 1 << 7;
        int mask2 = 1 << 6;
        for(int i =0; i < data.size(); i++){
            # for every byte
            int mask = 1 << 7;
            if (num_bytes == 0){
                while(data[i] & mask){
                    num_bytes += 1;
                    mask = mask >> 1;
                }
                if (num_bytes==0){
                    continue;
                }
                
                if (num_bytes == 1 or num_bytes > 4){
                    return false;
                }
                
            } else {
                // continuing character
                if (!((data[i] & mask1) and !(data[i] & mask2))){
                    return false;
                }
            }
            num_bytes -= 1;
        }
        return (num_bytes == 0);
    }
};

// 8ms solution, credits - leetcode:

// class Solution {
// public:
//     bool validUtf8(vector<int>& data) {
//         int count = 0;
//         for(auto c : data){
//             if(count == 0){
//                 if(c>>3 == 0b11110)
//                     count = 3;
//                 else if(c>>4 == 0b1110)
//                     count = 2;
//                 else if(c>>5 == 0b110)
//                     count = 1;
//                 else if(c>>7 != 0)
//                     return false;
//             }
//             else{
//                 if(c>>6 != 0b10)
//                     return false;
//                 count--;
//             }
//         }
//         return count==0;
//     }
// };