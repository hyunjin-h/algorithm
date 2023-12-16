def solution(S):
    reverse_c = {')': '(', ']':'[', '}':'{'}
    stacks = []
    for s in S:
        s_ = reverse_c.get(s, -1)
        if s_ == -1: # open
            stacks.append(s)
        else: # close
            if len(stacks) == 0 or s_ != stacks[-1]:
                return 0
            else:
                stacks.pop(len(stacks)-1)
    return int(len(stacks) == 0)
