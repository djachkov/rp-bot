class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.abilities = dict(
            strength=5,
            dexterity=5,
            constitution=5,
            intelligence=5,
            wisdom=5,
            charisma=5
        )
        self.level = 1
        self.max_health = (self.abilities['constitution'] * 10) + (self.abilities['strength'] * 3)
        self.health = self.max_health
        self.max_armour = 5
        self.armour = self.max_armour
        self.physical_damage = self.abilities['strength']
        self.skill_points = 6
        self.alive = True
    def levelup(self):
        self.level += 1
        self.max_health = self.max_health + ((self.max_health / 100) * 5)
        self.skill_points += 1
    def improve_ability(self, ability):
        if self.skill_points > 0:
            self.abilities[ability] += 1
            self.skill_points -= 1
            return self.abilities[ability]
        else:
            return "You cannot improve your abilities, {}.".format(self.name)
    def get_damage(self, damage):
        if self.armour > 0:
            if damage > self.armour:
                damage = damage - self.armour
                self.armour = 0
                self.health = self.health - damage
            else:
                self.armour = self.armour - damage
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.loose()
    def loose(self):
        self.alive = False
        return (f"{self.name} is dead!")



