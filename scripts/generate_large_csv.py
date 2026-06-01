import csv

with open("data/large_data.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["CustomerID", "Name", "City", "Amount"])

    for i in range(1, 100001):
        writer.writerow([
            i,
            f"Customer_{i}",
            f"City_{i % 100}",
            i * 10
        ])

print("Large CSV file generated successfully")