# I myself haven't understood what I did here :D:):D:):D:)
people = [x for x in input().split()]
killed_people = []
k = int(input())
n = 0
while people:
    for to_be_killed in range(len(people)):
        n += 1
        if n == k:
            n = 0
            killed_guy = people.pop(to_be_killed)
            killed_people.append(killed_guy)
            after_killed_guy = people[to_be_killed:]
            before_killed_guy = people[:to_be_killed]
            people = after_killed_guy + before_killed_guy
            break
print(f"[{','.join(killed_people)}]")

