import math

def get_player_pos() -> tuple:
    while True:
        try:
            p_text = input("Enter new coordinates as floats "
                           "in format 'x,y,z': ")
            p_list = p_text.split()
            if(len(p_list) != 3):
                raise Exception()
            print(p_list)
            print(float(p_list[0]))
            p_tuple = (float(p_list[0]), float(p_list[1]), float(p_list[2]))
            print(p_tuple)
            return (p_tuple)
        except Exception as e:
            print("Invalid syntax")


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===")
    position = get_player_pos()
    print(position)    