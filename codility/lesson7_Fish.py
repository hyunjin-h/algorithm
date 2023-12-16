def solution(A, B):
    down_stacks = []
    pass_cnt = 0
    for a, b in zip(A, B):
        if b == 1:
            down_stacks.append(a)
        else:
            while len(down_stacks) != 0:
                if down_stacks[-1] < a:
                    down_stacks.pop()
                else:
                    break
            else:
                pass_cnt+=1
    return pass_cnt + len(down_stacks)
