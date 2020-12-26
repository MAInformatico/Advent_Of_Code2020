def getHandshake(card_public_key, door_public_key):
    u = pow(7, 20201225, 20201227)
    x = card_public_key
    iterator = 1
    while x != 7:
        x = (x * u) % 20201227
        iterator += 1

    print(pow(door_public_key, iterator, 20201227))


getHandshake(6270530, 14540258)
