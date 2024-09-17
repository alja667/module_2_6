n = (int(input('Введите число от 3 до 20:__')))
numbers = []

for i in range(1, n):
    for j in range(1, 20):
        if i >= j:
            continue
        if n % (i + j) == 0:
            numbers += str(i)+str(j)

        else:
            continue

print(f'Возможный вариант пароля: ')
print (*numbers)
