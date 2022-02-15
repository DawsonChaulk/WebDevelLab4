def draw(enemies):
    for enemy in enemies:
        if enemy >= 50:
            print("Green")
        elif enemy > 20 and enemy < 50:
            print("Light Red")
        elif enemy <= 20 and enemy > 0:
            print("Flashing Bright Red")
        else:
            print("Terminated")

enemys = [42, 64, 0, 96, 9, 100, 21, 0, 83, 18]

draw(enemys)