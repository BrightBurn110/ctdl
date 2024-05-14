class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.bai_hat = []

    def ThemBaiHat(self, ten_bai_hat, ten_nhac_si, ten_ca_si):
        self.bai_hat.append((ten_bai_hat, ten_nhac_si, ten_ca_si))

    def XemAlbum(self):
        print(f"Tên album: {self.ten_album}")
        print("Danh sách bài hát:")
        for idx, (ten_bai_hat, ten_nhac_si, ten_ca_si) in enumerate(self.bai_hat, start=1):
            print(f"Bài hát {idx}:")
            print(f"  - Tên bài hát: {ten_bai_hat}")
            print(f"  - Tên nhạc sĩ: {ten_nhac_si}")
            print(f"  - Tên ca sĩ: {ten_ca_si}")
        print()

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self):
        ten_album = input("Nhập tên album: ").strip()
        album = Album(ten_album)
        so_bai_hat = int(input(f"Nhập số bài hát của album '{ten_album}': "))
        for i in range(so_bai_hat):
            ten_bai_hat = input(f"Nhập tên bài hát {i+1}: ").strip()
            ten_nhac_si = input(f"Nhập tên nhạc sĩ của bài hát {ten_bai_hat}: ").strip()
            ten_ca_si = input(f"Nhập tên ca sĩ của bài hát {ten_bai_hat}: ").strip()
            album.ThemBaiHat(ten_bai_hat, ten_nhac_si, ten_ca_si)
        self.albums[ten_album] = album

    def XemAlbum(self, ten_album):
        if ten_album in self.albums:
            self.albums[ten_album].XemAlbum()
        else:
            print(f"Album '{ten_album}' không tồn tại trong từ điển.")

# Sử dụng:
td = TuDien()

# Nhập thông tin của các album từ bàn phím
td.NhapAlbum()
td.NhapAlbum()
td.NhapAlbum()

# Xem thông tin của một album
ten_album_can_xem = input("Nhập tên album cần xem: ").strip()
td.XemAlbum(ten_album_can_xem)
