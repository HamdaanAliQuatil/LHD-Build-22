flag = "y"
while flag.lower() == "y":
    string = input("Enter string to be reversed: ")
    print(f"The given string after reversing:\n{string[::-1]}\n")
    flag = input("Reverse more strings? (Y/N): ")