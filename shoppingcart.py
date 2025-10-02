# Online Shopping Cart for Bike Engines (OOP in Python - Menu Driven)

class Engine:
    def __init__(self, engine_id, name, price, horsepower):
        self.engine_id = engine_id
        self.name = name
        self.price = price
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.engine_id}. {self.name} ({self.horsepower} HP) - ₹{self.price}"


class CartItem:
    def __init__(self, engine, quantity=1):
        self.engine = engine
        self.quantity = quantity

    def total_price(self):
        return self.engine.price * self.quantity

    def __str__(self):
        return f"{self.engine.name} x {self.quantity} = ₹{self.total_price()}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, engine, quantity=1):
        for item in self.items:
            if item.engine.engine_id == engine.engine_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(engine, quantity))

    def remove_item(self, engine_id):
        self.items = [item for item in self.items if item.engine.engine_id != engine_id]

    def view_cart(self):
        if not self.items:
            return "🛒 Your cart is empty."
        cart_details = "\n".join([str(item) for item in self.items])
        return f"\n--- Shopping Cart ---\n{cart_details}\n----------------------\nTotal = ₹{self.get_total()}"

    def get_total(self):
        return sum(item.total_price() for item in self.items)


# Sample engines available in the store
engines = [
    Engine(1, "Yamaha 150cc Engine", 55000, 150),
    Engine(2, "KTM 200cc Engine", 85000, 200),
    Engine(3, "Royal Enfield 350cc Engine", 120000, 350),
    Engine(4, "Honda 500cc Engine", 200000, 500)
]

def show_store():
    print("\n=== Available Bike Engines ===")
    for engine in engines:
        print(engine)


if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\n===== Online Bike Engine Store =====")
        print("1. View Available Engines")
        print("2. Add Engine to Cart")
        print("3. Remove Engine from Cart")
        print("4. View Cart")
        print("5. Checkout & Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_store()

        elif choice == "2":
            show_store()
            try:
                eng_id = int(input("Enter Engine ID to add: "))
                qty = int(input("Enter quantity: "))
                selected = next((e for e in engines if e.engine_id == eng_id), None)
                if selected:
                    cart.add_item(selected, qty)
                    print(f"✅ {selected.name} x{qty} added to cart.")
                else:
                    print("❌ Invalid Engine ID.")
            except ValueError:
                print("⚠ Please enter valid numbers.")

        elif choice == "3":
            try:
                eng_id = int(input("Enter Engine ID to remove: "))
                cart.remove_item(eng_id)
                print("🗑 Engine removed from cart (if it existed).")
            except ValueError:
                print("⚠ Please enter a valid number.")

        elif choice == "4":
            print(cart.view_cart())

        elif choice == "5":
            print("\n🛒 Final Cart Summary:")
            print(cart.view_cart())
            print("✅ Thank you for shopping with us!")
            break

        else:
            print("⚠ Invalid choice! Please enter a number between 1-5.")
