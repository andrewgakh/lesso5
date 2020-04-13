dict_chisla = {}            # Представление числа ПРОСТОЕ ЧИСЛО: КОЛИЧЕСТВО
flag_sost_chisla = False    # Флаг составного числа
prost_chislo = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,	47,	53,	59,	61,	67,	71,	73,	79,	83,	89,
                97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
                439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
                509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
                599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
                661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
                751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827,
                829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
                919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]

# Функция факторизации числа х
def factoriz(x):
    '''
    :param x: Натуральное число х [1:1000]
    :return:  dict_chisla Канонический вид числа
    '''
    global flag_sost_chisla
    global dict_chisla
    global prost_chislo
    ii = 0
    del_tmp = []

    while prost_chislo[ii] <= x:
        if x % prost_chislo[ii] == 0:
            flag_sost_chisla = True
            del_tmp.append(prost_chislo[ii])
            x = int(x / prost_chislo[ii])
            ii = -1
        ii += 1

    if flag_sost_chisla == False:
        dict_chisla[1] = 1
        dict_chisla[x] = 1

    for i in range (len(del_tmp)):
        dict_chisla[del_tmp[i]] = del_tmp.count(del_tmp[i])
    return

# Определение простоты числа
def prostoe_chislo(x):

    '''
    :param x: Исследуемое число
    :return: flag_sost_chisla  False/True - число простое/составное
    '''
    global prost_chislo
    global flag_sost_chisla
    flag_sost_chisla = False
    ii = 0
    i = int(x**0.5)

    while prost_chislo[ii] <= i:
        if x % prost_chislo[ii] == 0:
            flag_sost_chisla = True
            print()
            print('Число ', x, 'составное')
            break
        ii += 1

    if flag_sost_chisla == False:
        print()
        print('Число ', x, 'простое')

    return

# Список простых делителей числа
def delitely_chisla(x):
    '''
    :param x: Исследуемое число
    :return: Простые делители числа
    '''
    global dict_chisla

    factoriz(x)

    list_delitelei = list(dict_chisla.keys())
    return print('Делители числа', x,' :',list_delitelei)

# Наибольший простой делитель числа
def max_delitel_chisla(x):
    '''
    :param x: Исследуемое число
    :return: Наибольший простой делитель числа
    '''
    global dict_chisla

    factoriz(x)

    list_d = list(dict_chisla.keys())
    list_d.sort(key=lambda i: i, reverse=True)
    return print('Наибольший простой делитель числа ', x,' :', list_d[0])

# Kаноническое разложение числа
def kanonich_vid(x):
    '''
    :param x: Исследуемое число
    :return: Kаноническое разложение числа
    '''
    global dict_chisla
    list_chisla = []
    tmp=[]

    factoriz(x)

    list_chisla = list(dict_chisla.items())
    print('Канонический вид числа', x, ':')
    print()
    print(x, '= 1', end='')
    for i in range (len(list_chisla)):
        tmp = list_chisla[i]
        print(' *',tmp[0],'^',tmp[1], end='')
    print()
    return

# Наибольший делитель (не обязательно простой) числа.
def naib_del_chisla(x):
    '''
    :param x: Исследуемое число
    :return: Наибольший простой делитель числа
    '''
    global dict_chisla
    list_chisla = []
    tmp = []
    tmp1=[]
    a = 0

    factoriz(x)

    list_chisla = list(dict_chisla.items())
    for i in range (len(list_chisla)):
        tmp = list_chisla[i]
        a = tmp[0]**tmp[1]
        tmp1.append(a)
    tmp1.sort(key=lambda i: i, reverse=True)
    print('Наибольший делитель числа ', x, ':',tmp1[0])
    return
