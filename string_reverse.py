# String reversal script for coding challenge due 7-22

def main():
    input_string = input("Please enter a string to be reversed\n ->")
    length = len(input_string)
    i = 0
    while i < length:
        last_letter = input_string[length-1]
        input_string = input_string[:i] + last_letter + input_string[i:length-1]
        print(input_string)
        i += 1
    print(input_string)

if __name__ == '__main__':
    main()
