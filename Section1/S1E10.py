'''Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
- Números
- CEPs
- URLs'''

import re

numeros = 'troquei de celular, agora não possuo mais o número (51)997786198, meu novo é (51)987786199'

print(re.findall('\(\d{2}\)\d{9}', numeros))

ceps = '95630-000, 96213-002, 98730-000'

print(re.findall('\d{5}-\d{3}', ceps))