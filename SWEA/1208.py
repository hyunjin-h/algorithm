import sys
sys.stdin = open("input.txt", "r")

for testnum in range(1,11):
    dump=int(input())
    boxes=list(map(int,input().split()))
    for _ in range(dump):
        boxes[boxes.index(max(boxes))]-=1
        boxes[boxes.index(min(boxes))] += 1

    print(f'#{testnum} {max(boxes)-min(boxes)}')