schedule = input().split(', ')

changes = input()
while changes != 'course start':
    changes_args = changes.split(':')
    change = changes_args[0]
    lesson = changes_args[1]
    if change == 'Add':
        if lesson not in schedule:
            schedule.append(lesson)
    elif change == 'Insert':
        if lesson not in schedule:
            place = int(changes_args[2])
            schedule.insert(place, lesson)
    elif change == 'Remove':
        if lesson in schedule:
            place_lesson = schedule.index(lesson)
            if 'Exercise' in schedule[place_lesson + 1]:
                schedule.pop(place_lesson + 1)
            schedule.remove(lesson)
    elif change == 'Swap':
        lesson_2 = changes_args[2]
        if lesson in schedule and lesson_2 in schedule:
            place_lesson = schedule.index(lesson)
            place_lesson_2 = schedule.index(lesson_2)
            found_exercises = []
            if 'Exercise' in schedule[place_lesson + 1]:
                found_exercises.append(1)
            if place_lesson_2 < len(schedule) - 1:
                if 'Exercise' in schedule[place_lesson_2 + 1]:
                    found_exercises.append(2)
            if not found_exercises:
                schedule[place_lesson], schedule[place_lesson_2] = schedule[place_lesson_2], schedule[place_lesson]
            elif 1 in found_exercises and 2 not in found_exercises:
                pack_lesson_exercise = schedule[place_lesson] + ':' + schedule[place_lesson + 1]
                schedule.insert(place_lesson, pack_lesson_exercise)
                schedule.pop(place_lesson + 1)
                schedule.pop(place_lesson + 1)
                schedule[place_lesson], schedule[place_lesson_2 - 1] = schedule[place_lesson_2 - 1], schedule[place_lesson]
                this_lesson, this_exercise = schedule[place_lesson_2 - 1].split(':')
                schedule.pop(place_lesson_2 - 1)
                schedule.insert(place_lesson_2 - 1, this_exercise)
                schedule.insert(place_lesson_2 - 1, this_lesson)
            elif 2 in found_exercises and 1 not in found_exercises:
                pack_lesson_exercise = schedule[place_lesson_2] + ':' + schedule[place_lesson_2 + 1]
                schedule.insert(place_lesson_2, pack_lesson_exercise)
                schedule.pop(place_lesson_2 + 1)
                schedule.pop(place_lesson_2 + 1)
                schedule[place_lesson], schedule[place_lesson_2] = schedule[place_lesson_2], schedule[place_lesson]
                this_lesson, this_exercise = schedule[place_lesson].split(':')
                schedule.pop(place_lesson)
                schedule.insert(place_lesson, this_exercise)
                schedule.insert(place_lesson, this_lesson)
            elif 1 in found_exercises and 2 in found_exercises:
                schedule[place_lesson], schedule[place_lesson + 1], schedule[place_lesson_2], schedule[place_lesson_2 + 1] =\
                schedule[place_lesson_2], schedule[place_lesson_2 + 1], schedule[place_lesson], schedule[place_lesson + 1]
    else:
        if lesson in schedule:
            place_lesson = schedule.index(lesson)
            if 'Exercise' not in schedule[place_lesson + 1]:
                schedule.insert(place_lesson + 1, f'{lesson}-Exercise')
        else:
            schedule.append(lesson)
            schedule.append(f'{lesson}-Exercise')
    changes = input()

for num in range(1, len(schedule) + 1):
    print(f'{num}.', end='')
    print(schedule[num - 1])
