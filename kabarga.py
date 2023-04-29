# -*- coding: utf-8 -*-
#Created on Thu Oct  6 13:59:11 2022
#Математическая программа для решения разных задач из теории чисел

import numpy as np
from sympy.ntheory import factorint
import secrets as s
import random as r

print("                                     .-++=++++:                                           ")
print("    :*#@@%*+=-:.                      .-====+=:                                           ")
print("    ##**##@@@@%@%=:                   .:-====+-                                           ")
print("    .::..-==+#@%@@@*=:                .:--==++-                                           ")
print("     .-:   -+::#@@%#%+..:.           .:-==++++-.                                          ")
print("      :*-.  .:. :#*#%#==**=      ....-==+***##=.                                          ")
print("       .+-.:-=+  .+*#*****=:.     .:-=++#%%%@%*-.                                         ")
print("         :=---*+  :-+#%#%%%#=: :...  ..:-==+###=.                                         ")
print("          .:-=++:.  :-=+*=*%@#*#===::=*++++-:..:.                                         ")
print("             ....=    .=+*#@%%@%%#+++*##%%#*+=-+*+==:.                                    ")
print("               :...     -=%##%%@#**+++**#*==: -**%#==+**+-:                               ")
print("                .     :-====%@@*=-=+=+*+==: +#++#*%*-=#@@%%#+:.                           ")
print("                       .-++**#++--=+++*+-::-:::-*%#%*+==+++++++=-:.                       ")
print("                   .    ..-==+::-:++=*+:::.. :+*#*=. .-==+=++----:.   ..  : .             ")
print("                   -:.    .::.:-=*+*==+-.:... . :  . :-=+***+==-:. .:*#*+=+#@@+           ")
print("                     .=:  .:-:-=+=+-+=:::===-:-====:--++**+#+*+=-.:.-@@@@@#*%%++          ")
print("                      .-:..::---=++=:..::----#=--:--=-=-++*=--::..::=+%%@@@%*=++          ")
print("                       ..: :.::--:::-..-:.:=-=-:.:::-.=-=--:-..      .:*@%#+*+:           ")
print("                        ::...::*+:.-:--:-:--=:-:-.-::-:--::::.. . ..:-+*#@#+.             ")
print("                       .::::.--=:.:::=-==+-+=++====-:--:=--=.: -.:= +%%%+:.               ")
print("                      .-:==--=*--=-===-:-+*+**%###***+*==:-.:... .. :=:.                  ")
print("                     . +*+===+===+==---:=-++*#*:.:==--.:-:.-.:--=:  ::                    ")
print("                     .:*#+++*+*#**++===-==***#%=:=*-.-===*#%@@%@+= .                      ")
print("                     :-+#%##**##*##*=+-=+****###%##%@%@%@@%*=:                            ")
print("                    ::.=*@#@%%#%%%##*=+***#%%@@@@@@@@@%#+:                                ")
print("                    ...=*#%@@%%*=:.:-##*+***++###%%*---:.                                 ")
print("                    ..:==*%@@%%*-    =**#*+*=:--=*===++=-:.. ...                          ")
print("                     .::-*@@%@%%+:   -*#%@@@#--: .:-=+*++=-:..                            ")
print("                     :=-+:*+%@@%+. ..-#@@%@@%+-  .:-+*###+-:.                             ")
print("                      ===:-+%@@%=. .-=#@@@@@#+: -:.=*%@%#*=:.                             ")
print("                    . -.-=*#%%@#%:.+*#@@@@@%*+=:#=-+%@@@%*=-.                             ")
print("                    . .---+%%%@##*#*%@%%%@@%%##+%=+@@@@@@#+:.                             ")
print("                    .::-==++#%###%#%%%%##%%@@%@@%=*@@@@@%*-.                              ")
print("Математическая программа Кабарга (версия 1.2)")
print("Разработчик - И. А. Герасимов")
print("1. Составление таблицы элементов по модулю для нахождения обратного элемента.")
print("2. Решение системы сравнений")
print("3. RSA: Нахождение значений по известным n,e,m")
print("4. RSA: Шифрование сообщения")


lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def Vzaimro_prostie(a, b):
    if(gcd(a, b) == True):
        return ("Числа взаимно простые")
#print(Vzaimro_prostie(9,25))

import math as m
def phi(p,q):
    return m.lcm(p-1,q-1)
    #return(p-1)*(q-1)
 
def getLowLevelPrime(bits):
    while True:
        # Obtain a random number
        pc = s.randbits(bits)
 
         # Test divisibility by pre-generated
         # primes
        for divisor in lowPrimes:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc

def isMillerRabinPassed(mrc):
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = r.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True



def encrypt(e,n,m):
    cipher = ""
    for c in m:
        m = ord(c)
        cipher += str(pow(m,e,n)) + " "
    return cipher

def decrypt(d,n,c):
    m = ""
    parts = c.split()
    for part in parts:
        if(part):
            c = int(part)
            m += chr(pow(c,d,n))
    return m

def generateKeys(keysize):
    e = d = n = 0
    # генерация простых чисел p и q
    p = genLargePrime(keysize)
    q = genLargePrime(keysize)


    n = p * q # Модуль RSA
    phiN = phi(p, q)

    # e взаимно-простое с phiN и 1 < e <= phiN
    while True:
        e = r.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            break
        
    #d = modinv(e, phiN)
    d = pow(e,-1,phiN)
    return e, d, n

def genLargePrime(keysize):

    while True:
        prime_candidate = getLowLevelPrime(keysize)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            return prime_candidate
            break
            

def isCoPrime(p, q):
    """
        возвращает истину если gcd(p, q) = 1
    """
    return gcd(p, q) == 1

def gcd(p, q):
    while q:
        p, q = q, p % q
    return p

choice = int(input("Выбор опции: "))
if(choice == 1):
    """
    Составление таблицы элементов по модулю для нахождения обратного элемента.
    Т.е. n = 5
      1 2 3 4
    1 1 2 3 4
    2 2 4 1 3
    3 3 1 4 2
    4 4 3 2 1

    1^-1 =1 
    2 ^-1 = 3
    3 ^-1 = 2
    4 ^-1 = 4

    """    
    num = int(input("n: "))
    A = np.array([[0] * num] * num)
    for i in range(1,num):
        for j in range(1,num):
             A[i][j] = (i * j % num)
             
    for i in range(1,num):
        for j in range(1,num):
             A[i][j] = (i * j % num)      
    print(A)
elif(choice == 2):
    print("\nПример системы")
    print("x = 2 mod 5")
    print("x = 3 mod 7")
    print("x = 4 mod 9")
    print("\nРаботает только при 1*х и системе 3 на 3")
    n = 3
    print("\nВведите элементы Ai (Те которые перед nod)")
    A = []
    for i in range(n):
        A.append(int(input(f'a{i+1}: ')))
    print("\nВведите элементы Ni (Те которые после nod)")
    
    N = []
    for i in range(n):
        N.append(int(input(f'N{i+1}: ')))
    
    print(f'x1 = {N[0]}t + {A[0]}')
    print(f't = {N[0]}^-1 mod {N[1]}')
    print(f't = {pow(N[0], -1, N[1])} + {N[1]}k')
    
    print(f'x = {A[0]}+ {N[0]} * ({pow(N[0], -1, N[1])} + {N[1]}k)')
    print('Посчитайте: ')
    print("Пример: 1+2к. Сначала введите 1 потом 2")
    t1 = int(input(": "))
    t2 = int(input("k: "))
    print(f'\nx1 = {t1} + {t2}k')
    print(f'{t1} + {t2}k = {A[2]} mod {N[2]}')
    print(f'k = {N[1]}^-1 mod {N[2]}')
    print(f't = {pow(N[1], -1, N[2])} + {N[2]}t')
    print(f'x = {t1} + {t2}k = {t2}*({pow(N[1], -1, N[2])} + {N[2]}t) + {t1}')
    print('Посчитайте: ')
    t11 = int(input(": "))
    t22 = int(input("k: "))
    print(f'\nx = {t11} mod {t22}')
elif(choice == 3):
    n = int(input("n: "))
    e = int(input("e: "))
    m = int(input("m: "))
    pq = list(factorint(n))
    p,q = pq[0],pq[1]
    phiN = phi(p, q)
    d = pow(e,-1,phiN)
    c = pow(m,e,n)
    m1 = pow(c,d,n)
    print(f'p: {p}, q: {q}, n: {n}, phi(n): {phiN}, d: {d}, c: {c}, m1:{m1}')


elif(choice == 4):
    
    print('\nВыберите длину ключа')
    print('1. 4096 бит')
    print('2. 2048 бит (менее безопасно)')
    print('Или же вы можете сами ввести кол-во бит (2048, 3072, 4096)')
    choice2 = int(input(': '))
    if(choice2 == 1):
        keysize = 4096
    elif(choice2 == 2):
        keysize = 3072
    else:
       keysize = choice2
    print('Генерация ключей. Это может занять какое то время')
    e,d,n = generateKeys(keysize)
    m = str(input("Введите сообщение: "))
    c = encrypt(e, n, m)
    print(f'enc: {c}')
    dec = decrypt(d, n, c)
    print(f'dec: {dec}')
    
else:
    print('exit')
    exit()
    
