def findBestRestaurant(restaurant_list, menu_list):
    for i in range(len(menu_list)):
        if "pea soup" in menu_list[i] and "pancakes" in menu_list[i]:
            return restaurant_list[i]
    return "Anywhere is fine I guess"


def main():
    restaurant_list = []
    menu_list = []
    num_restaurants = int(input())
    for _ in range(num_restaurants):
        num_menu_items = int(input())
        restaurant_list.append(input())
        menu = set()
        for _ in range(num_menu_items):
            menu.add(input())
        menu_list.append(menu)
    print(findBestRestaurant(restaurant_list, menu_list))


if __name__ == "__main__":
    main()
