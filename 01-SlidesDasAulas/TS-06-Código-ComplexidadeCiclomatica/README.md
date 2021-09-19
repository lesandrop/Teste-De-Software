python -m unittest testaFoo.py -v

## Para análises de cobertura de comandos

> coverage run -m unittest testaFoo
> coverage report -m

## Para análises de cobertura de branch

> coverage run --branch -m unittest testaFoo
> coverage report -m
