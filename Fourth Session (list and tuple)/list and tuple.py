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
    case 5:
        my_number_list = []
        while True:
            number = input("Enter a number: or write e to exit: ")
            if number == "e":
                break
            else:
                my_number_list.append(int(number))
        print("Original List:", my_number_list)
        choice = int(input("Enter rotation number: "))
        choice = choice % len(my_number_list)
        new_number = my_number_list[-choice:] + my_number_list[:-choice]
        print("New List:", new_number)
    case 6:
        watchlist = []
        while True:
            print("1. Add Movie")
            print("2. Remove Movie")
            print("3. Show Movies")
            print("4. Sort Movies")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter movie name: ")
                year = int(input("Enter release year: "))
                rating = float(input("Enter movie rating: "))
                movie = (name, year, rating)
                watchlist.append(movie)
                print("Movie added successfully!")

            elif choice == "2":
                name = input("Enter movie name to remove: ")
                found = False
                for movie in watchlist:
                    if movie[0].lower() == name.lower():
                        watchlist.remove(movie)
                        found = True
                        print("Movie removed successfully!")
                        break
                if not found:
                    print("Movie not found!")

            elif choice == "3":
                if len(watchlist) == 0:
                    print("Watchlist is empty!")
                else:
                    for movie in watchlist:
                        print("Name:", movie[0])
                        print("Year:", movie[1])
                        print("Rating:", movie[2])
                        print("----------------")

            elif choice == "4":
                watchlist.sort()
                print("Movies sorted alphabetically!")
                for movie in watchlist:
                    print(movie)

            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice!")
