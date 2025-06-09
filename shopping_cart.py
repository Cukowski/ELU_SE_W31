def calculate_total(cart):
    total = 0.0
    for item in cart:
        try:
            total += float(item['price'])
        except (KeyError, ValueError, TypeError):
            print(f"Warning: Invalid item format: {item}")
    return total


def display_total(total):
    print(f"Total price: ${total:.2f}")


if __name__ == "__main__":
    cart = [
        {'name': 'Item A', 'price': 10.99},
        {'name': 'Item B', 'price': 5.99},
        {'name': 'Item C', 'price': 8.49},
    ]

    for item in cart:
        print(f"Item: {item['name']} - Price: ${item['price']}")

    total_price = calculate_total(cart)
    display_total(total_price)
