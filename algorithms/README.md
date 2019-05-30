### 算法汇总
- 算法原理
- 算法题  
1、[Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)（[源码]()）  
**大意**：比较两个字符串是否相等，其中字符串中的#代表删除，例：abc#==abcc##==ab。要求时间复杂度O(n)，空间复杂度O(1)   
**分析**：如果用栈很容易实现，#代表出栈，其余字符为入栈，时间复杂度为O(n)，但空间复杂度也是O(n)。  
**引申**：  

