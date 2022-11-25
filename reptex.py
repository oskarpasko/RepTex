from src.convert_phrase import convert_file, convert_phrase, feature_help

print('Welcome in RepTeX!')

print('1. Simple phrase')
print("2. File's Convert")
print('3. Help')
choice = input("\nWhich option You'd like to choose?")

match(choice):

    case '1':
        txt = input('Enter Your phrase: ')
        print(convert_phrase(txt))
    case '2':
        user_file = input("Enter file's name: ")
        convert_file(user_file)
    case '3':
        feature_help()
    case _:
        print('Wrong choice.')