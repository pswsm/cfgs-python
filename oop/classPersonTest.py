#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:

    def __init__(self, likes: list, name: str, age: int):
       self.likes = likes
       self.name = name
       self.age = age


pau: Person = Person(likes = ['linux', 'gaming', 'pcmr'], name = 'Pau', age = 18)

print(f'My name is {pau.name}, I am {pau.age} years old and I like:' + ' '.join(pau.likes) + '.')

