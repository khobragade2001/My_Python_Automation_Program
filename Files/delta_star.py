rows = int(input("Enter the number of rows for the horizontal delta pattern: "))

# Upper half of the delta pattern
for i in range(1, rows + 1):
    print("* " * i)

# Lower half of the delta pattern
for i in range(rows - 1, 0, -1):
    print("* " * i)
