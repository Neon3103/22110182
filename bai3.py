def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1): 
        swapped = False
        for j in range(n - 1 - i):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  
            break

while True:
    user_input = input("Nhập các số nguyên cách nhau bởi dấu cách: ")
    tokens = user_input.split()
    try:
        arr = [int(token) for token in tokens]
        break
    except ValueError:
        print("Lỗi: Bạn đã nhập số thập phân hoặc giá trị không hợp lệ. Vui lòng nhập lại.")

bubble_sort(arr)

print("Mảng sau khi sắp xếp:", arr)
