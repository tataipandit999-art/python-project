# MOBILE SHOP CRUD PROJECT

mobiles = []


def add_mobile():
    print("\n========== ADD MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("Mobile ID already exists.")
            return

    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    mobiles.append([mobile_id, brand, model, price, quantity])
    print("Mobile added successfully.")


def display_mobiles():
    print("\n========== MOBILE LIST ==========")

    if len(mobiles) == 0:
        print("No mobile records available.")
        return

    print("-" * 75)
    print(f"{'ID':<8}{'Brand':<15}{'Model':<20}{'Price':<15}{'Quantity':<10}")
    print("-" * 75)

    for mobile in mobiles:
        print(f"{mobile[0]:<8}{mobile[1]:<15}{mobile[2]:<20}"
              f"{mobile[3]:<15.2f}{mobile[4]:<10}")

    print("-" * 75)


def search_mobile():
    print("\n========== SEARCH MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to search: "))

    found = False
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found!")
            print("Mobile ID :", mobile[0])
            print("Brand     :", mobile[1])
            print("Model     :", mobile[2])
            print("Price     :", mobile[3])
            print("Quantity  :", mobile[4])
            found = True
            break

    if found == False:
        print("Mobile not found.")


def update_mobile():
    print("\n========== UPDATE MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to update: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found.")
            print("Current Brand    :", mobile[1])
            print("Current Model    :", mobile[2])
            print("Current Price    :", mobile[3])
            print("Current Quantity :", mobile[4])

            print("\nEnter New Details")
            mobile[1] = input("Enter New Brand: ")
            mobile[2] = input("Enter New Model: ")
            mobile[3] = float(input("Enter New Price: "))
            mobile[4] = int(input("Enter New Quantity: "))

            print("Mobile updated successfully.")
            return

    print("Mobile not found.")


def delete_mobile():
    print("\n========== DELETE MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to delete: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found.")
            print("Brand :", mobile[1])
            print("Model :", mobile[2])

            choice = input("Do you want to delete this mobile? (Y/N): ")

            if choice.upper() == "Y":
                mobiles.remove(mobile)
                print("Mobile deleted successfully.")
            else:
                print("Delete operation cancelled.")
            return

    print("Mobile not found.")


def dashboard():
    while True:
        print("\n" + "=" * 45)
        print(" MOBILE SHOP MANAGEMENT")
        print("=" * 45)
        print("1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_mobile()
            case "2":
                display_mobiles()
            case "3":
                search_mobile()
            case "4":
                update_mobile()
            case "5":
                delete_mobile()
            case "6":
                print("\nThank you for using Mobile Shop Management.")
                break
            case _:
                print("Invalid choice. Please try again.")


def main():
    dashboard()


if __name__ == "__main__":
    main()
