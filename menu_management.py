# menu_management.py

def add_menu_item(menu: list, item: str) -> None:
    if item not in menu:
        menu.append(item)
        print(f"{item} added to the menu.")
    else:
        print(f"{item} is already on the menu.")


def remove_menu_item(menu: list, item: str) -> None:
    if item in menu:
        menu.remove(item)
        print(f"{item} removed from the menu.")
    else:
        print(f"{item} not found in the menu.")


def check_menu_item(menu: list, item: str) -> None:
    if item in menu:
        print(f"{item} is available")
    else:
        print(f"{item} is not available")

if __name__ == "__main__":
    initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
    add_item = "Tacos"
    remove_item = "Salad"
    check_item = "Pizza"

    add_menu_item(initial_menu, add_item)
    remove_menu_item(initial_menu, remove_item)
    check_menu_item(initial_menu, check_item)

    print("Updated menu:", initial_menu)
