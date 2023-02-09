number_of_rooms = int(input())
exceed_chairs = 0

insufficient_chairs = False
for room in range(1, number_of_rooms + 1):
    room_details = input().split()
    chairs = len(room_details[0])
    people = int(room_details[1])
    if chairs > people:
        exceed_chairs += chairs - people
    if chairs < people:
        print(f'{people - chairs} more chairs needed in room {room}')
        insufficient_chairs = True
if not insufficient_chairs:
    print(f'Game On, {exceed_chairs} free chairs left')
