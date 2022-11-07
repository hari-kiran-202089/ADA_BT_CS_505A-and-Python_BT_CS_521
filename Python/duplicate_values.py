# Lab 6: Write a function to find Duplicate values in the List
def find_duplicates(values):
    # Using Set data structure since lookup is very fast

    unique = set()  # Set to store the unique values
    duplicates = set()  # set to store the duplicate values

    for val in values:  # O(N)
        if val in unique:
            duplicates.add(val)
        else:
            unique.add(val)
    return list(duplicates)


if __name__ == "__main__":
    values = [int(x)
              for x in input("Enter space seperated values: ").strip().split(" ")]
    print("Duplicate values are", find_duplicates(values))
