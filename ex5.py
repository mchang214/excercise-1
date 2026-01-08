numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8, 9]

value = int(input("Nhập số muốn tìm: "))

lastIndex = -1
for i in range (0, len(numbers)):
    if numbers[i] == value:
        lastIndex = i
if lastIndex != -1:
    print("Lần cuối số đó xuất hiện la:", lastIndex)
else:
    print("Không có số đó")