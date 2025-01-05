class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s_arr = [ord(c) - ord('a') for c in s]
        N = len(s)
        changes_pos = [0] * (N + 1)
        changes_neg = [0] * (N + 1)
        for shift in shifts:
            b, e, d = shift
            if d == 0:
                changes_neg[b] += 1
                changes_neg[e + 1] += -1
            else:
                changes_pos[b] += 1
                changes_pos[e + 1] += -1
        diff_pos = 0
        diff_neg = 0
        for i in range(N):
            diff_pos += changes_pos[i]
            diff_neg += changes_neg[i]
            s_arr[i] = (s_arr[i] + diff_pos) % 26
            s_arr[i] = (s_arr[i] - diff_neg) % 26

        return "".join([chr(c + ord('a')) for c in s_arr])
