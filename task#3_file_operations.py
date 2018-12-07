with open('referat.txt', 'r', encoding='utf-8') as file_1:
    content = file_1.read()
    print('Длина получившейся строки равна: ' + str(len(content)))
    print('Количество слов в тексте: ' + str(len(content.split())))
    # Заменяем точки на восклицательные знаки
    edited_content = content.replace('.','!')
    print(edited_content)
with open('referat2.txt','w', encoding='utf-8') as file_2:
    file_2.write(edited_content)