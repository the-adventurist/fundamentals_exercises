text = [int(j) for j in input().split(", ")]

for i in text:
    if i == 0:
        text.remove(i)
        text.append(i)

print(text)