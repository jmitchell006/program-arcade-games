#!/usr/bin/env python3
#O's
#Jason Mitchell
#11/16/17

number = int(input("How many o's"))
spaces = (number + 2) - 2

print('o' * ((number) + 2))

for o1 in range(1, number - 1):
    print('o' + (' ' * spaces) + 'o')

print('o' * ((number) * 2))
