import random

def menu():
    print('------------------------------MENU--------------------------')
    print('1. In ra danh sách vừa tạo.')
    print('2. In đảo ngược danh sách.')
    print('3. Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).')
    print('4. tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.')
    print('5. đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.')
    print('6. In ra vị trí các phần tử là số nguyên tố.')
    print('7. tìm các số duy nhất (không trùng lặp) trong danh sách.')
    print('8. liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.')
    print('9. In ra các đoạn con trong danh sách giảm liên tiếp.')
    print('10. Thoát')
    cl = int(input('moi ban chon (1 - 10): '))
    return cl

def tao_mang():
    n = int(input('nhap so phan tu cua mang: '))
    lst = list()
    for i in range(n):
        x = random.randint(1, 100)
        lst.append(x)
    return lst

def in_danh_sach(lst):
    print(lst)

def in_ds_dao_nguoc(lst):
    print(f'ds ban dau: {lst}')
    print(f'ds dao nguoc: {lst[::-1]}')

def in_danh_sach_sx(lst):
    print(f'ds ban dau: {lst}')
    print(f'ds sau da dc sx: {sorted(lst)}')

def tim_max_trong_mang(lst):
    print(f'ds ban dau: {lst}')
    maximum = 0
    count = 0
    for i in range(len(lst)):
        if lst[i] >= maximum:
            maximum = lst[i]
            count = i
    print(f'ptu lon nhat trong mang: {maximum} va nam o vi tri: {count}')

def so_sanh(lst):
    num = int(input('nhap gia tri X muon dem: '))
    count_list = list()
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count+=1
            count_list.append(i)
    print(lst)
    print(f'so ptu co gia tri bang {num} la {count} nam o cac vi tri: {count_list}')

def ds_so_nguyen_to(lst):
    lst_songuyento = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97]
    lst_num = list()
    count_list = list()
    for i in range(len(lst)):
        if lst[i] not in lst_songuyento:
            continue
        else:
            count_list.append(i)
    print(lst)
    print(f'vi tri cac so nguyen to: {count_list}')
    
def so_duy_nhat(lst):
    list_num = list()
    for item in lst:
        if lst.count(item) == 1:
            list_num.append(item)
    print(lst)
    print(f'cac so duy nhat trong ds la{list_num}')

def liet_ke(lst):
    print(lst)
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count+=1
        print(f'{lst[i]}: {count}')

def doan_con(lst):
    print(lst)

    for i in range(len(lst) - 1):
        new_list = [lst[i]]
        for j in range(i+1, len(lst)):
            if lst[j] < lst[j-1]:
                new_list.append(lst[j])
            else:
                break
        if len(new_list) > 1:
            print(new_list)

if __name__ == '__main__':
    while True:
        res = menu()
        print(res)
        if res == 1:
            ds = tao_mang()
            in_danh_sach(ds)
        if res == 2:
            ds = tao_mang()
            in_ds_dao_nguoc(ds)
        if res == 3:
            ds = tao_mang()
            in_danh_sach_sx(ds)
        if res == 4:
            ds = tao_mang()
            tim_max_trong_mang(ds)
        if res == 5:
            ds = tao_mang()
            so_sanh(ds)
        if res == 6:
            ds = tao_mang()
            ds_so_nguyen_to(ds)
        if res == 7:
            ds = tao_mang()
            so_duy_nhat(ds)
        if res == 8:
            ds = tao_mang()
            liet_ke(ds)
        if res == 9:
            ds = tao_mang()
            doan_con(ds)
        if res == 10:
            break
