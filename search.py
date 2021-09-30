import requests

cep = input('Digite o CEP: ')
print('----------------------')
r = requests.get('https://brasilapi.com.br/api/cep/v1/{}'.format(cep))

data = r.json()

print('Dados abaixo:')
print()
print('CEP: {}'.format(data['cep']))
print('Logradouro: {}'.format(data['street']))
print('Bairro: {}'.format(data['neighborhood']))
print('Cidade: {}'.format(data['city']))
print('Estado: {}'.format(data['state']))