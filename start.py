from main import Kuznechik
from Const import Const
from converter import *

if __name__ == '__main__':
    mode = int(input('Выберите режим работы шифра "Кузнечик":\n'
                     '1) Зашифрование\n'
                     '2) Расшифрование\n'))
    option_1 = int(input('Исходный текст - это:\n'
                              '1) Hex-строка\n'
                              '2) Произвольный текст\n'
                              '3) Текст в base64\n'))
    option_2 = int(input('Новый текст представить в виде:\n'
                           '1) Hex-строка\n'
                           '2) Произвольный текст\n'
                           '3) Текст в base64\n'))
    input_mode = ['', 'hex', 'text', 'base64'][option_1]
    output_mode = ['', 'hex', 'text', 'base64'][option_2]
    new_data = []

    with open('input.txt', 'r', encoding='utf-8') as file_in:
        text = file_in.read()
        new_text = eval(f'({input_mode}_to_hex(text))')
        data = [Const(new_text[i:i + 32]) for i in range(0, len(new_text) - 31, 32)]

    with open('key.txt', 'r', encoding='utf-8') as key_in:
        key = key_in.read()[:64]

    if mode == 1:
        for block in data:
            kuznechik = Kuznechik(key, block)
            new_data.append(kuznechik.encryption())
    else:
        for block in data:
            kuznechik = Kuznechik(key, block)
            new_data.append(kuznechik.decryption())

    with open('output.txt', 'w', encoding='utf-8') as file_out:
        temp = ''.join(map(str, new_data))
        out = eval(f'(hex_to_{output_mode}(temp))')
        file_out.write(out)
