import copy
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def canSwitch(w1,w2):
            counter = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    counter += 1
                if counter > 1:
                    return False
            return counter == 1
        
        if endWord not in wordList or beginWord == endWord:
            return 0
        #initiate bfs
        #item: (word,iteration)
        queue = collections.deque()
        queue.append((beginWord,0))
        visited = set([beginWord])
        while queue:
            el = queue.popleft()
            if canSwitch(el[0],endWord):
                return el[1] + 2
            for w in wordList:
                if  w not in visited and canSwitch(el[0],w):
                    new = (w,el[1]+1)
                    visited.add(w)
                    queue.append(new)

        return 0