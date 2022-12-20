string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

# 1
print(list(filter(lambda x: x % 17 == 0, range(1, 1000))))

# 2
print(list(filter(lambda x: '2' in str(x), range(1, 1000))))

# 3
print(list(filter(lambda x: str(x) == str(x)[::-1], range(1, 10000))))

# 4
print(string.count(' '))

# 5
print(''.join((list(filter(lambda x: x not in "aeiouyAEIOUY", string.replace(' ', ''))))))

# 6
print(list(filter(lambda x: len(x) <= 5, string.split())))

# 7
print({word: len(word) for word in string.split()})

# 8
print(list(set(filter(lambda x: x.isalpha(), string))))

# 9
print(list(map(lambda x: x**2, [1, 2, 3])))

# 10
print({(x, y): ((0 - x) ** 2 + (0 - y) ** 2) ** 0.5 for x, y in [(1, 1), (2, 3), (5, 3)] if 5 * x - 2 == y})

# 11
print(list(map(lambda x: x ** 2, range(2, 27, 2))))

# 12
print(max([((0 - x) ** 2 + (0 - y) ** 2) ** 0.5 for x, y in [(1, 1), (2, 3), (5, 3)] if x >= 0 and y >= 0]))

# 13
nums_first = [1, 2, 3, 5, 8]
nums_second = [2, 4, 8, 16, 32]
print([(x + y, x - y) for x, y in zip(nums_first, nums_second)])

# 14
lst = ['43141', '32441', '431', '4154', '43121']
print([int(elem) ** 2 for elem in lst if (int(elem) ** 2) % 2 == 0])

# 15
input_str = """name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998"""
keys = [line.split(',')[0] for line in input_str.split()]
other = list(zip(*(line.split(',')[1:] for line in input_str.split())))
print(list(dict(zip(keys, elem)) for elem in other))

# 16
a = [[11.9, 12.2, 12.9],
     [15.3, 15.1, 15.1],
     [16.3, 16.5, 16.5],
     [17.7, 17.5, 18.1]]

result = [sum(row[i] for row in a) for i in range(len(a[0]))]
print(result)
