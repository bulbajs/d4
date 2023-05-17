from django import template

register = template.Library()


@register.filter()
def censor(text):
    bad_words = ['Vtl', 'китай']
    if type(text) == str:
        for word in text.split():
            if word.lower() in bad_words:
                text = text.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    else:
        raise ValueError('Входные данные не являются строкой!')
    return f'{text}'