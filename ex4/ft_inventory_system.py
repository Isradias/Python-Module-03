import sys


def redundancy_validation(item, inventory) -> None:
    for x in inventory:
        if item[0] == x:
            raise Exception(f"Redundant item '{x}' - discarting")


def abundance(inventory) -> tuple:
    try:
        most = list(inventory.keys())[0]
        least = list(inventory.keys())[0]
    except Exception:
        raise Exception
    for item in inventory:
        if inventory[item] > inventory[most]:
            most = item
        if inventory[item] < inventory[least]:
            least = item
    return (most, least)


inventory: dict = {}

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    # if len(sys.argv) == 1:
    for arg in sys.argv[1:]:
        itens = arg.split(":")
        try:
            if len(itens) != 2:
                raise Exception(f"Error - invalid parameter '{arg}'")
            redundancy_validation(itens, inventory)
            try:
                inventory.update({itens[0].strip(): int(itens[1])})
            except Exception as e:
                raise TypeError(f"Quantity error for {itens[0]}: {e}")
        except Exception as e:
            print(e)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    itens_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {itens_quantity}")
    for item in inventory:
        print(f"Item {item} represents "
              f"{round((inventory[item] / itens_quantity) * 100, 1)}%")
    try:
        most, least = abundance(inventory)
        print(f"Item most abundance: {most} with quantity {inventory[most]}")
        print(f"Item least abundance: {least} "
              f"with quantity {inventory[least]}")
    except Exception:
        print("Item most abundance:")
        print("Item least abundance:")
    inventory.update({'magic_item': 1})
    print(f"Updated inventory: {inventory}")
