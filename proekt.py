class Product():
    def __init__(self, id, nomi, soni, narxi):
        self.id = id
        self.nomi = nomi
        self.soni = soni
        self.narxi = narxi
    def __str__(self):
        prod = 'name = {:<15} cost = {:<10} count = {}'.format(self.nomi, self.narxi, self.soni)
        return prod
    def summ_cost(self):
        return self.narxi * self.soni

prod = {}
prod[1] = Product(1, 'snickers', 9, 5000)
prod[2] = Product(2, 'kola 0.5', 10, 5000)
prod[3] = Product(3, 'lays chips', 5, 8000)
prod[4] = Product(4, 'baunty', 0, 4000)
prod[5] = Product(5, 'adrenalin rush', 8, 12000)
print(prod[1].summ_cost())

for key in prod:
    print(key," >> ",prod[key])

print("pul kiriting")
print("pul kiritib bo'lib 0 ni bosing")
money = 0

while True:
    pul = int(input('>>>>>>>> '))
    if pul != 0:
        if (pul != 1000) and (pul != 5000) and (pul != 10000):
            print("To'g'ri valyuta kiriting")
            print('summa',money)
        else:
            money+=pul
            print('summa',money)
    else:
        for key in prod:
            print(key," >> ",prod[key])
        id = int(input("Mahsulot raqamini kiriting = "))
        print(prod[id])
        if prod[id].soni < 1:
            print('bu mahsulot tugagan boshqa tanlang')
            continue

        if money < prod[id].narxi:
            print('kiritgan puliz yetmaydi yana kiriting')
            print('summa',money)
            continue
        print('1 ta '+prod[id].nomi+' chiqdi')
        prod[id].soni -=1
        money = money - prod[id].narxi
        if money > 0:
            print('Qaytimizni oling bizga birovni puli kerakmas')
        while money > 0:
            
            if money - 10000 >= 0:
                print(10000)
                money -= 10000
            elif money - 5000 >= 0:
                print(5000)
                money -= 5000
            elif money - 1000 >= 0:
                print(1000)
                money -= 1000
        print('yana nimadir olasizmi?')
        for key in prod:
            print(key," >> ",prod[key])
        