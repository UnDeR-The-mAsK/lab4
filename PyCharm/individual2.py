#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == "__main__":
    print("Есть ли среди трёх заданных чисел нечётные?")
    a1 = int(input("Первое число: "))
    a2 = int(input("Второе число: "))
    a3 = int(input("Третье число: "))

    if a1 % 2 == 0 or a2 % 2 == 0 or a3 % 2 == 0:
        print("Есть")
    else:
        print("Нет")
        exit(1)
