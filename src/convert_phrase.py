def convert_phrase(text):
    text = text.replace('ą', '\k{a}')
    text = text.replace('ć', "\\'c")
    text = text.replace('ę', '\\k{e}')
    text = text.replace('ł', '\l{}')
    text = text.replace('ń', "\\'n")
    text = text.replace('ó', "\\'o")
    text = text.replace('ś', "\\'s")
    text = text.replace('ż', '\.z')
    text = text.replace('ź', "\\'z")

    text = text.replace('Ą', '\k{A}')
    text = text.replace('Ć', 's')
    text = text.replace('Ę', '\k{E}')
    text = text.replace('Ł', '\L{}')
    text = text.replace('Ń', "\\'N")
    text = text.replace('Ó', "\\'O")
    text = text.replace('Ś', "\\'S")
    text = text.replace('Ż', '\.Z')
    text = text.replace('Ź', "\\'Z")

    print(text)

def convert_file():
    pass