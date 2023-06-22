class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 == 1 or s[0] == '}' or s[0] ==']' or s[0] == ')':
        #     return False
        # mappings = {'{':'}', '[':']', '(':')'}
        # tracker = []
        # for i in range(len(s)):
        #     if s[i] in mappings:
        #         tracker.append(s[i])
        #         print(tracker)
        #     else:
        #         tracker.pop()
        # if tracker:
        #     return True
        # return False 
        # mapping = {'{':'}', '[':']', '(':')'}
        # stack = []     
        # for char in s:
        #     if char in mapping:
        #         if stack:
        #             top_element = stack.pop()
        #         else:
        #             top_element = '#'

        #         if mapping[char] != top_element:
        #             return False
        #     else:
        #         stack.append(char)
        # return not stack
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack or mapping[stack.pop()] != char:
                    return False
        return not stack
