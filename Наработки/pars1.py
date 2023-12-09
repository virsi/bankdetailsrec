import re
import os

def parse_text_file(filename):
    key_words = ['ИНН', 'БИК', 'КПП', 'р/с', 'к/с', 'л/с', 'Сч. №']
    result = {}

    with open(filename, 'r') as file:
        content = file.read().replace('\n', '').replace('\r', '')

    for key_word in key_words:
        # Находим все совпадения ключевого слова и ищем значение после пробела
        matches = re.findall(rf'\b{key_word}\s* \s*(\d+)', content)
        #re.split('; |, |\*|\n', content)
        """if key_word == 'ИНН':
            try:
                matches.remove('5032266891')
            except ValueError:
                pass
        if key_word == 'БИК':
            try:
                matches.remove('044525593')
            except ValueError:
                pass
        if key_word == 'КПП':
            try:
                matches.remove('503201001')
            except ValueError:
                pass
        if key_word == 'р/с':
            try:
                matches.remove('40703810302820000018')
            except ValueError:
                pass
        if key_word == 'к/с':
            try:
                matches.remove('30101810200000000593')
            except ValueError:
                pass"""
        
        
        if matches:
            result[key_word] = set(matches)
    


    return result

filename = 'image2text/chek2text.txt'
result = parse_text_file(filename)
print(result)


"""
import re
import os

def parse_text_file(filename):
    key_words = ['ИНН', 'БИК', 'КПП', 'р/с', 'к/с', 'л/с', 'Сч. №']
    result = {}

    with open(filename, 'r') as file:
        content = file.read().replace('\n', '').replace('\r', '')
        splitcont = re.split(' |: |, |\*|\n', content)

    print(splitcont)

    for key_word in key_words:


        # Находим все совпадения ключевого слова и ищем значение после пробела
        #matches = re.findall(rf'\b{key_word}\s* \s*(\d+)', content)
try:
            for i in range(splitcont.count(key_word)):
                result[key_word] = splitcont[splitcont.index(key_word) + 1]
        except ValueError:
            continue
        

    return result

filename = 'image2text/chek2text.txt'
result = parse_text_file(filename)
print(result)

"""
