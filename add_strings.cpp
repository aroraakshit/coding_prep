class Solution { // 4ms
public:
    string addStrings(string num1, string num2) {
        int c=0;
        string ans="";
        cout<<num1<<" , "<<num2<<endl;
        while(!num1.empty() || !num2.empty() || c!=0){
            int x = (!num1.empty()) ? num1[num1.size()-1] - '0' : 0;
            int y = (!num2.empty()) ? num2[num2.size()-1] - '0' : 0;
            int z = x+y+c;
            int v = z % 10;
            ans.insert(0, to_string(v));
            c = z/10;
            // cout<<x<<" , "<<y<<" , "<<c<<" , "<<z << " : "<<ans<<endl;
            // cout<<num1<<" , "<<num2<<" , "<<c<<endl;
            if(!num1.empty()){
                num1.pop_back();
            }
            if(!num2.empty()){
                num2.pop_back();
            }
            
        }
        return ans;   
    }
};