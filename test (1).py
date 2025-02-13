class cal(): #annab koodile aru, et tahetakse hakata tegema kalkulaatorit
    def __init__(self,a,b): #loob 2 atribuuti mida tuleb edaspidi kas liita, lahutada, jagada, korrutada, jäägi leidma või ruutjuure leidma.
        self.a = a #esimene atribuut milleks on ''a''
        self.b = b #teine atribuut milleks on ''b''

    def liitmine(self): #lisatakse esimest valiku varianti milleks on liitmine
        return self.a + self.b #näitab programmile kuidas see liitmine käib, objektiga a ja b
    def lahutamine(self): #lisatakse teist valiku varianti milleks on lahutamine
        return self.a - self.b #näitab programmile kuidas see lahutamine käib, objektiga a ja b
    def korrutamine(self): #lisatakse kolmandat valiku varianti milleks on korrutamine
        return self.a * self.b #näitab programmile kuidas see korrutamine käib, objektidega a ja b
    def jagamine(self): #lisatakse neljandat valiku varianti milleks on jagamine
        return self.a / self.b #näitab programmile kuidas see jagamine käib, objektidega a ja b
    def jaak(self): #lisatakse viiendat valiku varianti milleks on jääk
        return self.a % self.b #näitab programmile kuidas see jäägi arvutiamine käib, objektidega a ja b
    def ruutjuur(self): #lisatakse kuuendat valiku varianti milleks on ruutjuur
        return self.a ** self.b #näitab programmile kuidas see ruutjuure arvutamine käib, objektidega a ja b
a = int(input("Sisesta esimene number: ")) #programm palub kasutajal sisestada esimene number
b = int(input("Sisesta teine number: ")) # programm palub kasutajal sisestada teine number

kalk = cal(a,b)                         
while True: #kõik mis selle käsu alla läheb hakkab töötama üheskoos ehk näitab kõik valiku variandid numbritega korraga
    def menu(): #näitab kõik valiku variandid nagu menüüd. Üks teise all
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine. ') #Nummerdab kõik valiku variandid
        print(x) #prindib ''x''
    menu() #menüü ja mis selle all on on menüü sisu
    valik = int(input('Sisesta üks valikutest: ')) #programm küsib kasutajalt sisestada üks valiku variantidest mida ta soovib
    if valik == 1: #nummerdab valikut numbriga 1
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2: #nummerdab valikut numbriga 2
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3: #nummerdab valikut numbriga 3
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4: #nummerdab valikut numbriga 4
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5: #nummerdab valikut numbriga 5
        print("Vastus: ",kalk.jaak())
        break
    elif valik == 6: #nummerdab valikut numbriga 6
        print("Vastus: ",kalk.ruutjuur())
        break
    elif valik == 0: #nummerdab valikut numbriga 7
        print('Sisesta uuesti üks liitmise operaator')
        break




