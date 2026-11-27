programm = int(input("Enter 1 or 2 or 3 or 4 or 5 or 6 : "))
match programm:
    case 1:
        my_list = ["M", 1, "Mahdi", True, 'c', 20, "Ghodsikhah", [1, 2, 3]]
        print(my_list[1:4])
    case 2:
        brands = ["Nike", "Adidas", "Puma", "Apple", "Samsung"]
        brands.append("Zara")
        brands.insert(2, "Gucci")
        brands.pop(0)
        brands.sort(reverse=1)
        brands.remove("Puma")
        brands.extend(["1", "2"])
        print(brands)
    case 3:
        my_tuple = (1, "Mahdi", False, 1)
        my_tuple_count = my_tuple.count(1)
        my_tuple_len = len(my_tuple)
        print(my_tuple_count)
        print(my_tuple_len)
    case 4:
        cart_items = []
        cart_prices = []
        while True:
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Show Cart")
            print("4. Print Invoice")
            print("5. Exit")
            choice = int(input("Choose an opion: "))

            if choice == 1:
                item = input("Enter product name: ")
                price = int(input("Etner product price: "))
                cart_items.append(item)
                cart_prices.append(price)
                print("successfully")
            elif choice == 2:
                name = input("Enter product name to remove: ")
                if name in cart_items :
                    index = cart_items.index(name)
                    cart_items.pop(index)
                    cart_prices.pop(index)
                    print(name, "removed successfully!")
                else:
                    print("Product not found!")
            elif choice == 3:
                for i in range(len(cart_items)):
                    print(cart_items[i], "-", cart_prices[i])
            elif choice == 4:
                total = sum(cart_prices)
                final_price = total * 1.09
                for i in range(len(cart_items)):
                    print(cart_items[i], "-", cart_prices[i])
                print("Final Price:", final_price)
            elif choice == 5:
                print("Goodbye!")
                break
    