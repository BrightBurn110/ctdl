class TuDien:
    def __init__(self):
        self.dictionary = {}

    def NhapTu(self):
        tu = input("Nhập từ: ").strip()
        dongnghia = input("Nhập từ đồng nghĩa (nếu có): ").strip()
        trai_nghia = input("Nhập từ trái nghĩa (nếu có): ").strip()

        # Hàm băm để lấy ký tự đầu tiên của từ làm khóa
        key = tu[0].lower()

        # Tạo hoặc cập nhật từ điển
        if key in self.dictionary:
            self.dictionary[key].append((tu, dongnghia, trai_nghia))
        else:
            self.dictionary[key] = [(tu, dongnghia, trai_nghia)]

    def DongNghia(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm khóa
        key = tu[0].lower()

        # Kiểm tra xem từ điển có từ cần tra không
        if key in self.dictionary:
            dongnghia_list = [entry[1] for entry in self.dictionary[key] if entry[0] == tu and entry[1] is not None]
            return dongnghia_list
        return []

    def TraiNghia(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm khóa
        key = tu[0].lower()

        # Kiểm tra xem từ điển có từ cần tra không
        if key in self.dictionary:
            trai_nghia_list = [entry[2] for entry in self.dictionary[key] if entry[0] == tu and entry[2] is not None]
            return trai_nghia_list
        return []

# Sử dụng:
td = TuDien()

# Nhập từ và các từ đồng nghĩa, từ trái nghĩa từ bàn phím
td.NhapTu()
td.NhapTu()
td.NhapTu()

# Tra từ
tu_can_tra = input("Nhập từ cần tra: ").strip()
dong_nghia_list = td.DongNghia(tu_can_tra)
trai_nghia_list = td.TraiNghia(tu_can_tra)

print(f"Từ '{tu_can_tra}' có các từ đồng nghĩa là: {dong_nghia_list}")
print(f"Từ '{tu_can_tra}' có các từ trái nghĩa là: {trai_nghia_list}")
