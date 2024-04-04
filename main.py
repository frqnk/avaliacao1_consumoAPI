import math, requests

class IsEven_API:
    URL = 'https://api.isevenapi.xyz/api/iseven/'
    tiers = {
        'public': {
            'range': range(1+999999),
            'advertisements': True,
            'negative_numbers': False,
            '24_7_support': False,
        },
        'premium': {
            'range': range(1+999999999),
            'advertisements': False,
            'negative_numbers': False,
            '24_7_support': False,
        },
        'enterprise': {
            'range': range(1+999999999999),
            'advertisements': False,
            'negative_numbers': True,
            '24_7_support': True,
        },
    }

    def __init__(self, tier = 'public'):
        self.tier = self.tiers[tier]

    def request(self, number):
        return requests.get(self.URL+str(number))

class User_number:
    parity = None

    def __init__(self):
        self.input = input('\nDê um número: ')

        try:
            self.as_float = float(self.input.replace(',', '.'))

            if math.ceil(self.as_float) - math.floor(self.as_float) == 0:
                self.as_int = int(self.as_float)
            else:
                self.as_int = None

        except:
            self.as_float = None
            self.as_int = None

    def is_not_a_number(self):
        if self.as_float is None:
            return True
        else:
            return False

    def is_not_a_whole_number(self):
        if self.as_int is None:
            return True
        else:
            return False

    def is_a_negative_number(self):
        if self.as_int < 0:
            return True
        else:
            return False

def remove_ad(content):
    content['ad'] = None
    return content

API = IsEven_API()

print(f'\nBem-vindo ao verificador de paridade de números entre {API.tier["range"][0]} e {API.tier["range"][-1]}.')

while True:
    user_number = User_number()

    try:
        response = API.request(user_number.as_int)

        response.raise_for_status()

        if API.tier['advertisements']:
            user_number.parity = ('ímpar', 'par')[remove_ad(response.json())['iseven']]
        else:
            user_number.parity = ('ímpar', 'par')[response.json()['iseven']]

        print(f'{user_number.input} é um número {user_number.parity}.')

    except:
        if user_number.is_not_a_number():
            print(f'"{user_number.input}" não é um número válido.')

        elif user_number.is_not_a_whole_number():
            print('Números não inteiros não possuem paridade.')

        elif user_number.is_a_negative_number() and API.tier['negative_numbers'] == False: 
            print('Números negativos não são suportados pelo plano atual. Considere migrar de plano para melhor atender às suas necessidades.')

        elif user_number.as_int not in API.tier['range']:
            print(f'{user_number.input} não está no intervalo de {API.tier["range"][0]} a {API.tier["range"][-1]} do plano atual. Considere migrar de plano para melhor atender às suas necessidades.')

        elif response.status_code in range(400, 500):
            print('Algo deu errado e a culpa é minha. Lamento.')

        elif response.status_code in range(500, 600):
            print('Problema no servidor. Tente novamente mais tarde.')

        else:
            print('Algo dentre muitas coisas que podiam dar errado deu errado. Tente novamente. Se continuar dando errado, encontre o problema e o corrija antes de tentar novamente. Boa sorte.')

    if input('\nContinuar? (S/n) ').strip().lower() in {'n', 'nao', 'não'}: exit()
