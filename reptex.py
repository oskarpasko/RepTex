from src.convert_phrase import convert_file, convert_phrase

print('Welcome in RepTeX!')

print('1. Simple phrase')
print("2. File's Convert")
choice = input("\nWhich option You'd like to choose?")

match(choice):

    case '1':
        txt = input('Enter Your phrase: ')
        convert_phrase(txt)
    case '2':
        user_file = input("Enter file's name: ")
        convert_file(user_file)
    case _:
        print('Wrong choice.')