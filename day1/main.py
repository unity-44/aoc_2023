file = open("input.txt")

my_list = []

digit_list = []
result_list = []



words_values = {
    "oneight" : 18,
    "twone" : 21,
    "eightwo" : 82,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}



def wordToValue(string, words_values):
    for word, value in words_values.items():
        string = string.replace(word, str(value))
    return string

for line in file:
    line = line.strip()
    digit_list.append(wordToValue(line, words_values))
    

file.close()

for string in digit_list:
    # Find the first digit in the original loop
    first_digit = next((char for char in string if char.isdigit()), None)

    # Find the last digit in the reversed loop
    reversed_line = string[::-1]
    last_digit = next((char for char in reversed_line if char.isdigit()), None)

    # Combine the first and last digits into a single value
    combined_value = first_digit + last_digit if first_digit and last_digit else None

    result_list.append(combined_value)


int_list = [int(i) for i in result_list if i]

print(int_list)

print(sum(int_list))