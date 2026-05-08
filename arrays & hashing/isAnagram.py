from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_dict(query:str):
            q_dict = defaultdict(int)
            for q in query:
                q_dict[q] +=1
            return q_dict
        s_dict = make_dict(s)
        t_dict = make_dict(t)
        return s_dict == t_dict

        
