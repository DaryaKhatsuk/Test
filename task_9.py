# Анаграммами называются слова, образованные путем взаимной перестановки букв.
# В английском языке, например, анаграммами являются слова «live» и «evil»,
# а в русском – «выбор» и «обрыв». Напишите программу, которая будет запрашивать
# у пользователя два слова, определять, являются ли они анаграммами, и выводить на экран ответ.
def funct(word1, word2):
    if sorted(word1) == sorted(word2):
        return 'This is anagram'
    else:
        return 'This is not anagram'


print(funct(input('word 1: '), input('word 2: ')))