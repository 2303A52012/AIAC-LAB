class LibraryBook:
    def __init__(self,title,author, borrower,days_late):
        self.title = title
        self.author = author
        self.borrower = borrower
        self.days_late = days_late
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Borrower: {self.borrower}")
        print(f"Days Late: {self.days_late}")
    def calculate_late_fee(self):
        if self.days_late<=5:
            fee_per_day=5
        elif self.days_late<=10:
            fee_per_day=7
        else:
            fee_per_day=10
        total_fee=self.days_late*fee_per_day
        return total_fee
# Example usage
if __name__ == "__main__":
    book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "Alice", 4)
    book2 = LibraryBook("1984", "George Orwell", "Bob", 8)
    book3 = LibraryBook("To Kill a Mockingbird", "Harper Lee", "Charlie", 12)

    for book in [book1, book2, book3]:
        book.display_details()
        late_fee = book.calculate_late_fee()
        print(f"Late Fee: ${late_fee}\n")
        
'''
Title: The Great Gatsby
Author: F. Scott Fitzgerald
Borrower: Alice
Days Late: 4
Late Fee: $20

Title: 1984
Author: George Orwell
Borrower: Bob
Days Late: 8
Late Fee: $56

Title: To Kill a Mockingbird
Author: Harper Lee
Borrower: Charlie
Days Late: 12
Late Fee: $120
'''