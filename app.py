class RPG_GAME:
    def __init__(self, name, health, attack_points, defense_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.defense_points = defense_points

    def attack(self, other):
        damage_reduction = 1 - (other.defense_points * 0.003) # 1 point de défense annule 0,3% de dégâts
        damage = max(0, self.attack_points * damage_reduction) # Appliquer la réduction sur les dégâts
        other.health -= damage # Appliquer la réduction sur les dégâts
        print(f"{self.name} attacked {other.name} for {damage:.0f} damages !")
        print(f"{other.name} has {other.health:.0f} health points left !")
        
    def defense(self, other):
        damage = max(0, other.attack - self.defense_points)
        self.health -= damage
        print(f"{self.name} defended from {other.name} for {damage} damages (test d affichage de la def) !")
        
    def health_point(self, other):
        self.health += 10
        
    def damage(self, other):
        damage = self.attack_points - other.defense

class Dragon(RPG_GAME):
    def __init__(self, name, health, attack_points, defense_points):
        super().__init__(name, health, attack_points, defense_points)
        self.health = 100
        self.attack_points = 10
        self.defense_points = 5
        
        
class Hero(RPG_GAME):
    def __init__(self, name, health, attack_points, defense_points):
        super().__init__(name, health, attack_points, defense_points)
        self.health = 100
        self.attack_points = 15
        self.defense_points = 5
        
class Fight():
    def __init__(self, dragon, hero):
        self.dragon = dragon
        self.hero = hero
        
    def fight(self):
        while self.dragon.health > 0 and self.hero.health > 0:
            self.dragon.attack(self.hero)
            self.hero.attack(self.dragon)
        if self.dragon.health <= 0:
            print("Le dragon est mort !")
        elif self.hero.health <= 0:
            print("Le héros est mort !")

dragon = Dragon("Dragon", 100, 10, 5)
hero = Hero("Héros", 100, 15, 5)
fight = Fight(dragon, hero)
fight.fight()