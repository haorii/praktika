list = []
for x in range(1, 101):
    if x % 15 == 0:
        list.append('FizzBuzz')
    elif x % 3 == 0:
        list.append('Fizz')
    elif x % 5 == 0:
        list.append('Buzz')
    else:
        list.append(x)
    print(list)