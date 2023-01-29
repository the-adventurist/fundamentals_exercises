result = 'Draw!'
first_won = False
second_won = False
list_1_horizontal = input().split()
list_2_horizontal = input().split()
list_3_horizontal = input().split()
common_list = list_1_horizontal + list_2_horizontal + list_3_horizontal
common_list += list_1_horizontal[0], list_2_horizontal[0], list_3_horizontal[0]
common_list += list_1_horizontal[1], list_2_horizontal[1], list_3_horizontal[1]
common_list += list_1_horizontal[2], list_2_horizontal[2], list_3_horizontal[2]
common_list += list_1_horizontal[0], list_2_horizontal[1], list_3_horizontal[2]
common_list += list_1_horizontal[2], list_2_horizontal[1], list_3_horizontal[0]
final_list = []
while common_list:
    current_triple = ''
    current_element = ''
    for i in range(3):
        current_element = common_list.pop(0)
        current_triple += current_element
    final_list.append(current_triple)

if '111' in final_list:
    print('First player won')
elif '222' in final_list:
    print('Second player won')
else:
    print(result)
