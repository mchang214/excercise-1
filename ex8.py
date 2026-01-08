numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon xoa: "))

while value in numbers:
    numbers.remove(value)

print("List moi la: ",numbers)