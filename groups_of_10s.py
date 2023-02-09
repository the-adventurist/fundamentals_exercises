numbers = [int(x) for x in input().split(', ')]


rotations = max(numbers) / 10
if not rotations.is_integer():
    rotations = int(rotations) + 1
current_group = 10
while rotations:
    fall_in_current_group = []
    for num in numbers:
        if current_group - 10 < num <= current_group:
            fall_in_current_group.append(num)
    print(f"Group of {current_group}'s: {fall_in_current_group}")
    current_group += 10
    rotations -= 1
