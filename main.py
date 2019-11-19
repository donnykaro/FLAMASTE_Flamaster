import sys

max_number_of_cases = 50
max_range = 200

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)

shortcuts = []
for x in range(0, number_of_cases):
    full_word = input()

    if len(full_word) < 1 or len(full_word) > max_range:
        sys.exit(0)

    temp_word = ''
    repeat_counter = 1
    next_ch = ''
    for i, ch in enumerate(full_word):
        try:
            next_ch = full_word[i+1]
        except IndexError:
            next_ch = ''

        if ch != next_ch:
            temp_word += ch

        if ch != next_ch and repeat_counter == 2:
            temp_word += ch
            repeat_counter = 1

        if ch == next_ch and len(temp_word) == 0:
            repeat_counter += 1
        elif ch == next_ch and len(temp_word) != 0 and ch != temp_word[-1]:
            repeat_counter += 1

        if ch != next_ch and repeat_counter > 2:
            temp_word += str(repeat_counter)
            repeat_counter = 1

    shortcuts.append(temp_word)

for s in shortcuts:
    print(s)
