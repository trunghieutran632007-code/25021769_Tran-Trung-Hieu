def create_diamond(K, border_char, inner_char, stitch_char):
    # Tổng số dòng cần in là 2*K - 1
    total_rows = 2 * K - 1
    
    # Duyệt qua từng dòng
    for i in range(total_rows):
        # Tính khoảng cách từ dòng hiện tại (i) đến dòng giữa (K-1)
        # abs() giúp chúng ta xử lý đối xứng nửa trên và nửa dưới giống hệt nhau
        dist_from_center = abs((K - 1) - i)
        
        # 1. Tính toán phần lề trái (khoảng trắng bên ngoài)
        leading_spaces = " " * dist_from_center
        
        # 2. Xác định ký tự viền (border)
        # Nếu khoảng cách đến tâm = 0 (tức là hàng giữa), dùng stitch_char
        if dist_from_center == 0:
            current_border = stitch_char
        else:
            current_border = border_char
            
        # 3. In ra dòng hoàn chỉnh
        if dist_from_center == K - 1:
            # Trường hợp đặc biệt: Đỉnh trên cùng và dưới cùng (chỉ có 1 ký tự)
            print(f"{leading_spaces}{current_border}")
        else:
            # Trường hợp các dòng thân: Có 2 viền và ký tự inner ở giữa
            # Công thức tính số lượng ký tự bên trong dựa trên khoảng cách tới tâm
            num_inner = 2 * (K - 1 - dist_from_center) - 1
            inner_part = inner_char * num_inner
            
            print(f"{leading_spaces}{current_border}{inner_part}{current_border}")

# --- Chạy thử hàm với ví dụ trong bài ---
# K=5, Viền='@', Bên trong='~', Stitch='S'
print("Kết quả chạy thử:")
create_diamond(6, '@', '~', 'S')