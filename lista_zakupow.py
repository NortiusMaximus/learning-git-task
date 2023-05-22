lista_zakupow = {
    'piekarnia' :  ['chleb', 'pączek', 'bułki'],
    'warzywniak' : ['marchew', 'seler', 'rukola']
}

for sklep, rzeczy in lista_zakupow.items():
    print(f'Idę do {sklep}, kupuję tu następujące rzeczy: {rzeczy}')