numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon tim: "))

if value in numbers:
    firstIndex = numbers.index(value)
    print("Vị trí số đó xuất hiện lần đầu là:", firstIndex)
else:
    print("Không có số đó")