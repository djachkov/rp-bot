from weapons import weapons
from armors import armors
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
        self.weapon = None
        self.level = 1
        self.max_health = (self.abilities['constitution'] * 10) + (self.abilities['strength'] * 3)
        self.health = self.max_health
        self.max_protection = 5
        self.armor = None
        self.protection = self.max_protection
        self.physical_damage = self.abilities['strength']
        self.skill_points = 6
        self.alive = True
    def equip(self, item):
        if item in weapons:
            return self._equip_weapon(item)
        elif item in armors:
            return self._equip_armor(item)
        else:
            return "Я не могу использовать это"
    def _equip_weapon(self, weapon):
        attack_power = weapons[weapon]
        if not self.weapon:
            self.physical_damage += attack_power
            self.weapon = weapon
            return f'{self.name} equip {weapon}.'
        else:
            dropped = self.weapon
            self.physical_damage = self.abilities['strength'] + attack_power
            self.weapon = weapon
            return f'{self.name} drop {dropped} and equip {weapon}.'
    def _equip_armor(self, armor):
        protection = armors[armor]
        self.max_protection += protection
        self.protection = self.max_protection
        return f'{self.name} equip {armor}.'

    def levelup(self):
        self.level += 1
        self.max_health = self.max_health + ((self.max_health / 100) * 5)
        self.health = self.max_health
        self.skill_points += 1
    def improve_ability(self, ability):
        if self.skill_points > 0:
            self.abilities[ability] += 1
            self.skill_points -= 1
            if ability == 'strength':
                self.physical_damage += 1
            return f"{self.abilities[ability]} increased."
        else:
            return "You cannot improve your abilities, {}.".format(self.name)
    def get_damage(self, damage):
        if self.armor > 0:
            if damage > self.armor:
                damage = damage - self.armor
                self.armor = 0
                self.health = self.health - damage
            else:
                self.armor = self.armor - damage
        else:
            self.health = self.health - damage
        if self.health <= 0:
            self.death()
    def death(self):
        self.alive = False
        return (f"{self.name} is dead!")



