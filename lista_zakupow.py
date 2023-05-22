lista_zakupow = {
    'piekarnia' :  ['chleb', 'pączek', 'bułki'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}
x=0

for sklep, rzeczy in lista_zakupow.items():
    print(f'Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {list(map(str.capitalize,rzeczy))}')
    for rzecz in rzeczy:
        x = x + 1

print(f'W sumie kupuję {x} produktów.')