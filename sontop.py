"""
25.03.2021

"Son topish o'yini"

Muallif Sh. Sayfitdinov
"""
import random
print("\nSalom keling son topish o'yinini o'ynaymiz!!!")

def sontop(x = 10): #Kompyuter o'ylagan sonni topish
    pc_son = random.randint(1, x)
    taxminlar = 0
    print(f"\n1 dan {x} gacha bo'lgan oraliqda son o'yladim topa olasizmi?")

    while True:
        taxminlar += 1
        taxmin = int(input(">>"))
        if taxmin == pc_son:
            print(f"\nTOPDINGIZ! Men o'ylagan son {pc_son} edi.\nSiz {taxminlar} ta taxmin bilan topdingiz.")
            break
        elif taxmin > pc_son:
            print("\nXato! Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            print("\nXato! Men o'ylagan son bundan kattaroq. Yana harakat qiling:")

    return taxminlar

def sontop_pc(x = 10): #Biz o'ylagan sonni kompyuter topish
    taxminlar_pc = 0
    min = 1
    max = x
    print(f"\nEndi 1 dan {x} gacha oraliqda bolgan son o'ylang men topaman!")
    input("\nO'ylagan bo'lsangiz ENTER tugmasini bosing.")

    while True:
        if min > max:
            print("Siz g'irrom o'ynadingiz!")
            taxminlar_pc = 0
            break
        taxminlar_pc += 1
        taxmin = random.randint(min, max)
        javob = input(f"\nSiz {taxmin} sonini o'yladingiz. To'g'ri(t), men o'ylagan son bundan kattaroq(+) yoki kichikroq(-)\n>>").lower()
        if javob == "t":
            print(f"\nTOPDIM! Siz {taxmin} sonini o'ylagan ekansiz.\nMen {taxminlar_pc} ta taxmin bilan topdim")
            break
        elif javob == "+":
            min = taxmin + 1
        else:
            max = taxmin - 1

    return taxminlar_pc

hisob = {"Pc":0, "User":0}

while True:
    n = int(input("\n1 dan nechigacha bo'lgan son o'ylaymiz tanlang: "))
    user = sontop(n)
    pc = sontop_pc(n)
    if pc == 0:
        print("\nNatija : YUTQAZDINGIZ. G'irrom o'yin uchun.")
        hisob["Pc"] += 1
    elif user == pc:
        print(f"\nNatija : DURRANG. Ikkalamiz ham {pc} ta taxmin bilan topdik.")
        hisob["Pc"] += 0.5
        hisob["User"] += 0.5
    elif user > pc:
        print(F"\nNatija : YUTQAZDINGIZ. Men {pc} ta taxmin bilan topdim siz esa {user} ta.")
        hisob["Pc"] += 1
    else:
        print(f"\nNatija : G'ALABA. Siz {user} ta men esa {pc} ta taxmin bilan topdim")
        hisob["User"] += 1
    print(f"\tUmumiy hisob\t***\tSiz {hisob['User']} : {hisob['Pc']} Pc\t***")

    play = int(input("\nKeling yana o'ynab ko'ramizmi? ha(1)/yo'q(0) : "))
    if play == 0:
        break
print("O'yin tugadi! E'tiboringiz uchun rahmat")
