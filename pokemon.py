class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out

    def lose_health(self, value):
        self.current_health -= value
        if self.current_health <= 0:
            self.knock_out()
        else:
            print("{} now has {} health".format(self.name, self.current_health))

    def gain_health(self, value):
        self.current_health += value
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print("{} now has {} health".format(self.name, self.current_health))

    def knock_out(self):
        self.is_knocked_out = True
        print("{} is knocked out".format(self.name))

    def revive(self):
        self.is_knocked_out = False
        self.current_health = self.max_health
        print("{} is revived".format(self.name))

    def attack(self, pokemon):
        # advantages = "Fire" > "Grass" > "Water" > "Fire"
        if self.is_knocked_out:
            print("Can not attack. " + self.name + " is knocked out now, "
                                                   "please switch your pokemon.")
        elif pokemon.is_knocked_out:
            print("Can not attack. " + pokemon.name + " is knocked out now.")
        else:
            print(self.name, "attacks", pokemon.name)
            # advantage
            if (self.type == "Water" and pokemon.type == "Fire") \
                    or (self.type == "Grass" and pokemon.type == "Water") \
                    or (self.type == "Fire" and pokemon.type == "Grass"):
                print("{} attacks {}: very effective".format(self.type, pokemon.type))
                pokemon.lose_health(self.level * 2)
            # same
            elif (self.type == "Water" and pokemon.type == "Water") or (
                    self.type == "Grass" and pokemon.type == "Grass") or \
                    (self.type == "Fire" and pokemon.type == "Fire"):
                print("{} attacks {}: not very effective".format(self.type,
                                                                 pokemon.type))
                pokemon.lose_health(self.level * 0.5)
            else:
                print("{} attacks {}: not very effective".format(self.type, pokemon.type))
                pokemon.lose_health(self.level * 0.5)


class Trainer:
    def __init__(self, name, pokemons, potions, current_pokemon):
        self.name = name
        self.pokemons = pokemons
        # potions is a list
        self.potions = potions
        # potions is a dict
        self.current_pokemon = current_pokemon
        # currently_active_pokemon is a number

    def use_potion(self, potion_name):
        potion_ability = {"healing water": 10, "sacred water": 50}
        try:
            self.potions[potion_name] -= 1
        except KeyError:
            print("You don't have this potion")
        if self.potions[potion_name] < 0:
            print("run out of " + potion_name)
        else:
            print("Using " + potion_name)
            self.pokemons[self.current_pokemon].gain_health(potion_ability[potion_name])

    def attack_other_trainer(self, other_trainer):
        print(self.name, "attacks", other_trainer.name)
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        self.pokemons[self.current_pokemon].attack(their_pokemon)

    def switch_pokemon(self, index_of_pokemon_list):
        if self.pokemons[index_of_pokemon_list].is_knocked_out:
            print("{} has been knocked out. You can not switch to this pokemon".
                  format(self.pokemons[index_of_pokemon_list].name))
        self.current_pokemon = index_of_pokemon_list
