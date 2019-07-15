x = set('A Python Tutorial')
print(x)
print(type(x))
x = set(['Perl', 'Python', 'Java'])
print(x)
cities = set(('Paris', 'Lyon', 'London', 'Berlin', 'Paris', 'Birmingham'))
print(cities)
# cities=set(('Python','Perl'),('Paris','Berlin','London'))
print(cities)
cities = set(['Frankfurt', 'Basel', 'Freiburg'])
print(cities)
cities.add('Strasbourg')
print(cities)
cities = set(['Frankfurt', 'Basel', 'Freiburg'])
cities = frozenset(['Frankfurt', 'Basel', 'Freiburg'])
# cities.add('Strasbourg')
print(cities)
adjectives = {'cheap', 'expensive', 'inexpensive', 'economical'}
print(adjectives)
more_cities = {'Delhi', 'Mumbai', 'Mandsour'}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)

x = {'a', 'b', 'c', 'd', 'e'}
y = {'b', 'c'}
z = {'c', 'd'}
print(x.difference(y))
print(x.difference(y).difference(z))
print(x - y)
print(x - y - z)
x = {'a', 'b', 'c', 'd', 'e'}
y = {'b', 'c'}
x.difference_update(y)
print(x)
x = {'a', 'b', 'c', 'd', 'e'}
y = {'b', 'c'}
x = x - y
print(x)
x = {'a', 'b', 'c', 'd', 'e'}
x.discard('a')
print(x)
x.discard('z')
print(x)
x = {'a', 'b', 'c', 'd', 'e'}
x.remove('a')
print(x)
x = {'a', 'b', 'c', 'd', 'e'}
# x.remove('f')
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd', 'e', 'f', 'g'}
print(x.intersection(y))
print(x & y)
z = {'p', 'q'}
print(x.isdisjoint('z'))
print(x.isdisjoint('y'))
print(x.isdisjoint(y))
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd'}
print(x.issubset(y))
print(y.issubset(x))
print(x < y)
print(y < x)

print(x < x)
print(x <= x)
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd'}
print(x.issuperset(y))
print(x > y)
print(x >= y)
print(x >= x)
print(x > x)
print(x.issuperset(x))
x = {'a', 'b', 'c', 'd', 'e'}
print(x.pop())
print(x.pop())
y = {}
print(y.pop())
