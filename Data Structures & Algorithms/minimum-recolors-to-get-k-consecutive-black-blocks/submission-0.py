class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_cnt = 0
        for i in range(0, k):
            if blocks[i] == 'W':
                white_cnt += 1
        min_white_cnt = white_cnt
        left = 0    
        right = k
        while right < len(blocks):
            if blocks[left] == 'W':
                white_cnt -= 1
            if blocks[right] == 'W':
                white_cnt += 1
            min_white_cnt = min(min_white_cnt, white_cnt)
            left += 1
            right += 1
        return min_white_cnt


        