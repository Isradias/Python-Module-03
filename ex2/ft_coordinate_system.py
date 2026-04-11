from math import sqrt


def str_to_tuple(p_str_list) -> tuple:
    p_float_list = [0.0] * 3
    i = 0
    while (i < 3):
        try:
            p_float_list[i] = float(p_str_list[i])
            i += 1
        except Exception as e:
            raise Exception(f"Error on parameter '{p_str_list[i]}': {e}")
    p_tuple = (p_float_list[0], p_float_list[1], p_float_list[2])
    return (p_tuple)


def get_player_pos() -> tuple:
    while True:
        try:
            p_str = input("Enter new coordinates as "
                          "floats in format 'x,y,z': ")
            p_str_list = p_str.split(",")
            if len(p_str_list) != 3:
                raise Exception("Invalid syntax")
            p_tuple = str_to_tuple(p_str_list)
            return (p_tuple)
        except Exception as e:
            print(e)


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===")
    pos_1 = get_player_pos()
    print(f"Got a first tuple: {pos_1}")
    x1 = pos_1[0]
    y1 = pos_1[1]
    z1 = pos_1[2]
    distance_center = round(sqrt((0 - x1)**2 + (0 - y1)**2 + (0 - z1)**2), 4)
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {distance_center}\n")

    print("Get a second set of coordinates")
    pos_2 = get_player_pos()
    x2 = pos_2[0]
    y2 = pos_2[1]
    z2 = pos_2[2]
    distance_pos2 = round(sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_pos2}")
