import re

# Чтение первых 20 строк файла и поиск строк с ключевым словом
# Добавлено из-за неправильного нахождения БИКа
def find_lines_with_keyword_in_first_20_lines(file_path, keyword):
    found_lines = []
    with open(file_path, 'r') as file:
        for _ in range(20):
            line = file.readline()
            if keyword in line:
                found_lines.append(line)
    return found_lines

lines_with_AO = find_lines_with_keyword_in_first_20_lines('image2text/chek2text.txt', 'АО')
lines_with_OOO = find_lines_with_keyword_in_first_20_lines('image2text/chek2text.txt', 'ООО')

#Функция парсинга 
def parse_text_file(filename, lines_with_AO, lines_with_OOO):
    key_words = ['инн', 'бик', 'кпп', "АО", 'ООО', 'р/с', 'к/с', 'л/с', 'сч. №', 'кбк']
    ifnotbik = ["АО", 'ООО']
    result = {}

    with open(filename, 'r') as file:
        content = file.read().replace('\n', ' ').replace('\r', ' ')
        content = content.lower()

    for key_word in key_words:
        # Находим все совпадения ключевого слова и ищем значение после пробела
        #matches = re.findall(rf'\b{key_word}\s*\s*(\d+)', content)
        if key_word == 'бик':
            matches = re.findall(rf'\b{key_word}\s*(?:\||\s)*(\d+)', content)
            if len(matches) == 0:
                for _ in ifnotbik:
                    if _ == 'АО':
                        if len(lines_with_AO) != 0:
                            matches.append(lines_with_AO[0][-10:-1])
                    elif _ == 'ООО':
                        if len(lines_with_OOO) != 0:
                            matches.append(lines_with_OOO[0][-10:-1])
        else:
            matches = re.findall(rf'\b{key_word}\s*(?:\||\s)*(\d+)', content)

        # Удаление реквизитов "Роболатории"
        if key_word == 'инн':
            try:
                matches.remove('5032266891')
            except ValueError:
                pass
        if key_word == 'бик':
            try:
                matches.remove('044525593')
            except ValueError:
                pass
        if key_word == 'кпп':
            try:
                matches.remove('503201001')
            except ValueError:
                pass
        if key_word == 'р/с' or key_word == 'cч. №' or key_word == 'л/с':
            try:
                matches.remove('40703810302820000018')
            except ValueError:
                pass
        if key_word == 'к/с':
            try:
                matches.remove('30101810200000000593')
            except ValueError:
                pass
        
        #добавление всего что нашли в словарь
        if matches:
            result[key_word] = list(set(matches))
    
    # Частичная проверка значений
    for key in result:
        if key == 'инн':
            pass
        elif key == 'бик':
            for elem in range(len(result[key])):
                if len(result[key][elem]) != 9:
                    result[key][elem] = result[key][elem][result[key][elem].index('0'):]


    return result
'''
filename = 'image2text/chek2text.txt'
res = parse_text_file(filename)
print(res)'''








"""
    for key_word in key_words:
        # Находим все совпадения ключевого слова и ищем значение после пробела
        #matches = re.findall(rf'\b{key_word}\s*\s*(\d+)', content)
        if key_word == 'АО':
            print(lines_with_AO)
            matches = []
            if len(lines_with_AO) != 0:
                matches.append(lines_with_AO[0][-10:-1])
        elif key_word == 'ООО':
            print(lines_with_OOO)
            matches = []
            if len(lines_with_OOO) != 0:
                matches.append(lines_with_OOO[0][-10:-1])
        else:
            matches = re.findall(rf'\b{key_word}\s*(?:\||\s)*(\d+)', content)

"""