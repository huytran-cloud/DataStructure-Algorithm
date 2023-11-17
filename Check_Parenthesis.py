def is_correct(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return 0
            if char == ")" and stack[-1] != "(" or char == "]" and stack[-1] != "[" or char == "}" and stack[-1] != "{":
                return 0
            stack.pop()
    return 1 if len(stack) == 0 else 0


s = input().strip()
print(is_correct(s))
