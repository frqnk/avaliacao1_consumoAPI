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
        self.supportedRange = self.tier['range']
        self.minValue = self.tier['range'][0]
        self.maxValue = self.tier['range'][-1]
        self.hasAd = self.tier['advertisements']
        self.allowNegativeNumbers = self.tier['negative_numbers']

    def isEven(self, number):
        response = requests.get(self.URL+str(number))
        response.raise_for_status()
        return response.json()['iseven']

class User_number:
    parity = None
    as_float = None
    as_int = None

    def __init__(self, input):
        self.input = input
        try:
            self.as_float = float(self.input.replace(',', '.'))
        except:
            return
        if math.ceil(self.as_float) - math.floor(self.as_float) == 0:
            self.as_int = int(self.as_float)

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

def main():
    user_number = User_number(input('\nDê um número: '))

    try:
        user_number.parity = 'par' if parityChecker.isEven(user_number.as_int) else 'ímpar'
    except:
        if user_number.is_not_a_number():
            print(f'"{user_number.input}" não é um número válido.')
        elif user_number.is_not_a_whole_number():
            print('Números não inteiros não possuem paridade.')
        elif user_number.is_a_negative_number() and not parityChecker.allowNegativeNumbers:
            print('Números negativos não são suportados pelo plano atual. Considere migrar de plano para melhor atender às suas necessidades.')
        elif user_number.as_int not in parityChecker.supportedRange:
            print(f'{user_number.input} não está no intervalo de {parityChecker.minValue} a {parityChecker.maxValue} do plano atual. Considere migrar de plano para melhor atender às suas necessidades.')
        elif response.status_code in range(400, 500):
            print('Algo deu errado e a culpa é minha. Lamento.')
        elif response.status_code in range(500, 600):
            print('Problema no servidor. Tente novamente mais tarde.')
        else:
            print('Algo dentre muitas coisas que podiam dar errado deu errado. Tente novamente. Se continuar dando errado, encontre o problema e o corrija antes de tentar novamente. Boa sorte.')
        return

    print(f'{user_number.input} é um número {user_number.parity}.')

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

parityChecker = IsEven_API()

print(f'\nBem-vindo ao verificador de paridade de números entre {parityChecker.minValue} e {parityChecker.maxValue}.')

main_loop()
