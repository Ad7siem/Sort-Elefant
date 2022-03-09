import os

# Przypisanie do zmiennej nazwę pliku podanej w konsoli
file = input('Podaj nazwę pliku, który chcesz otworzyć: ')

dane = []

# Pobranie danych z pliku i zapisane ich w liście
if os.path.isfile(f'zadanie_B/{file}'):
    with open(f'zadanie_B/{file}', 'r') as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.replace(' ', ',')
            dane.append(line.split(','))

else:
    print('Plik nie istnieje')

# Zmiana pierwszych dwóch list z string na int
for i in range(0,2):
    for j in range(0, len(dane[i])):
        dane[i][j] = int(dane[i][j])

# Tworzenie listy pomocniczej do sprawdzenia czy słoń był już sprawedzany
proven_elephants = []
for i in range(0, dane[0][0]):
    proven_elephants.append('FALSE')

# Wypisanie w konsoli wartości w zmiennej i liście
# print(proven_elephants, '\n')
# for i in dane:
#     print(i)

# Stworzenie zmiennych pomocniczych i list do wypisanie cykli
position = 0
cycles = []
cycle = []
full = False
elephants_now = dane[2]
elephants_new = dane[3]
value = elephants_now[position]
cycle.append(elephants_now[position])
k = 0

# Tworzenie cykli
while k < dane[0][0]:
    k = 0
    # Tworzenie nowego cyklu
    if full:
        cycle.clear()
        cycle.append(elephants_now[position])
        value = elephants_now[position]
        full = False

    # Przypianie do zmiennej indeksu słonia
    position = elephants_now.index(value)         

    # Zmiana wartości w liście pomocnicznej
    proven_elephants[position] = 'TRUE'

    # Dopisanie do cyklu wartości jeśli się już nie powtórzyła
    if elephants_new[position] != cycle[0]:
        cycle.append(elephants_new[position])
        value = elephants_new[position]
    else:
        for i in proven_elephants:
            if i == 'FALSE':
                position = proven_elephants.index(i)
        cycles.append(cycle[:])
        full = True

    # Sprawdzenie ilości spisanych już liczb
    for i in proven_elephants:
        if i == 'TRUE':
            k += 1


# print(cycles)
# print(proven_elephants)

# Stworzenie listy z wagami słoni
elephant_weight = dane[1]

# Przypisanie do zmiennej najniższej wagi wszystkich słoni
min_weight = min(elephant_weight)
# print(min_weight)

# Stworzenie list cykli z wartościami ciężaru słoni
list_wight_cycles = []
list_wight_cycle = []

for cycle in cycles:
    list_wight_cycle.clear()
    for cyc in cycle:
        list_wight_cycle.append(elephant_weight[int(cyc) - 1])
    list_wight_cycles.append(list_wight_cycle[:])

# print(list_wight_cycles)


sum_all = 0
    
# Obliczenia użycia siły do przesunięcia słoni używając najlepszej metody
for list_wight_cycle in list_wight_cycles:
    min_C = min(list_wight_cycle)
    sum_C = sum(list_wight_cycle)
    C = len(list_wight_cycle)
    # print(min_C)
    # print(sum_C)
    # print(C)
    method_1 = sum_C + (C - 2) * min_C
    method_2 = sum_C + min_C + (C + 1) * min_weight
    if method_1 > method_2:
        min_sum = method_2
    else:
        min_sum = method_1
    # print(method_1)
    # print(method_2)
    # print(min_sum)
    sum_all += min_sum

# print(sum_all)

# Zapisywanie wyniku do plikuo w głównym folderze o nazwie podanej na początku z formatem .out
for i in file:
    if i == '.':
        file = file[:file.index(i)]

with open(f'{file}.out', 'w') as f:
    f.write(str(sum_all))

