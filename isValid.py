


class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        i = 0
        while i < len(s):
            char = s[i]
            if char in "[{(":
                my_stack.append(char)

            if char == "]":
                if my_stack == [] or my_stack[-1] != "[":
                    return False
                else:
                    my_stack.pop()
            if char == ")":
                if my_stack == [] or my_stack[-1] != "(":
                    return False
                else:
                    my_stack.pop()

            if char == "}":
                if my_stack == [] or my_stack[-1] != "{":
                    return False
                else:
                    my_stack.pop()


            i += 1
            
        if my_stack == []:
                return True


print(Solution().isValid("(){}}{"))
