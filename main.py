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

    def supportedRange(self):
        return self.tier['range']

    def minValue(self):
        return self.tier['range'][0]

    def maxValue(self):
        return self.tier['range'][-1]

    def hasAd(self):
        return self.tier['advertisements']

    def allowNegativeNumbers(self):
        return self.tier['negative_numbers']

class User_number:
    parity = None

    def __init__(self, input):
        self.input = input

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

def main():
    user_number = User_number(input('\nDê um número: '))

    try:
        response = API.request(user_number.as_int)

        response.raise_for_status()

        if API.hasAd():
            user_number.parity = ('ímpar', 'par')[remove_ad(response.json())['iseven']]
        else:
            user_number.parity = ('ímpar', 'par')[response.json()['iseven']]

        print(f'{user_number.input} é um número {user_number.parity}.')

    except:
        if user_number.is_not_a_number():
            print(f'"{user_number.input}" não é um número válido.')

        elif user_number.is_not_a_whole_number():
            print('Números não inteiros não possuem paridade.')

        elif user_number.is_a_negative_number() and API.allowNegativeNumbers() == False: 
            print('Números negativos não são suportados pelo plano atual. Considere migrar de plano para melhor atender às suas necessidades.')

        elif user_number.as_int not in API.supportedRange():
            print(f'{user_number.input} não está no intervalo de {API.minValue()} a {API.maxValue()} do plano atual. Considere migrar de plano para melhor atender às suas necessidades.')

        elif response.status_code in range(400, 500):
            print('Algo deu errado e a culpa é minha. Lamento.')

        elif response.status_code in range(500, 600):
            print('Problema no servidor. Tente novamente mais tarde.')

        else:
            print('Algo dentre muitas coisas que podiam dar errado deu errado. Tente novamente. Se continuar dando errado, encontre o problema e o corrija antes de tentar novamente. Boa sorte.')

def askToContinue():
    answer = input('\nContinuar? (S/n) ').strip().lower()

    if answer in {'n', 'no', 'nao', 'não'}:
        exit()
    elif answer in {'', 'y', 'yes', 's', 'sim'}:
        pass
    else:
        askToContinue()

def main_loop():
    main()
    askToContinue()
    main_loop()

def tests():
    pass

API = IsEven_API()

print(f'\nBem-vindo ao verificador de paridade de números entre {API.minValue()} e {API.maxValue()}.')

main_loop()
