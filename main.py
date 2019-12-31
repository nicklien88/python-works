import pokemon
charmander = pokemon.Pokemon("Charmander", 20, "Fire", 500, 500, False)
ninetales = pokemon.Pokemon("Ninetales", 50, "Fire", 300, 300, False)
blastoise = pokemon.Pokemon("Blastoise", 70, "Water", 1000, 1000, False)
kyogre = pokemon.Pokemon("Kyogre", 100, "Water", 10000, 10000, False)
sceptile = pokemon.Pokemon("Sceptile", 59, "Grass", 900, 900, False)
bulbasaur = pokemon.Pokemon("Bulbasaur", 25, "Grass", 400, 400, False)

nick = pokemon.Trainer("Nick", [charmander, kyogre, sceptile],
                       {"healing water": 10, "sacred water": 5}, 1)
peter = pokemon.Trainer("Peter", [ninetales, blastoise, bulbasaur],
                        {"healing water": 7, "sacred water": 5}, 2)


kyogre.kncok_out()
nick.attack_other_trainer(peter)

