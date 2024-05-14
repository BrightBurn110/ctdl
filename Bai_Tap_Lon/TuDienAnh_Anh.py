class MoTa:
    def __init__(self, loaiTu, moTa, viDu):
        self.loaiTu = loaiTu
        self.moTa = moTa
        self.viDu = viDu

class Tu:
    def __init__(self, tu):
        self.tu = tu
        self.moTa = []
    
    def ThemMoTa(self, loaiTu, moTa, viDu):
        moTa_obj = MoTa(loaiTu, moTa, viDu)
        self.moTa.append(moTa_obj)

class TuDien:
    def __init__(self):
        self.tuDien = []

    def ThemTu(self, tu, loaiTu=None, moTa=None, viDu=None):
        tu_obj = Tu(tu)
        tu_obj.ThemMoTa(loaiTu, moTa, viDu)
        self.tuDien.append(tu_obj)

    def LoaiBoTu(self, tuMuonXoa):
        for tu in self.tuDien:
            if tu.tu == tuMuonXoa:
                self.tuDien.remove(tu)
                return True
        return False

    def TraCuuNghia(self, tuMuonTraCuu):
        for tu in self.tuDien:
            if tu.tu == tuMuonTraCuu:
                return tu.moTa
        return False

    def LuuTuDien(self):
        with open("Bai_Tap_Lon/n20dcat029_VuQuangKhai.txt", "a") as file:
            for tu in self.tuDien:
                file.write(tu.tu + ":\n")
                for moTa in tu.moTa:
                    file.write(f"- {moTa.loaiTu}: {moTa.moTa} (Example: {moTa.viDu})\n")

    def DocFile(self):
        self.tuDien = []  # Reset dictionary when reading from file
        with open("Bai_Tap_Lon/n20dcat029_VuQuangKhai.txt", "r") as file:
            lines = file.readlines()
            tuMoi = None
            for line in lines:
                if line.strip() and line.strip()[-1] == ":":
                    tu = line.strip()[:-1]
                    tuMoi = Tu(tu)
                    self.tuDien.append(tuMoi)
                elif tuMoi:
                    parts = line.strip().split(":")
                    if len(parts) == 3:
                        tuLoai = parts[0].strip().strip(" -").strip()
                        moTa = parts[1].strip().rstrip(" (Example")
                        viDu = parts[2].strip().rstrip(")")
                        tuMoi.ThemMoTa(tuLoai, moTa, viDu)

def Menu():  
    tuDien = TuDien()  # Create TuDien instance
    while True:
        print("---------------------------Main Menu-----------------------")
        print("1. Thêm một mục từ mới vào từ điển.")
        print("2. Loại bỏ một mục từ của từ điển.")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển.")
        print("4. Lưu từ điển vào các tập tin.")
        print("5. Nạp từ điển từ các tập tin.")
        print("6. Thoát chương trình.")
        print("------------------------------------------------------------")
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            tuMuonThem = ""
            while tuMuonThem=="":
                tuMuonThem = input("Nhập từ mà bạn muốn thêm: ")
                if tuMuonThem=="":
                    print("Vui lòng nhập từ muốn thêm vào!")
            loaiTu = input("Nhập loại từ của từ vừa rồi: ")
            moTa = input("Nhập mô tả của từ vừa rồi: ")
            viDu = input("Nhập ví dụ của từ vừa rồi: ")
            tuDien.ThemTu(tuMuonThem, loaiTu, moTa, viDu)

        elif choice == "2":
            tuMuonXoa = input("Nhập từ mà bạn muốn xóa: ")
            if tuDien.LoaiBoTu(tuMuonXoa):
                print("Đã xóa từ")
            else:
                print("Từ bạn cần xóa không có trong từ điển")
            
        elif choice == "3":
            tuMuonTraCuu = input("Nhập từ mà bạn muốn Tra cứu nghĩa: ")
            nghia = tuDien.TraCuuNghia(tuMuonTraCuu)
            if nghia:
                print(tuMuonTraCuu)
                for x in nghia:
                    print(f"-{x.loaiTu}: {x.moTa} (Example:{x.viDu})")
            else:
                print("Từ bạn cần tra không có trong từ điển!")

        elif choice == "4":
            tuDien.LuuTuDien()
            print("Đã lưu!")

        elif choice == "5":
            tuDien.DocFile()
            print("Đã đọc!")
        elif choice == "6":
            print("Bạn đã thoát chương trình.")
            break
        else:
            print("Vui lòng nhập một số nguyên!")
            


if __name__ == "__main__":
    Menu()
