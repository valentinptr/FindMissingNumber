def find_missing_numbers(list_input):
    list_output = []

    for i in range(min(list_input), max(list_input) + 1):
        if i not in list_input[:]:
            list_output.append(i)
    return list_output


list_input = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
out = find_missing_numbers(list_input)

print(out)
