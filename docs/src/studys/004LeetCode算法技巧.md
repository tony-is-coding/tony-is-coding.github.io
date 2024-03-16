### 前缀和数组
> 针对一堆数组与二维数组构建对应的前缀和数组 prefixSum

- **一维数组**
```java
prefixSum = new int[nums.length];
prefixSum[0] = nums[0];
for (int i = 1; i < nums.length; i++) {
    prefixSum[i] = nums[i] + prefixSum[i - 1];
} 
```

-  **二维数组**
```java
final int rows = matrix.length; // 行数
final int cols = matrix[0].length; // 列数
prefixSum = new int[rows][cols];
prefixSum[0][0] = matrix[0][0];
// 初始化边界填充
for (int i = 1; i < rows; i++) {
    prefixSum[i][0] = prefixSum[i - 1][0] + matrix[i][0];
}
for (int j = 1; j < cols; j++) {
    prefixSum[0][j] = prefixSum[0][j - 1] + matrix[0][j];
}
for (int i = 1; i < rows; i++) {
    for (int j = 1; j < cols; j++) {
        prefixSum[i][j] = matrix[i][j] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1];
    }
} 
```

##### 算法真题: 
**查询数组或二维数组的部分区间和**
> 前缀和主要适⽤的场景是原始数组不会被修 改的情况下，频繁查询某个区间的累加和

1. (LC303) 部分动态和 如求： 原数组下标  j 到 k (j <= k)的数字和 ; 通过前缀和相减
2. (LC304) 求二维数组矩形体  (i,j) -> (p,k) 内的数字和
3. (LC560) 动态求一维数组中连续和为 n 的子序列;
4. (LC363) 求二维数组中和为 n 的矩形的数量, 或者和不超过 n 的数组数量(暂时未解出)

### 差分数组
> 差分数组经典问题： 数组连续区间增加一个指定的值(LC370)

**解决场景**：

- 连续区间增加指定值
- 多次调用上面操作性能问题

**基本思路为**: 构建差分数组 -> 连续区间累加 -> 倒推原始数组的流程
场景示例 :
```
原始数组：  8   2   6   3   1
差分数组：  8  -6   4  -3  -2 (差分数组的原理是 diff[i] = arr[i] - arr[i-1])

定向累加, 加上需要从下标 1 -> 3 每项累加5, 那么做法是 diff[1] += 5; diff[3+1] -=5;
原理是:
- 差分数组反推是 res[i] = diff[i] + res[i-1];  意味着, 只要再 i 位置加 n, 原数组 i以及i之后的每一项都会再反推过程中 加n；
- 通过再 j+1 位置减去n, 那么就抵消了 j + 1 到 length 位置的增量变化了

增量增加后的数组：
8  -3  4 -3  -5
反推出原始数组：
8   5  9  6  1 (完成了  1 - 3 位置加 3 的操作)
```

**相关代码示例**
```java
public static void main(int[] arr){
    int[] diff = new int[arr.length];
    diff[i] = arr[i] - arr[i-1]; // 构建差分数组
    arr[i] = diff[i] + arr[i-1]; // 通过上面的公示反推原数组
    // 差分数组累加 实现 i到j位置每一项加n
    diff[i] += n
    diff[j+1] -=n
}
```
##### 算法真题

1. (LC370)  对一个数组的多个连续区间进行增加随机数字 n ;
2. (LC1109) 航班预定问题, 多份预定清单, 每份清单对多个航班进行不同位置数量预定, 求每个航班被预定的位置数量
3. (LC1194) 顺风车问题, 多个乘客出现计划

### 滑动窗口问题

1. 滑动窗口方案很多，本质上都是基于双指针, 同时可以通过加入缓存或者计数器之类的操作， 通过滑动窗口来求最值(LC76)
2. 滑动窗口常见的解决的场景是字串问题

**滑动窗口的基本公式 伪代码**：
```java
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        // c 是将移⼊窗⼝的字符
        char c = s[right];
        // 右移窗⼝
        right++;
        // 进⾏窗⼝内数据的⼀系列更新
        ...
        while (window needs shrink) { // 判断左侧窗⼝是否要收缩, 设定一个需要进行左收缩的边界值
            // d 是将移出窗⼝的字符
            char d = s[left];
            // 左移窗⼝
            left++;
            // 进⾏窗⼝内数据的⼀系列判断与更新
            ...
          }
      }
}
```

**示例题目**： **给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度(LC3)**
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        if (len <= 1) {
            return len;
        }
        char[] cc = new char[128];
        char[] cs = s.toCharArray();
        int left = 0;
        int right = -1;
        int max = 0;
        while (right < len - 1) {
            right++;
            char c = cs[right];
            int ci = cc[c];
            if (ci == 0) {
                cc[c] = 1;
                max = Math.max(right - left + 1, max);
            } else if (ci == 1) {
                cc[c] = 2;
                while (cc[c] == 2 && left <= right) {
                    cc[cs[left]] -= 1;
                    left++;
                }
            }
        }
        return max;
    }
}
```
### 二分搜索


### 单调栈
> 通过遍历逐个迭代构造一个单调递增或者递减的栈

```java
// eg: 通过构造一个单调递增栈 输出一个
int[] nextGreaterElement(int[] arr) {
    int len = arr.length;
    int[] res = new int[len];
    int[] stack = new int[len];
    int pos = -1;
    for (int e = len - 1; e >= 0; e--) {
        while (pos != -1 && stack[pos] <= arr[e]) { // 所有元素都只会被 push 一次 + pop 一次即时间复杂度为 2n = O(n)
            pos--;
        }
        res[e] = pos == -1 ? -1 : stack[pos];
        stack[++pos] = arr[e];
    }
    return res;
}
```

单调栈主要思路：

- 单调栈是一个辅助栈
- 正向遍历变为逆向遍历, 逆向入栈：比如要查找一周 7 天里， 每一天至少需要 几天才能升温, 逆向遍历到 i 时, 其实已经知道 i 到七的所有结果
- 栈的构造需要不断保证 最值(最大/最小/最接近/最大差) 在栈顶, 将不满足的值剔除栈
- 在处理完成当前节点往前走的时候, 需要将当前点加入单调栈
- 特殊的：处理循环数组 可以考虑将数组长度翻倍

**示例： leetcode 739 / leetcode 503**
```java
public class LC739 {
    static class Solution {
        public int[] dailyTemperatures(int[] temperatures) {
            int len = temperatures.length;
            int[] res = new int[len];
            int[] stack = new int[len];
            int[] stackIdx = new int[len];
            int stackPos = -1;
            for (int i = len - 1; i >= 0; i--) {
                while (stackPos != -1 && stack[stackPos] <= temperatures[i]) {
                    stackPos--;
                }
                res[i] = stackPos == -1 ? 0 : stackIdx[stackPos] - i;
                // 当前元素压入栈
                stackPos++;
                stack[stackPos] = temperatures[i];
                stackIdx[stackPos] = i;
            }
            return res;
        }
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] res = solution.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73});
        System.out.println(Arrays.toString(res));
    }
}
```

### 单调队列

### 二叉树


### 二叉树还原
> 通过 前中后序遍历中的两种还原原来的二叉树系列

**要点:**

- 二叉树的遍历递归顺序遵循 `先序: 根左右s 中序: 左根右 后序: 左右根`
- 先序遍历的根节点肯定在0位置
- 后序遍历的根节点肯定在 len - 1 位置
- 中序遍历根节点左边的在左子树,右边的在右子树
- 遍历顺序虽然不同, 但是同一颗子树的节点数量是一样的
- 通过前后序来还原时:  剔除root节点后, 确认先序遍历剩余节点的第一个节点在后序遍历的位置, 后序遍历中该节点前的数据为左子树数据, 节点后的数据为右子树数据
二叉搜索树
- 左子树的所有节点都比当前节点小
- 右子树的所有节点都比当前节点大
- 中序遍历有序性
- 本质上还是递归思想

### 回溯
**回溯算法的核心公式**
```python
result = []
def backtrack(路径, 可选列表):
    if 满足结束条件:
        result.add(路径)
        return;
    for 可选路径 in 可选列表:
        可选列表.remove(可选路径)
        backtrack(可选路径, 剩余可选列表)
        可选列表.add(可选路径)
```
### 深度优先算法(DFS)
**深度优先遍历, 本质是**`**不撞南墙不回头**`**, 但是需要重点关注几个点**

1. 南墙(边界) 是什么?
2. 回头了做什么(状态保留)?
3. 记录什么(求值)?

**场景示例: 深度优先算法解决岛屿问题**

1. 双层嵌套遍历地图获取陆地块
2. 深度遍历当前岛屿的所有的陆地,并将陆地淹没更改成海水
3. 在这个过程中可以做:
- 统计陆地块数
- 统计岛屿数量
- 统计被海水包围的陆地(1. 淹没地图边缘的岛屿 2. 统计剩余的岛屿)

### 广度优先遍历
**广度优先遍历一般会用来求最短路径或者最小编辑次数等**

1. 二叉树最小高
2. 迷宫游戏最少次数
3. 最小编辑距离(待定思考)?

**广度优先遍历一般是借鉴层次遍历思想来解决问题, 一层一层去查找目标值, 基于上一层衍生下一层, 通过队列进行头进尾出遍历**

1. 抽象行为, 将要解决的问题抽象成一颗 n 叉树
2. 层次遍历, 同来统计状态变化次数
3. 访问记录字典, 减少重复子树

### 动态规划
> 动态规划可以先通过递归 + 减枝的思路来做出基本模型,然后推出变化条件, 推导出动态规划框架

**动态规划核心框架**

1. 确定状态
2. 找到转移公式
3. 确定初始条件以及边界条件
4. 计算结果
##### 示例: 找零钱问题
```java
public class CoinChange {
    /*
    1. 确定状态
    2. 找到转移公式
    3. 确定初始条件以及边界条件
    4. 计算结果。
    动态分析：
    1. 状态分析: 对于dp-table dp[j] 代表凑成数字 j 所需要最少的硬币数量
    2. 对于任意 dp[j] 从所有的coin中挑出一个 coin 使得 dp[j-coin] 最小
    dp[j] = 1 + min(dp[j-coin1], dp[j-coin2]... dp[j-coinM])
    3. 边界条件与初始条件
        - j < coin 时, 跳过coin
        - dp[0] = 0
        - 必然会有结果这个时最大的前提
    4. 求 dp[amount]

    思路:
    1. 先按照dfs的思路递归, 求最小使用coin 树
    2. 添加dpTable 进行重复子树剪枝
    3. 将递归优化成遍历(可选的)
    */
    
    int coinChange1(int[] coins, int amount){
        if(amount == 0){
            return 0;
        }
        int res = amount + 1;;
        for(int coin:coins){
            if(coin > amount){
                continue;
            }
            int dfs = coinChange1(coins, amount - coin);
            if(dfs != -1){
                res = Math.min(res, 1 + dfs);
            }
        }
        return res == amount + 1?-1:res;
    }
    
    int coinChange(int[] coins, int amount) {
        if (amount <= 1) {
            return amount;
        }
        // 题⽬要求的最终结果是 dp(amount)
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i < amount + 1; i++) {
            for (int coin : coins) {
                if (coin > i) {
                    continue;
                }
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
            }
        }
        return dp[amount];
    }
}
```


#### 动态规划经典问题系列


##### LC72 最短编辑距离

```java
class Solution {
    /*
    给你两个单词word1 和word2， 请返回将word1转换成word2 所使用的最少操作数
    你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
    定义：dp(i, j) 返回 s1[0..i] 和 s2[0..j] 的最⼩编辑距离
    抽象对单词的操作新为:
    word[i] == word[j] 相同; 不需要操作, 直接统一往前进行推移
    插入一个字符    即在 word1[i+1] 最后写入一个 word2[j] ,等价于将word2[j]的字符删除, 再求word1[0..i] 变成word2[0..j-1] 的最小编辑距离
    删除一个字符    即将word2[i]的字符删除, 再求word1[0..i-1] 变成word2[0..j] 的最小编辑距离
    替换一个字符    替换一个字符则是将 word1[i] 虚拟设置为 word2[j] 然后将i,j 往前,继续求 word1[0..i-1] 变成word2[0..j-1] 的最小编辑距离
    */
    public int minDistance(String word1, String word2) {
        char[] cs1 = word1.toCharArray();
        char[] cs2 = word2.toCharArray();
        int[][] dp = new int[cs1.length + 1][cs2.length+1];
        // 边界值填充
        for(int row = 1; row <= cs1.length; row ++){
            dp[row][0] = row;
        }
        for(int col = 1;col <= cs2.length; col++){
            dp[0][col] = col;
        }
        for(int i = 1; i <= cs1.length ; i++){
            for(int j = 1;j <= cs2.length ; j++){
                if(cs1[i - 1] == cs2[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.min(
                        dp[i-1][j] + 1,
                        Math.min(dp[i][j-1] + 1, dp[i-1][j-1] + 1)
                    );
                }
            }
        }
        return dp[cs1.length][cs2.length];
    }
}
```

##### LC1143 最长公共子序列问题(递归版本)

```java
class Solution2 {
    /*
    给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
    一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
    两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
    示例 1：
    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace" ，它的长度为 3
    
    示例 2：
    输入：text1 = "abc", text2 = "abc"
    输出：3
    解释：最长公共子序列是 "abc" ，它的长度为 3
    
    示例 3：
    输入：text1 = "abc", text2 = "def"
    输出：0
    解释：两个字符串没有公共子序列，返回 0
    */
    int[][] memeory;
    public int longestCommonSubsequence(String text1, String text2) {
        // 思路:  对于任意的两个字符串, 求最长的公共子序列都是求的到 两个字符串截止点 i,j 的最长公共子序列
        // 那么针对 i,j 有多种可能, i == j 与 i != j
        
        
        char[] cs1 = text1.toCharArray();
        char[] cs2 = text2.toCharArray();
        memeory = new int[cs1.length][cs2.length];
        for(int[] is: memeory){
            Arrays.fill(is,-1);
        }
        return recursive(cs1,cs1.length-1,cs2,cs2.length-1);
        
    }
    public int recursive(char[] cs1, int i, char[] cs2, int j){
        if(i <0 || j <0){
            return 0;
        }
        if(memeory[i][j] != -1){
            return memeory[i][j];
        }
        
        if(cs1[i] == cs2[j]){
            memeory[i][j] = 1 + recursive(cs1, i-1,cs2, j-1);
        }else{
            memeory[i][j] = Math.max(recursive(cs1, i-1,cs2,j), recursive(cs1,i,cs2,j-1));
        }
        return memeory[i][j];
    }
}




class Solution1{
    public static int longestCommonString(String s1, String s2){
         
    }
        
    
}
```


