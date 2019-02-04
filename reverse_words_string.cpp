class Solution {
public:
    void reverseWords(string &s) {
        int slow=0;
        int fast=0;
        while(s[fast]==' ' and fast < s.size()) fast++;
        
        if(fast>=s.size()){
            s[0] = '\0';
            return;
        }
        char tmp = 'a';
        while(true){
            int last = slow;
            while(s[fast] != ' ' and fast < s.size()){
                s[slow++] = s[fast++];
            }
            
            for (int j =last; j<(last+slow)/2; j++){
                tmp = s[j];
                s[j] = s[last+slow-j-1];
                s[last+slow-j-1] = tmp;
            }
            // cout<<last<<" "<<slow-1<<" in "<<s<<" s[fast] = "<<fast<<" slow "<<slow<<endl;
            while(s[fast]==' ' and fast < s.size()) fast++;
            
            if(fast >= s.size()) break;
            
            s[slow++]=' ';
            
        }
        s[slow]='\0';
        int last = 0;
        for (int j =last; j<(last+slow)/2; j++){
            tmp = s[j];
            s[j] = s[last+slow-j-1];
            s[last+slow-j-1] = tmp;
        }
        
    }
};