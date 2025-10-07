def format_price(prase:float) -> str:
    return f"ціна: {prase:.2f} грн"


def check_availability(*items, store: dict) -> dict:
    return {item: (item in store) for item in items}


def make_order(order: list, store: dict):
    unavailable = [item for item in order if item not in store]
    if unavailable:
        print("Замовлення неможливе! Немає в наявності:",", ".join(unavailable))
        return


    total_price = sum(store[item] for item in order)
    while True:
        choice = input("Оберіть опцію (1 - переглянути ціну, 2 - купити): ")
        if choice == "1":
            print("Вартість замовлення:", format_price(total_price))
        elif choice == "2":
            print("Ви купили товари на суму:", format_price(total_price))
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


def main():
    store = {
        "хліб": 25.5,
        "молоко": 32.0,
        "яйця": 55.25,
        "сир": 120.75,
        "кава": 210.0
    }

    print("Ласкаво просимо до магазину!")
    print("В наявності:", ", ".join(store.keys()))


    order = input("Введіть товари через кому: ").split(",")
    order = [item.strip() for item in order if item.strip()]

    make_order(order, store)


if __name__ == "__main__":
    main()
