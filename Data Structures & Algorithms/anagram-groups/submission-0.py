class Solution:
    def calculate_string(self, s: str):
        buckets = [0 for _ in range(26)]
        for letter in s:
            buckets[ord(letter) - ord('a')] += 1
        return tuple(buckets)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = dict()
        for s in strs:
            bucket_tuple = self.calculate_string(s)
            if bucket_tuple in hm.keys():
                hm[bucket_tuple].append(s)
            else:
                hm[bucket_tuple] = [s]
        return list(hm.values())