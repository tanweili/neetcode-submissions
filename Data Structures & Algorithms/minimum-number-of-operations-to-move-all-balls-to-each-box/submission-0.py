class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix_sum = [0 for _ in range(len(boxes))]
        suffix_sum = [0 for _ in range(len(boxes))]
        ball_cnt = 0 if boxes[0] == '0' else 1
        for i in range(1, len(boxes)):
            prefix_sum[i] = prefix_sum[i-1] + ball_cnt
            if boxes[i] == '1':
                ball_cnt += 1
        ball_cnt = 0 if boxes[-1] == '0' else 1
        for j in range(len(boxes) - 2, -1, -1):
            suffix_sum[j] = suffix_sum[j+1] + ball_cnt
            if boxes[j] == '1':
                ball_cnt += 1

        output = []
        for i in range(len(prefix_sum)):
            output.append(prefix_sum[i] + suffix_sum[i])
        return output
