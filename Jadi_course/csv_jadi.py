import csv

with open("CSV_files/products.csv") as file:
    csv_data = list(csv.DictReader(file))

for row in csv_data:
    total = int(row["Quantity"]) * int(row["Price"])
    row["Total Price"] = total

with open("CSV_files/new_products", 'w', newline="") as file:
    fieldnames = ["Product Name", "Price", "Quantity", "Total Price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(csv_data)
