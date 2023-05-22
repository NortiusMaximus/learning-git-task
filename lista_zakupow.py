lista_zakupow = {
    'piekarnia' :  ['chleb', 'pączek', 'bułki'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}

for sklep, rzeczy in lista_zakupow.items():
    print(f'Idę do {sklep.capitalize()}, kupuję tu następujące rzeczy: {list(map(str.capitalize,rzeczy))}')