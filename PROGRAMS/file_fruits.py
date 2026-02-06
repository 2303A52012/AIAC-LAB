# Python program to create a text file, write sample text, read and display the content

def main():
    filename = "fruits.txt"
    fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

    # Write sample text to the file
    with open(filename, "w") as file:
        for fruit in fruits:
            file.write(fruit + "\n")

    # Read and display the content
    print("Contents of the file:")
    with open(filename, "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()
