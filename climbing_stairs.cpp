class Solution { // O(n) time and O(n) space
public:
    map<int,int> d;
    int climbStairs(int n) {
        if (n == 2){
            return 2;
        }
        else if(n == 1){
            return 1;
        } else if (d.find(n) != d.end()){
            return d[n];
        }
        d[n] = climbStairs(n-2) + climbStairs(n-1);
        return d[n];
    }
};

//Direct iterative fibonacci, without saving intermediate states! O(1) space, O(n) compute

// Binets Method (uses matrix multiplication to obtain nth fib number) [[1,1],[1,0]] ^ n = F(n) {or in our case [[1,0],[0,1]}
// But the implementation below is also good, matrix multiplication can use GPUs to be even faster!
//  public class Solution {
//     public int climbStairs(int n) {
//         int[][] q = {{1, 1}, {1, 0}};
//         int[][] res = pow(q, n);
//         return res[0][0];
//     }
//     public int[][] pow(int[][] a, int n) {
//         int[][] ret = {{1, 0}, {0, 1}};
//         while (n > 0) {
//             if ((n & 1) == 1) {
//                 ret = multiply(ret, a);
//             }
//             n >>= 1;
//             a = multiply(a, a);
//         }
//         return ret;
//     }
//     public int[][] multiply(int[][] a, int[][] b) {
//         int[][] c = new int[2][2];
//         for (int i = 0; i < 2; i++) {
//             for (int j = 0; j < 2; j++) {
//                 c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
//             }
//         }
//         return c;
//     }
// }


// Another solution could have been Fibonacci formula O(log(n)) complexity, O(1) space. because pow function takes log(n)