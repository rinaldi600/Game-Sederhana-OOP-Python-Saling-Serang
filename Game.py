class Hero:

    jumlah = 0


    def __init__(self , name , health , attackPower , armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self , hero) :
        print(self.name , " Menyerang " , hero.name ,)
        hero.diserang(self , self.attackPower)

    def diserang(self , lawan , attack_power) :
        print(self.name , " Diserang " , lawan.name)
        attack_diterima = attack_power / self.health
        Hero.jumlah += attack_diterima
        print("Serangan Terasa : " , Hero.jumlah)
        health_diterima = self.health - Hero.jumlah
        if health_diterima == 0 :
            print("Kesehatan Tersisa : " , health_diterima)
            print("Anda Gugur")
        else :
            print("Kesehatan Tersisa : ", health_diterima)
            print("Maju Terosss !!")
        print("======================================")

sniper = Hero("Sniper" , 200 , 1000 , 300)
axe = Hero("Axe" , 100 , 1200 , 320)
rikimaru = Hero("Rikimaru" , 140 , 3200 , 234)
