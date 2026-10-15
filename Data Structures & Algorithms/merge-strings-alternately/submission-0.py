class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        it1, it2 = 0, 0
        while it1 < len(word1) or it2 < len(word2):
            if it1 >= len(word1):
                lst.append(word2[it2:])
                break
            elif it2 >= len(word2):
                lst.append(word1[it1:])
                break
            elif it1 == it2:
                lst.append(word1[it1])
                it1 += 1
            elif it1 > it2:
                lst.append(word2[it2])
                it2 += 1
        return ''.join(lst)
        
        