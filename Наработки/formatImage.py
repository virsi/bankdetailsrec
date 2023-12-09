"""import cv2

# Загружаем цветное изображение
image = cv2.imread('out/out0.jpg')

# Конвертируем изображение в серый
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, black_and_white_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)


# Отображаем изображение
cv2.imshow('Black and White Image', black_and_white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

import cv2
import numpy as np

# Загружаем изображение с таблицей
image = cv2.imread('out/out0.jpg')

# Преобразуем изображение в градации серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применяем фильтр Canny для обнаружения границ
canny_edges = cv2.Canny(gray_image, 300, 400)

# Находим контуры на изображении
contours, _ = cv2.findContours(canny_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Создаем маску изображения, содержащую только внутренние контуры
mask = np.ones(image.shape[:2], dtype="uint8") * 255
cv2.drawContours(mask, contours, -1, 0, 1)

# Применяем маску к изображению, чтобы удалить контуры
result_image = cv2.bitwise_and(image, image, mask=mask)

isWritten = cv2.imwrite('out/isoutIMAGE.jpg', result_image)
########

# Отображаем результат
cv2.imshow('Table without borders', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
file_path = 'example.txt'  # путь к файлу

# Чтение первых 20 строк файла и поиск строк с ключевым словом
def find_lines_with_keyword_in_first_20_lines(file_path, keyword):
    found_lines = []
    with open(file_path, 'r') as file:
        for _ in range(20):
            line = file.readline()
            if keyword in line:
                found_lines.append(line)
    return found_lines

lines_with_AO = find_lines_with_keyword_in_first_20_lines(file_path, 'AO')

for line in lines_with_AO:
    print(line)


"""