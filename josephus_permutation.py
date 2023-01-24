people = [int(x) for x in input().split()]
k = int(input())
k_progress = k
while people:

    for to_be_killed in people:
        k_progress += 1
        if k_progress % k == 0 and k <= len(people):
            print(to_be_killed)
            break