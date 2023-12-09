
"""
bank_data = {}
with open('chek2text.txt', 'r') as data:
	for line in data:
		if 'ИНН' in line or 'БИК' in line or 'КПП' in line or 'р/с' in line or 'к/с' in line:
			splited_line = line.split()
			if 'ИНН' in line:
				tick_position = splited_line.index('ИНН')
				tick_name = 'ИНН'
				dataaftertick = splited_line[tick_position + 1]
				bank_data[tick_name] = str(dataaftertick)
			if 'БИК' in line:
				tick_position = splited_line.index('БИК')
				tick_name = 'БИК'
				data_position = splited_line[tick_position + 1]
				bank_data[tick_name] = str(dataaftertick)
			if 'КПП' in line:
				tick_position = splited_line.index('КПП')
				tick_name = 'КПП'
				data_position = splited_line[tick_position + 1]
				bank_data[tick_name] = str(dataaftertick)
			if 'р/с' in line:
				tick_position = splited_line.index('р/с')
				tick_name = 'р/с'
				data_position = splited_line[tick_position + 1]
				bank_data[tick_name] = str(dataaftertick)
			if 'к/с' in line:
				tick_position = splited_line.index('к/с')
				tick_name = 'к/с'
				data_position = splited_line[tick_position + 1]
				bank_data[tick_name] = str(dataaftertick)

	print(bank_data)
"""

"""def parse_text_file(filename):
    inn_list = []
    bik_list = []
    kpp_list = []
    rs_list = []
    ks_list = []
    ls_list = []

    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for i in range(len(words)):
                if words[i] == "ИНН":
                    if i+1 < len(words):
                        inn_list.append(words[i+1])
                elif words[i] == "БИК":
                    if i+1 < len(words):
                        bik_list.append(words[i+1])
                elif words[i] == "КПП":
                    if i+1 < len(words):
                        kpp_list.append(words[i+1])
                elif words[i] == "р/с":
                    if i+1 < len(words):
                        rs_list.append(words[i+1])
                elif words[i] == "к/с":
                    if i+1 < len(words):
                        ks_list.append(words[i+1])
                elif words[i] == "л/с":
                    if i+1 < len(words):
                        ls_list.append(words[i+1])

    return {
        "ИНН": inn_list,
        "БИК": bik_list,
        "КПП": kpp_list,
        "р/с": rs_list,
        "к/с": ks_list,
        "л/с": ls_list
    }

# Пример использования
filename = "/Users/EV/Desktop/01_Егор/Код/Python/Проекты/RobolatoriyaScan/chek2text.txt"  # замените на путь к вашему текстовому файлу
result = parse_text_file(filename)
print(result)
"""





'''
import re

text_file = 'chek2text.txt'

key_words = ['ИНН', 'БИК', 'КПП', 'р/с', 'к/с', 'л/с']
result = []

with open(text_file, 'r') as file:
	content = file.read()

for key_word in key_words:
# Находим все совпадения ключевого слова и ищем значение после двоеточия
	matches = re.findall(rf'\b{key_word} \s*\d+', content)

for match in matches:
    # Добавляем в список result ключ:значение
    result.append(f'{key_word}:{match}')

print(result)
'''

"""
import re

def parse_text_file(filename):
    key_words = ['ИНН', 'БИК', 'КПП', 'р/с', 'к/с', 'л/с']
    result = {}

    with open(filename, 'r') as file:
        content = file.read()

    for key_word in key_words:
        # Находим все совпадения ключевого слова и ищем значение после двоеточия
        matches = re.findall(rf'\b{key_word}\s* \s*(\S+)', content)
        
        if matches:
            result[key_word] = matches
    
    return result

# Пример использования
filename = 'chek2text.txt'  # замените на путь к вашему текстовому файлу
result = parse_text_file(filename)
print(result)


"""