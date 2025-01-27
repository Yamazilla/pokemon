import random

class Pokemon:
    def __init__(self, species, level=None, name=None):
        
        self.species = species
        
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = species

        self.attack_power = self.level * 5
        self.hp = self.level * 10

    def __str__(self):
        return "{}({})".format(self.species, self.level)
    
    def attack(self, pokemon):
        pokemon.hp = pokemon.hp - self.attack_power
        print("{} lost {} HP".format(pokemon, self.attack_power))

        if pokemon.hp <= 0:
            print("{} fainted!".format(pokemon))
            return True
        else:
            return False

class ElectricPokemon(Pokemon):
    type = "electric"

    def attack(self, pokemon):
        print("{} used Thunder Shock in {}".format(self, pokemon))
        return super().attack(pokemon)

class FirePokemon(Pokemon):
    type = "fire"

    def attack(self, pokemon):
        print("{} used Flame Thrower in {}".format(self, pokemon))
        return super().attack(pokemon)

class WaterPokemon(Pokemon):
    type = "water"

    def attack(self, pokemon):
        print("{} used Hydro Pump in {}".format(self, pokemon))
        return super().attack(pokemon)

class GrassPokemon(Pokemon):
    type = "grass"

    def attack(self, pokemon):
        print("{} used Vine Whip in {}".format(self, pokemon))
        return super().attack(pokemon)


