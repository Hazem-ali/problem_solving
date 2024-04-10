from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        res =[]
        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if strs_dict.get(sorted_word, 0):
                strs_dict[sorted_word].append(i)
            else:
                strs_dict[sorted_word] = [i]

        for _, indices_list in strs_dict.items():
            anagram = []
            for index in indices_list:
                anagram.append(strs[index])
            res.append(anagram)
            
        return res