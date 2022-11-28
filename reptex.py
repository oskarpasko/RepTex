from src.convert_phrase import convert_file, convert_phrase
from src.settings import Colors

print(f'{Colors.YELLOW}Welcome in RepTeX!{Colors.END}')
print(f'{Colors.CYAN}1. Simple phrase')
print("2. File's Convert")
print(f'3. Help{Colors.END}')
choice = input(f"{Colors.GREEN}\nWhich option You'd like to choose: {Colors.END}")

match(choice):

    case '1':
        txt = input('Enter Your phrase: ')
        print(convert_phrase(txt))
    case '2':
        user_file = input("Enter file's name: ")
        convert_file(user_file)
    case '3':
        print (f"""
    {Colors.LIGHT_RED}1. == Simple phrase =={Colors.END}
    {Colors.LIGHT_GREEN}You can convert simple phrase.
    You should enter Your phrase.
    Then You will see converted phrase in console.\n{Colors.END}
    {Colors.LIGHT_RED}2. == File's Convert =={Colors.END}
    {Colors.LIGHT_GREEN}You can convert whole file.
    Paste file .txt in 'input_files' folder.
    Then in app after that You chose 2nd option
    enter Your file's name for example file.txt .
    Later Your converted file will wait in 
    'output_files' folder.{Colors.END}
    """)
    case _:
        print('Wrong choice.')

