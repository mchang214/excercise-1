numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon xoa: "))
if value in numbers:
    numbers.remove(value)
    print("Đã xóa thành công số xuất hiện đầu tiên")
    print("Dãy mới là: ",numbers)
else:
    print("Không có số đó để xóa")