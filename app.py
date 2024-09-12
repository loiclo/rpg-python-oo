class RPG_GAME:
    def __init__(self, name, health, attack_points, defense_points):
        self.name = name
        self.health = health
        self.attack_points = attack_points
        self.defense_points = defense_points

    def attack(self, other):
        damage_reduction = 1 - (other.defense * 0.003) # 1 point de défense annule 0,3% de dégâts
        damage = max(0, self.attack_points * damage_reduction) # Appliquer la réduction sur les dégâts
        other.health -= damage # Appliquer la réduction sur les dégâts
        print(f"{self.name} attacked {other.name} for {damage} damages !")
        print(f"{other.name} has {other.health} health points left !")
        
    def defense(self, other):
        damage = max(0, other.attack - self.defense_points)
        self.health -= damage
        print(f"{self.name} defended from {other.name} for {damage} damages (test d affichage de la def) !")
        
    def health_point(self, other):
        self.health += 10
        
    def damage(self, other):
        damage = self.attack_points - other.defense



hero = RPG_GAME("Hero", 100, 20, 5)  # 5 points de défense
evil = RPG_GAME("Evil", 100, 15, 8)  # 8 points de défense

hero.attack(evil)  # Le héros attaque le méchant
evil.attack(hero)  # Le méchant attaque le héros
