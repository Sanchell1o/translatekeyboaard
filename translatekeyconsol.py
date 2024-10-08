import sys

# Массивы с символами для русской и английской раскладок
ru = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
      'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э',
      'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.',
      'ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
      'Ё', '!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+',
      'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ',
      'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', 'Э',
      'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', ',', ' ']

en = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']',
      'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
      'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/',
      '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
      '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+',
      'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}',
      'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
      'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', ' ']


def translate(text, source_text, target_text):
    translated_text = []
    for char in text:
        if char in source_text:
            index = source_text.index(char)
            translated_text.append(target_text[index])
        else:
            translated_text.append(char)
    return ''.join(translated_text)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Данная программа - консольный исправитель раскладки")
        print("Для использования введите данное:")
        print("translatekeyconsol <опции> текст для исправления раскладки")
        print("Опции:")
        print("-re или --ru_eng - исправление текста, написанного на русской раскладке")
        print("-er или --eng_ru - исправление текста, написанного на английской раскладке")
        sys.exit(1)

    option = sys.argv[1]
    input_text = ' '.join(sys.argv[2:])

    if option in ("--ru_eng", "-re"):
        print(translate(input_text, ru, en))
    elif option in ("--eng_ru", "-er"):
        print(translate(input_text, en, ru))
    else:
        print(f"Ошибка. Неизвестный параметр '{option}'")
        print("Использование:")
        print("pycl <опции> текст для исправления раскладки")
        print("Опции:")
        print("-re или --ru_eng - исправление текста, написанного на русской раскладке")
        print("-er или --eng_ru - исправление текста, написанного на английской раскладке")
        sys.exit(1)
