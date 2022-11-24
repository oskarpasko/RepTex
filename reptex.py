print('Welcome in RepTeX!')

print('1. Simple phrase')
print('2. File Convert (soon)')
choice = input("\nWhich option You'd like to choose?")

def convert_phrase(text):
    text = text.replace('ą', '\k{a}')
    text = text.replace('ę', '\k{e}')

    print(text)

match(choice):

    case '1':
        txt = input('Enter Your phrase: ')
        convert_phrase(txt)
    case _:
        print('Wrong choice.')

