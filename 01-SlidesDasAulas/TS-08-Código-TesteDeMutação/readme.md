## Instalar o MutPy

https://pypi.org/project/MutPy/

> python -m pip install mutpy

## Rodar os casos de testecom mut.py

> mut.py --target Foo --unit-test testaFoo -m


## Implementação e Relatório

1. O arquivo ``Foo.py`` contém a implementação da funcionalidade;
1. O arquivo ``testaFoo.py`` é a primeira versão da suíte de testes;
1. O arquivo ``testaFoo2.py`` é a segunda versão da suíte de testes, gerada após a execução do teste de mutação;
1. O arquivo ``out.txt`` contém o resultado final da execução do teste de mutação.

## Para análises de cobertura de comandos

> coverage run -m unittest testaFoo
> coverage report -m

## Para análises de cobertura de branch

> coverage run --branch -m unittest testaFoo
> coverage report -m
