from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict= defaultdict(list)
        def make_dict(query:str):
            q_dict=defaultdict(int)
            for q in query:
                q_dict[q] +=1
            return q_dict
        for s in strs:
            dict_tuple = tuple(sorted(make_dict(s).items()))
            main_dict[dict_tuple].append(s)
        return list(main_dict.values())

        
