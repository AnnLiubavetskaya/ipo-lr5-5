strochka = input("Введите вашу строку: ")
all_sgls = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м","н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
index = []
for i in strochka.lower() :
    for i in range(len(strochka)):
        if strochka[i] in all_sgls:
            index.append(i)

print("Индексы согласных букв:", index)