import tkinter as tk

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity, price):
        self.items.append((item, quantity, price))

    def total_price(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        return total


def add_to_cart():
    item = entry_item.get()

    quantity = int(entry_quantity.get())
    price = int(entry_price.get())
    cart.add_item(item, quantity, price)
    listbox_items.insert(tk.END, f"{item} - {quantity} x {price}")
    label_total.config(text=f"Pay sum: {cart.total_price()} toman")


cart = Cart()

root = tk.Tk()
root.title("Shopping Cart")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Item Name:", bg="#f0f0f0").pack(padx=10, pady=10)
entry_item = tk.Entry(root)
entry_item.pack()

tk.Label(root, text="Quantity:", bg="#f0f0f0").pack(pady=5)
entry_quantity = tk.Entry(root)
entry_quantity.pack()

tk.Label(root, text="Price:", bg="#f0f0f0").pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack()

tk.Button(root, text="Add to Cart", command=add_to_cart, bg="#2264AF", fg="white").pack(pady=10)

listbox_items = tk.Listbox(root, width=50)
listbox_items.pack(pady=10)

label_total = tk.Label(root, text="Pay sum: 0 toman", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_total.pack(pady=10)

root.mainloop()
