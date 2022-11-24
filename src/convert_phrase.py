def convert_phrase(text):
    text = text.replace('ą', '\k{a}')
    text = text.replace('ę', '\k{e}')

    print(text)