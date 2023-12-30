age = int(input('Qual a sua idade? '))

if age < 16:
    print(f'Com a idade de {age} anos, não pode votar.')
elif (age >= 16 and age <= 17) or age >= 70:
    print(f'Com a idade de {age} pode votar, mas não é obrigatório.')
else:
    print(f'Com a idade de {age} é obrigatório votar.')
