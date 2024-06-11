import time
while True:
    allow = input("Do you to enter a word? ").lower()
    if allow != "yes":
        print("Ok :(")
        break
    else:
        word = input("Enter the word: ").lower()
        splitWord = list(word)
        reversedWord = splitWord[::-1]
        if splitWord == reversedWord:
            print(f"\n{word} IS a palindrome\n")
            time.sleep(2)
        else:
            print(f"\n{word} is NOT a palindrome\n")
            time.sleep(2)