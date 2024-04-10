from typing import List
class Solution:

    def __init__(self) -> None:
        self.operators = "+-*/"

    def isOperand(self, char):
        return char in self.operators

    def evaluate(self, right, left, operator):

        if operator == "+":
            return int(left + right)
        elif operator == "-":
            return int(left - right)
        elif operator == "*":
            return int(left * right)
        elif operator == "/":
            return int(left / right)

        return -1

    def evalRPN(self, tokens: List[str]) -> int:
        # ["2","1","+","3","*"]
        my_stack = []
        operator = ""
        if len(tokens) == 1:
            return int(tokens[0])
        for item in tokens:

            if not self.isOperand(item):
                # item is number
                my_stack.append(item)
            else:
                # the item is operand
                operator = item

                right = int(my_stack.pop())
                left = int(my_stack.pop())

                my_stack.append(self.evaluate(right, left, operator))
                
        return my_stack[0]
    