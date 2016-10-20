import random

class Weapon:
    def __init__(self,name,hp,att):
        self.name = name
        self.hp = hp
        self.att = att
        self.owner = None

    def attack(self,other):
        if not self.hp:
            print('武器已失效')
            self.owner.weapon = None
            other.hp-=self.owner.at
            print('%s用双手攻击%s.'%(self.owner.name,other.name))
        else:
            other.hp-=self.att+self.owner.at
            self.hp-=1
            print('%s使用%s攻击%s.'%(self.owner.name,self.name,other.name))

class Magic:
    def __init__(self,name,mp,att):
        self.name = name
        self.mp = mp
        self.att = att
        self.owner = None

    def attack(self,other):
        if self.owner.mp<self.mp:
            print('%s 没有足够的魔法'%self.owner.name)
        else:
            other.hp-=self.att
            print('%s使用技能%s攻击%s'%(self.owner.name,self.name,other.name))

class Food:
    def __init__(self,hp,mp):
        self.hp = hp
        self.mp = mp

class Hero(object):
    def __init__(self,name,hp,at,mp):
        self.name = name
        self.hp = hp
        self.hp_max = hp
        self.at = at
        self.mp = mp
        self.mp_max = hp
        self.weapon = None
        self.magic = None

    def gainweapon(self,weapon):
        weapon.owner = self
        self.weapon = weapon
        print(self.name+'得到了武器'+weapon.name)

    def gainmagic(self,magic):
        magic.owner = self
        self.magic = magic
        print(self.name+'得到了技能'+magic.name)

    def phy_att(self,other):
        if self.weapon:
            self.weapon.attack(other)
        else:
            other.hp-=self.at
            print('%s用双手攻击%s'%(self.name,other.name))

    def mag_att(self,other):
        if self.magic:
            self.magic.attack(other)

    def attack(self,other):
        if random.randint(0,100)>50:
            self.mag_att(other)
        else:
            self.phy_att(other)
        if other.hp>0:
            other.attack(self)
        else:
            print('%s挂了。。。。'%other.name)

    def supply(self,food):
        self.hp = min(self.hp_max,self.hp+food.hp)
        self.mp = min(self.mp_max,self.mp+food.mp)

if __name__=='__main__':
    jack = Hero('Jack',random.randint(80,150),random.randint(5,15),random.randint(80,150))
    jack.gainweapon(Weapon('金丝大环刀',random.randint(0,10),random.randint(0,10)))
    rose = Hero('Rose',random.randint(80,150),random.randint(5,15),random.randint(80,150))
    rose.gainweapon(Magic('玉女心经',random.randint(0,10),random.randint(0,10)))
    while jack.hp>0 and rose.hp>0:
        jack.attack(rose)
        

