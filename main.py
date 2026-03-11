tasks = []

while True:
    print("\n--- TODO LIST ---")
    print("1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        task = input("Yangi vazifa yozing: ")
        tasks.append(task)
        print("Vazifa qo'shildi!")

    elif choice == "2":
        print("\nVazifalar:")
        for t in tasks:
            print("-", t)

    elif choice == "3":
        print("Dastur tugadi.")
        break

    else:
        print("Noto'g'ri tanlov!")
