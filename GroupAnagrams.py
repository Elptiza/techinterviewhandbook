from collections import defaultdict


# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    spr = []
    result = [[]]
    for el_strs in strs:
        spr_an_word = defaultdict(int)
        for el in el_strs:
            spr_an_word[el] += 1

        if len(spr) == 0:
            spr.append(spr_an_word)
            result[0].append(el_strs)
        else:
            print(result)
            for i in range(len(spr)):
                if spr[i] == spr_an_word:
                    result[i].append(el_strs)
                    break
                elif i+1 == len(spr):
                    print(el_strs)
                    print(spr_an_word)
                    spr.append(spr_an_word)
                    result.append([el_strs])
                    break
    return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# strs = [""]
# Output: [[""]]

# strs = ["a"]
# Output: [["a"]]