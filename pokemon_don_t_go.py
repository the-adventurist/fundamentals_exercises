def increasing_decreasing_elements(value, pokemons_collection):
    for this_pokemon in range(len(pokemons)):
        if pokemons[this_pokemon] <= pokemon_value:
            pokemons[this_pokemon] += pokemon_value
        else:
            pokemons[this_pokemon] -= pokemon_value


pokemons = [int(x) for x in input().split()]
dead_pokemons_values = 0

while pokemons:
    index = int(input())
    if index < 0:
        pokemon_value = pokemons.pop(0)
        dead_pokemons_values += pokemon_value
        copied_pokemon = pokemons[len(pokemons) - 1]
        pokemons.insert(0, copied_pokemon)
        increasing_decreasing_elements(pokemon_value, pokemons)
    elif index >= len(pokemons):
        pokemon_value = pokemons.pop()
        dead_pokemons_values += pokemon_value
        copied_pokemon = pokemons[0]
        pokemons.append(copied_pokemon)
        increasing_decreasing_elements(pokemon_value, pokemons)
    else:
        pokemon_value = pokemons.pop(index)
        dead_pokemons_values += pokemon_value
        increasing_decreasing_elements(pokemon_value, pokemons)
print(dead_pokemons_values)
