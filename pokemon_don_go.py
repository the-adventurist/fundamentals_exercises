pokemons = [int(x) for x in input().split()]
dead_pokemons_values = 0
while pokemons:
    index = int(input())
    pokemon_value = None
    if index < 0:
        pokemon_value = pokemons.pop(0)
        dead_pokemons_values += pokemon_value
        copied_pokemon = pokemons[-1]
        pokemons.insert(0, copied_pokemon)
    elif index >= len(pokemons):
        pokemon_value = pokemons.pop()
        dead_pokemons_values += pokemon_value
        copied_pokemon = pokemons[0]
        pokemons.insert(len(pokemons), copied_pokemon)
    else:
        pokemon_value = pokemons.pop(index)
        dead_pokemons_values += pokemon_value
        for current_pokemon in range(len(pokemons)):
            if pokemons[current_pokemon] <= pokemon_value:
                pokemons[current_pokemon] += pokemon_value
            else:
                pokemons[current_pokemon] -= pokemon_value
print(dead_pokemons_values)
