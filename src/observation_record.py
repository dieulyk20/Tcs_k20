from datetime import datetime

ma_quan_sat = input("Nhap ma quan sat: ")
dai_luong = input("Nhap ten dai luong: ")
gia_tri_do = float(input("Nhap gia tri do: "))
don_vi = input("Nhap don vi: ")

thoi_diem = datetime.now()
thoi_diem_str = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print("\n— PHIEU QUAN SAT —")
print(f"Ma quan sat: {ma_quan_sat}")
print(f"Dai luong: {dai_luong}")
print(f"Gia tri: {gia_tri_do:.2f} {don_vi}")
print(f"Thoi diem: {thoi_diem_str}")

from datetime import datetime

ma_quan_sat = input("Nhập mã quan sát: ")
dai_luong = input("Nhập đại lượng: ")
gia_tri_do = float(input("Nhập giá trị đo: "))
don_vi = input("Nhập đơn vị: ")

thoi_diem = datetime.now()
thoi_diem_hien_thi = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng : {dai_luong}")
print(f"Giá trị : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm : {thoi_diem_hien_thi}")