
####[Exercício Python #107 - Exercitando módulos em Python](link)
- Data: 09/09/2020
- Feito: Sim 08/09/2020
- Tipo: Exercício
- Aula: 22
- Video: #107
***
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções. 

***
[Solução ex107](link.py)
***
Solução do professor:
    
* Olhar pasta [ex107Professor](ex107Professor) 
***
Dica:
1. Nesta Aula, os diretórios passam a ser vistos como pacotes.
Então é possível importar indicando o nome da pasta principal
e depois o módulo desejado.
1. é possivel importar diretamente, chamando o nome do módulo também.
1. esse método é para evitar conflitos
```python
from ex107Professor import moeda 
# from (nome da pasta sem espaços) import (módulo) 
#ou
#import moeda
```


