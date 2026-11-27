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
    