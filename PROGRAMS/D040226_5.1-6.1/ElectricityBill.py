class ElectricityBill:
    def __init__(self, customer_id,customer_name,units_consumed):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.units_consumed = units_consumed
    def display_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Units Consumed: {self.units_consumed} units")
    def calculate_bill(self):
        if self.units_consumed <= 100:
            bill_amount = self.units_consumed * 5
        elif 101 <= self.units_consumed <= 300:
            bill_amount = (100 * 5) + (self.units_consumed - 100) * 7
        else:
            bill_amount = (100 * 5) + (200 * 7) + (self.units_consumed - 300) * 10
        return bill_amount
# Example usage
if __name__ == "__main__":
    customer1 = ElectricityBill(1, "John Doe", 250)
    customer2 = ElectricityBill(2, "Jane Smith", 450)

    customers = [customer1, customer2]

    for customer in customers:
        customer.display_details()
        bill = customer.calculate_bill()
        print(f"Total Electricity Bill: {bill} units\n")

'''
Customer ID: 1
Customer Name: John Doe
Units Consumed: 250 units
Total Electricity Bill: 1550 units

Customer ID: 2
Customer Name: Jane Smith
Units Consumed: 450 units
Total Electricity Bill: 3400 units
'''