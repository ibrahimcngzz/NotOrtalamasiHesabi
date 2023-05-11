# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:01:13 2023

@author: ibrah
"""
notSayisi = int(input("Final harici kaç adet not olduğunu giriniz "))

if notSayisi == 3:
    not1 = int(input("1. Notunuzu giriniz ")) 
    not2 = int(input("2. Notunuzu giriniz "))
    not3 = int(input("3. Notunuzu giriniz "))
    final = int(input("Final notunuzu giriniz "))
    oran1 = int(input("1. Notunuzun oranını % olarak giriniz "))
    oran2 = int(input("2. Notunuzun oranını % olarak giriniz "))
    oran3 = int(input("3. Notunuzun oranını % olarak giriniz "))
    finalOran = 100 - oran1 - oran2 - oran3
    ortalama = (not1 * oran1/100)+(not2 * oran2/100)+(not3*oran3/100)+(final* finalOran/100)
    if ortalama >= 0 and ortalama < 50:
        print(f"Ortalamanız: {ortalama} ile kaldınız\nHarf notunuz: FF ")
    elif ortalama >= 50 and ortalama <= 57:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DD ")
    elif ortalama >= 58 and ortalama <= 64:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DC ")
    elif ortalama >= 65 and ortalama <= 74:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CC ")        
    elif ortalama >= 75 and ortalama <= 79:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CB ")        
    elif ortalama >= 80 and ortalama <= 84:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BB ")        
    elif ortalama >= 85 and ortalama <= 89:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BA ")        
    elif ortalama >= 90 and ortalama <= 100:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: AA ")        
    else:
        print("Hatalı giriş yaptınız")
elif notSayisi == 2:
    not1 = int(input("1. Notunuzu giriniz ")) 
    not2 = int(input("2. Notunuzu giriniz "))
    final = int(input("Final notunuzu giriniz "))
    oran1 = int(input("1. Notunuzun oranını % olarak giriniz "))
    oran2 = int(input("2. Notunuzun oranını % olarak giriniz "))
    finalOran = 100 - oran1 - oran2
    ortalama = (not1 * oran1/100)+(not2 * oran2/100)+(final* finalOran/100)
    if ortalama >= 0 and ortalama < 50:
        print(f"Ortalamanız {ortalama} ile geçtiniz\nHarf notunuz: FF ")
    elif ortalama >= 50 and ortalama <= 57:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DD ")
    elif ortalama >= 58 and ortalama <= 64:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DC ")
    elif ortalama >= 65 and ortalama <= 74:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CC ")        
    elif ortalama >= 75 and ortalama <= 79:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CB ")        
    elif ortalama >= 80 and ortalama <= 84:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BB ")        
    elif ortalama >= 85 and ortalama <= 89:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BA ")        
    elif ortalama >= 90 and ortalama <= 100:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: AA ")        
    else:
        print("Hatalı giriş yaptınız")
elif notSayisi == 1:
    not1 = int(input("1. Notunuzu giriniz ")) 
    final = int(input("Final notunuzu giriniz "))
    oran1 = int(input("1. Notunuzun oranını % olarak giriniz "))
    finalOran = 100 - oran1
    ortalama = (not1 * oran1/100)+(final* finalOran/100)
    if ortalama >= 0 and ortalama < 50:
        print(f"Ortalamanız: {ortalama} ile kaldınız\nHarf notunuz: FF ")
    elif ortalama >= 50 and ortalama <= 57:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DD ")
    elif ortalama >= 58 and ortalama <= 64:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DC ")
    elif ortalama >= 65 and ortalama <= 74:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CC ")        
    elif ortalama >= 75 and ortalama <= 79:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CB ")        
    elif ortalama >= 80 and ortalama <= 84:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BB ")        
    elif ortalama >= 85 and ortalama <= 89:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BA ")        
    elif ortalama >= 90 and ortalama <= 100:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: AA ")        
    else:
        print("Hatalı giriş yaptınız")
elif notSayisi == 0:
    final = int(input("Final notunuzu giriniz "))
    ortalama = final
    if ortalama >= 0 and ortalama < 50:
        print(f"Ortalamanız: {ortalama} ile kaldınız\nHarf notunuz: FF ")
    elif ortalama >= 50 and ortalama <= 57:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DD ")
    elif ortalama >= 58 and ortalama <= 64:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: DC ")
    elif ortalama >= 65 and ortalama <= 74:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CC ")        
    elif ortalama >= 75 and ortalama <= 79:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: CB ")        
    elif ortalama >= 80 and ortalama <= 84:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BB ")        
    elif ortalama >= 85 and ortalama <= 89:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: BA ")        
    elif ortalama >= 90 and ortalama <= 100:
        print(f"Ortalamanız: {ortalama}, geçtiniz\nHarf notunuz: AA ")        
    else:
        print("Hatalı giriş yaptınız")
else:
    print("Hatalı giriş yaptınız")
















