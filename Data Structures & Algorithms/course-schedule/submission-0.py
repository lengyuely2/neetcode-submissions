class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)

        visiting =  set()
        def dfs(crs):
            if crs in visiting:
                return False
            if premap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            premap[crs] = []

            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True