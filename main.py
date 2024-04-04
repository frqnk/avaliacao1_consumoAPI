import math, requests

def remove_ad(content):
    content['ad'] = None
    return content

API_URL = 'https://api.isevenapi.xyz/api/iseven/'

print('\nBem-vindo ao verificador de paridade de números naturais até novecentos e noventa e nove mil novecentos e noventa e nove!')

while True:
    if input('\nContinuar? (S/n) ').strip().lower() in ['n', 'nao', 'não']: exit()
    
    user_number_as_str = input('\nDê um número: ')

    try:
        user_number_as_float = float(user_number_as_str.replace(',', '.'))
    except:
        print(f'\"{user_number_as_str}\" não é um número.')
        continue

    if math.ceil(user_number_as_float) - math.floor(user_number_as_float) != 0:
        print('Números não inteiros não possuem paridade.')
        continue

    user_number_as_int = int(user_number_as_float)

    if user_number_as_int < 0:
        print('Números negativos não são suportados no plano gratuito.')

    if user_number_as_int > 999999:
        print('Números maiores que novecentos e noventa e nove mil novecentos e noventa e nove não são suportados no plano gratuito.')

    response = requests.get(API_URL+str(user_number_as_int))

    if response.ok:
        print(f'{user_number_as_str} é um número %s.' % ('ímpar', 'par')[remove_ad(response.json())['iseven']])

    elif response.status_code >= 500:
        print('Problema no servidor. Tente novamente mais tarde.')
