# -*- coding: utf-8 -*-
old_file = 'Arquivo_sujo.txt'

with open(old_file) as f:
    linhas = f.read()
    f.close()

linhas_new = linhas.replace('p', '').replace(' ', '')
print(linhas_new)

new_file = 'Arquivo_limpo.txt'

with open(new_file, 'w') as f:
    f.write(linhas_new)
    f.write('João que fez')
    f.close()

print(new_file)
