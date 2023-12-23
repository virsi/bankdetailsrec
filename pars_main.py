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

# lines_with_AO = find_lines_with_keyword_in_first_20_lines('image2text/chek2text.txt', 'АО')
# lines_with_OOO = find_lines_with_keyword_in_first_20_lines('image2text/chek2text.txt', 'ООО')

# по умолчанию передавать None
#Функция парсинга 
def parse_text_file(filename, lines_with_AO, lines_with_OOO):
    key_words = ['инн', 'бик', 'кпп', "АО", 'ООО', 'р/с', 'к/с', 'л/с', 'сч. №', 'кбк']
    ifnotbik = ["АО", 'ООО']
    result = {
        'инн': ['0'], 
        'бик': ['0'], 
        'кпп': ['0'],
        'к/с': ['0'],
        'сч. №': ['0']
    }

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
                        if len(lines_with_AO) != 0 and str(lines_with_AO[0])[-10:-1].isdigit():
                            matches.append(lines_with_AO[0][-10:-1])
                    elif _ == 'ООО':
                        if len(lines_with_OOO) != 0 and str(lines_with_AO[0])[-10:-1].isdigit():
                            matches.append(lines_with_OOO[0][-10:-1])
        else:
            matches = re.findall(rf'\b{key_word}\s*(?:\||\s)*(\d+)', content)

        # Реализовать удаление реквизитов второго юр лица
        # Удаление реквизитов "Роболатории"
        if key_word == 'инн':
            try:
                matches.remove('5032225870')
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
                matches.remove('40702810602820000997')
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
        if result[key] != None:
            if key == 'инн':
                for elem in result[key]:
                    if len(elem) != 10 or not str(elem).isdigit():
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'бик':
                for elem in result[key]:
                    if (not str(elem).isdigit()) or str(elem)[0] != '0' or len(elem) != 9:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'кпп':
                for elem in result[key]:
                    if not str(elem).isdigit() or len(elem) != 9:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'р/с':
                for elem in result[key]:
                    if str(elem) == '1' or len(elem) != 20:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'сч. №':
                for elem in result[key]:
                    if str(elem) == '1' or len(elem) != 20:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'л/с':
                for elem in result[key]:
                    if str(elem) == '1' or len(elem) != 20:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)
            if key == 'к/с':
                for elem in result[key]:
                    if not str(elem).isdigit() or len(elem) != 20:
                        try:
                            result[key] = result[key].remove(elem)
                        except ValueError:
                            pass
                    if result[key] != None:
                        result[key] = result[key][0]
                    else:
                        result[key] = str(None)

    return result