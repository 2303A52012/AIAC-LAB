class Product:
    def __init__(self,product_id,product_name,price,category):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.category = category
    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
    def calculate_discount(self):
        if self.category.lower() == "electronics":
            discount = 0.10 * self.price
        elif self.category.lower() == "clothing":
            discount = 0.15 * self.price
        elif self.category.lower() == "grocery":
            discount = 0.05 * self.price
        else:
            discount = 0 * self.price
        return discount, self.price - discount
# Example usage
if __name__ == "__main__":
    product1 = Product(201, "Laptop", 1000, "Electronics")
    product2 = Product(202, "Jeans", 50, "Clothing")
    product3 = Product(203, "Book", 20, "Stationery")
    product4= Product(204, "Rice", 30, "Grocery")

    products = [product1, product2, product3, product4]

    for product in products:
        product.display_details()
        discount, final_price = product.calculate_discount()
        print(f"Discount: {discount}")
        print(f"Final Price after Discount: {final_price}\n")
        
'''
Product ID: 201
Product Name: Laptop
Price: 1000
Category: Electronics
Discount: 100.0
Final Price after Discount: 900.0

Product ID: 202
Product Name: Jeans
Price: 50
Category: Clothing
Discount: 7.5
Final Price after Discount: 42.5

Product ID: 203
Product Name: Book
Price: 20
Category: Stationery
Discount: 0
Final Price after Discount: 20

Product ID: 204
Product Name: Rice
Price: 30
Category: Grocery
Discount: 1.5
Final Price after Discount: 28.5
'''