class Weapon():
    def __init__(self,damage,buttet_count):
        self.damage = damage
        self.buttet_count = buttet_count
        
    def attack(self):
        self.buttet_count -=1
        print("发射子弹，攻击力是%d，剩余子弹%d" %(self.damage,self.buttet_count))
