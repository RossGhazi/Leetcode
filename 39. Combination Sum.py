# my own video
class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:  
            def backtracking(cur,target):                              
                if target<=0: # since threre is no zero,  < wil also work
                    return []   
                if (cur,target) in dic:
                    return dic[(cur,target)]
                res=[]
                for i in  range(cur, len(candidates)):
                    if candidates[i] > target:
                        continue
                    if candidates[i]==target:
                        res.append([target])
                    temp=backtracking(i,target-candidates[i])
                    res+=[item+[candidates[i]] for item in temp]
                dic[(cur,target)]=res    
                return res                        
            dic={}
            #Reverse Sorting will help here : We hit the cases where the target is exceeded first. Thus, prune helps here
            candidates.sort(reverse=True)
            return backtracking(0,target)
                
                
################################ Analysis
#above solution combinationSum_Recursion_memoization is best solution. It is based on:
#https://leetcode.com/problems/combination-sum/discuss/170940/python-solution 
# https://www.youtube.com/watch?v=3bH3yGZLzF4&t=2s



# 39. Combination Sum
# 6 solutions are compared. But combinationSum_Recursion_memoization is best and it should be used.

# combinationSum_path and combinationSum_index based  is backtracking: word case time complexity: 2^m (t^ target)
# combinationSum_index is a little bit better than combinationSum
# combinationSum_DP  is dynamic programming, which is faster :m*m*n
# best soloution is  combinationSum_Recursion_memoization

#ref:
# https://leetcode.com/problems/combination-sum/discuss/937255/Python-3-or-DFSBacktracking-and-Two-DP-methods-or-Explanations
# https://www.youtube.com/watch?v=GBKI9VSKdGg&t=606s 
# https://leetcode.com/problems/combination-sum/discuss/170940/python-solution  (for memoization)
# https://www.youtube.com/watch?v=3bH3yGZLzF4&t=2s


import random
import time

class Solution: 
    def combinationSum_path(self, candidates, target):         
        res=[]       
        def dfs(remaning,path,currenSum):           
            if currenSum==target:
                res.append(path)
                return
            if currenSum>target:                
                return
            for i in range(len(remaning)):
                n=remaning[i]
                dfs(remaning[i:],path+[n],currenSum+n)                        
        dfs(candidates,[],0)        
        return res
        
    def combinationSum_index(self, candidates, target):
        res=[]   
        def backtrack(path,index,currentSum):
            if currentSum==target:
                res.append(path[:])
                return
            if currentSum>target:
                return
            for i in range(index,len(candidates)):                  
                backtrack(path+[candidates[i]],i,currentSum+candidates[i])
        backtrack([],0,0)
        return res          

   
    def combinationSum_DP(self, candidates, target: int) :
        # we find dp[] for each number up to the target
        # for example dp[10] is all cases that sum will be 10
        # dp[target] will be all cases  that sum will be target
        dp = [[] for _ in range(target+1)]                    

        for c in candidates:                                 
            for i in range(c, target+1):             #we do not need to check before c as there is no answer
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: 
                    dp[i].append(comb + [c]) # for each combination array of [i-c] we will add [c] for dp[i]
        return dp[-1]


    def combinationSum_Recursion_noPath(self, candidates, target):       
        def helper(candidates, target):
            if not candidates or target <= 0:
                return []
            res = []
            for i in range(len(candidates)):

                # this line not required as there is no duplicate
                if i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                    continue
                elif candidates[i] == target:
                    res.append([target])
                tmp = helper(candidates[:i+1], target - candidates[i])
                res += [lst+[candidates[i]] for lst in tmp]               
            return res
        
        candidates = sorted(candidates)
        return helper(candidates, target)

    #https://leetcode.com/problems/combination-sum/discuss/170940/python-solution 
    def combinationSum_Recursion_memoization_nosort(self, candidates, target):        
        def helper(candidates, target, j):
            if not candidates or target <= 0:
                return []
            elif (target,j) in dic:
                return dic[(target,j)]
            res = []
            for i in range(len(candidates)):
                # this line not required as there is no duplicate
                if i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                    continue
                elif candidates[i] == target:
                    res.append([target])
                tmp = helper(candidates[:i+1], target - candidates[i], i)
                res += [lst+[candidates[i]] for lst in tmp]
            dic[(target, j)] = res
            return res
        
        dic = {}
        return helper(candidates, target,0)    
    

    def combinationSum_Recursion_memoization(self, candidates, target):        
        def helper(candidates, target, j):
            if not candidates or target <= 0:
                return []
            elif (target,j) in dic:
                return dic[(target,j)]
            res = []
            for i in range(len(candidates)):
                # this line not required as there is no duplicate
                if i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                    continue
                elif candidates[i] == target:
                    res.append([target])
                tmp = helper(candidates[:i+1], target - candidates[i], i)
                res += [lst+[candidates[i]] for lst in tmp]
            dic[(target, j)] = res
            return res
        
        dic = {}
        candidates = sorted(candidates,reverse=True)
        return helper(candidates, target,0)   


      
                
                

    
                    
target=350
candidates=[]
for i in range(30):
    temp=random.randint(1, 200) 
    candidates.append(temp)


a=Solution()


start_time = time.time()
temp1=a.combinationSum_path(candidates,target)
print ("combinationSum_path", time.time() - start_time, "to run")
start_time = time.time()
temp2=a.combinationSum_index(candidates,target)
print ("combinationSum_index", time.time() - start_time, "to run")
start_time = time.time()
temp3=a.combinationSum_DP(candidates,target)
print ("combinationSum_DP", time.time() - start_time, "to run")
start_time = time.time()
temp4=a.combinationSum_Recursion_noPath(candidates,target)
print ("combinationSum_Recursion_noPath", time.time() - start_time, "to run")
start_time = time.time()
temp5=a.combinationSum_Recursion_memoization(candidates,target)
print ("combinationSum_Recursion_memoization", time.time() - start_time, "to run")
start_time = time.time()
temp6=a.combinationSum_Recursion_memoization_nosort(candidates,target)
print ("combinationSum_Recursion_memoization_nosort", time.time() - start_time, "to run")
start_time = time.time()





