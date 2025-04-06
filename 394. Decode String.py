class Solution:
    def decodeString(self, s: str) -> str:
        '''
        use stack
        append number into num.
        append opening bracket in stack and ele
        if you find closing bracket. pop till opening brace and multiply with num
        '''
        stack = []
        current_string = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((current_string, num))
                current_string = ""
                num = 0
            elif char == "]":
                last_string, repeat_count = stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                current_string += char

        return current_string
