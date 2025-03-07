class Solution:
    def isValid(self, s: str) -> bool:
        recent = []
        for i in s:
            if i == "{":
                recent.append("{")
            elif i == "[":
                recent.append("[")
            elif i == "(":
                recent.append("(")
            elif len(recent) == 0:
                return False
            elif i == "}":
                if recent[-1] == "{":
                    recent.pop(-1)
                else:
                    return False
            elif i == "]":
                if recent[-1] == "[":
                    recent.pop(-1)
                else:
                    return False
            elif i == ")":
                if recent[-1] == "(":
                    recent.pop(-1)
                else:
                    return False
        if len(recent) == 0:
            return True
        return False