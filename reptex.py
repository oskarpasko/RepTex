from src.convert_phrase import convert_phrase

print('Welcome in RepTeX!')

print('1. Simple phrase')
print('2. File Convert (soon)')
choice = input("\nWhich option You'd like to choose?")

match(choice):

    case '1':
        txt = input('Enter Your phrase: ')
        convert_phrase(txt)
    case _:
        print('Wrong choice.')

