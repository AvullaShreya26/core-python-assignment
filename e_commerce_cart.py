# e_commerce_cart.py

def calculate_total_price(cart_items: dict) -> float:
    if not cart_items:
        print("Cart is empty.")
        return 0.0
    
    total_items = len(cart_items)
    total_price = sum(cart_items.values())

    if total_items > 5:
        discount = 0.10  
        total_price *= (1 - discount)

    return total_price

if __name__ == "__main__":
    cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
    total = calculate_total_price(cart_items)
    print(f"Total Price: {int(total)}")
