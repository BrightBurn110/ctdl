# Bai 1
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

    def TraTu(self, tu):
        # Hàm băm để lấy ký tự đầu tiên của từ làm khóa
        key = tu[0].lower()

        # Kiểm tra xem từ điển có từ cần tra không
        if key in self.dictionary:
            for word, dongnghia, trai_nghia in self.dictionary[key]:
                if word == tu:
                    return dongnghia, trai_nghia
        return None, None

# Sử dụng:
td = TuDien()
td.NhapTu()
td.NhapTu()
td.NhapTu()

# Tra từ
tu_can_tra = input("Nhập từ cần tra: ").strip()
dong_nghia, trai_nghia = td.TraTu(tu_can_tra)
if dong_nghia or trai_nghia:
    print(f"Từ '{tu_can_tra}' đồng nghĩa là: {dong_nghia}, trái nghĩa là: {trai_nghia}")
else:
    print(f"Từ '{tu_can_tra}' không có trong từ điển.")