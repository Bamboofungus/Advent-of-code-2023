DIGITS = {
    'one': '1',
    'two': '2', 
    'three': '3', 
    'four': '4', 
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'
}

def trebuchet(file_path):
    with open(file_path, 'r') as file:
        res = []
        # assume digit guaranteed in each line
        for line in file:
            first = last = None
            for i, char in enumerate(line.rstrip()):
                if i >= 4 and line[i-5:i] in DIGITS.keys():
                    first = DIGITS[line[i-5:i]]
                    break
                elif i >= 3 and line[i-4:i] in DIGITS.keys():
                    first = DIGITS[line[i-4:i]]
                    break
                elif i >= 2 and line[i-3:i] in DIGITS.keys():
                    first = DIGITS[line[i-3:i]]
                    break
                elif char.isdigit():
                    first = char
                    break
            
            for i in range(len(line.rstrip()) - 1, -1, -1):
                char = line[i]
                if i < len(line) - 5 and line[i:i+5] in DIGITS.keys():
                    last = DIGITS[line[i:i+5]]
                    break
                elif i < len(line) - 4 and line[i:i+4] in DIGITS.keys():
                    last = DIGITS[line[i:i+4]]
                    break
                elif i < len(line) - 3 and line[i:i+3] in DIGITS.keys():
                    last = DIGITS[line[i:i+3]]
                    break
                elif char.isdigit():
                    last = char
                    break
            res.append(int(first + last))
        return sum(res)


if __name__ == "__main__":
    res = trebuchet('trebuchet.txt')
    print(res)
