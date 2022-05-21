import random

move = ((0, 1), (0, -1), (1, 0), (-1, 0))


def generate_game(size=(5,5), snoms=1):
    snom_count=0
    snom_coordinates = []
    stone_coordinates = []
    clear_coordinates = []

    while snom_count < snoms:
        x = random.randint(0, size[0]-1)
        y = random.randint(0, size[0]-1)
        if (x, y) not in snom_coordinates:
            snom_coordinates.append([x, y])

    while true:
        direction = random.randint(0, 3)

        max_steps = {}
        stop = False

        for snom in snom_coordinates:
            for i in range(1, max(size)):
                new_pos = snom + move[direction]*i

                if out_of_bounds(new_pos) or new_pos in stone_coordinates:
                    max_steps[snom] = i
                    break

        for snom in snom_coordinates:
            if max_steps[snom] > 0:
                if random.randint(0, 1):
                    teps
