alien_0 ={'x_position': 0, 'y_position': 25, 'speed': 'slow'}

if alien_0['speed'] == 'slow':
    x_incremento = 1
elif alien_0['speed'] == 'medium':
    x_incremento = 2
else:
    x_incremento = 3

alien_0['x_position'] = alien_0['x_position'] + x_incremento

print(f"La nueva posicion en X es {alien_0['x_position']}")