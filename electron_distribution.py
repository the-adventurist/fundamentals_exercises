total_number_of_electrons = int(input())
electron_shell = []
orbit = 1

while total_number_of_electrons:
    orbit_electron_capacity = 2 * orbit ** 2
    current_orbit_delivery = orbit_electron_capacity
    if total_number_of_electrons < orbit_electron_capacity:
        current_orbit_delivery = total_number_of_electrons
    total_number_of_electrons -= current_orbit_delivery
    electron_shell.append(current_orbit_delivery)
    orbit += 1

print(electron_shell)
