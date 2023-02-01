def sign_determiner(this_list):
    result = ''
    count_of_negatives = 0
    for num in this_list:
        if num < 0:
            count_of_negatives += 1
        elif num == 0:
            result = 'zero'
            return result
    if count_of_negatives == 1 or count_of_negatives == 3:
        result = 'negative'
    else:
        result = 'positive'
    return result


current_list = [int(input()), int(input()), int(input())]
print(sign_determiner(current_list))