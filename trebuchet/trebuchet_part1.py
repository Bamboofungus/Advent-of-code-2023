def trebuchet(file_path):
    with open(file_path, 'r') as file:
        res = []
        # assume digit guaranteed in each line
        for line in file.readlines():
            first = last = None
            for char in line:
                if char.isdigit():
                    first = char
                    break
            for char in line[::-1]:
                if char.isdigit():
                    last = char
                    break
            res.append(int(first + last))
        return sum(res)
                
                    

if __name__ == "__main__":
    res = trebuchet('trebuchet.txt')
    print(res)
