class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        valid_anagram_dict = {}
        for letters in strs:
            joined_key = "".join(sorted(letters))
            if joined_key not in valid_anagram_dict:
                valid_anagram_dict[joined_key] = [letters]
            else:
                valid_anagram_dict[joined_key].append(letters)
        return list(valid_anagram_dict.values())


        