# File để bạn có thể thêm các kỹ năng (Skills) cho Bot
# Hướng dẫn thực hiện:

# Bước 1: Thêm từ khóa (keys) vào file keywords.json
# Mỗi skill được định nghĩa dưới dạng một danh sách từ khóa đại diện.
# Ví dụ:
# "keyword": {
#     "cus__skill__1": [  # Tên của skill
#         "key 1",        # Từ khóa đại diện cho skill này
#         "key 2",
#         "key 3",
#         "key 4"
#     ],
#     "cus__skill__2": [
#         "key 1",
#         "key 2",
#         "key 3",
#         "key 4"
#     ]
# }
# Cụ thể:
# - skill chúc mừng sinh nhật:
#     "skill__happy__birthday": [
#         "mừng sinh nhật",
#         "birthday"
#     ]
# - skill chúc Tết:
#     "skill__happy__new__year": [
#         "chúc tết",
#         "tết nguyên đán"
#     ]

# Bước 2: Tạo hàm xử lý logic cho từng skill.
# Các hàm này sẽ được gọi khi từ khóa tương ứng được phát hiện trong câu hỏi của người dùng.

import random  # Thư viện để lựa chọn ngẫu nhiên các câu trả lời

# Hàm chúc mừng sinh nhật
def skill__happy__birthday(skill, data):
    """
    Hàm xử lý logic cho skill chúc mừng sinh nhật.
    
    Args:
        skill (str): Tên của skill (không sử dụng trong logic này).
        data (str): Chuỗi đầu vào từ người dùng.

    Returns:
        Tuple[str, bool]: 
            - Một chuỗi chúc mừng sinh nhật ngẫu nhiên.
            - `True` để xác nhận hoàn thành skill.
    """
    answers = [
        "Chúc mừng sinh nhật! Mong rằng bạn có một ngày thật vui vẻ và đầy ý nghĩa.",
        "Chúc mừng sinh nhật! Hy vọng năm mới của bạn sẽ đem lại nhiều thành công và niềm vui.",
        "Happy birthday! Chúc bạn luôn khỏe mạnh, hạnh phúc và thành công trong cuộc sống.",
        "Sinh nhật vui vẻ! Hãy tận hưởng ngày đặc biệt này cùng gia đình và bạn bè của bạn."
    ]
    # Lựa chọn ngẫu nhiên một câu trả lời từ danh sách
    answer = random.choice(answers)
    return answer, True

# Hàm chúc mừng năm mới
def skill__happy__new__year(skill, data):
    """
    Hàm xử lý logic cho skill chúc mừng năm mới.
    
    Args:
        skill (str): Tên của skill (không sử dụng trong logic này).
        data (str): Chuỗi đầu vào từ người dùng.

    Returns:
        Tuple[str, bool]: 
            - Một chuỗi chúc mừng năm mới ngẫu nhiên.
            - `True` để xác nhận hoàn thành skill.
    """
    answers = [
        "Chúc mừng năm mới! Mong rằng năm mới mang lại nhiều niềm vui, thành công và sức khỏe cho bạn.",
        "Chúc mừng năm mới! Hy vọng năm mới sẽ đem lại nhiều cơ hội và thành tựu lớn cho bạn.",
        "Happy New Year! Chúc bạn có một năm mới thật phát đạt và hạnh phúc.",
        "Năm mới an lành! Chúc bạn và gia đình có một kỳ nghỉ vui vẻ và đầy ý nghĩa."
    ]
    # Lựa chọn ngẫu nhiên một câu trả lời từ danh sách
    answer = random.choice(answers)
    return answer, True

import random  # Thư viện để lựa chọn ngẫu nhiên các câu trả lời

# Hàm chúc mừng sinh nhật
def skill__happy__birthday(skill, data):
    """
    Hàm xử lý logic cho skill chúc mừng sinh nhật.
    
    Args:
        skill (str): Tên của skill (không sử dụng trong logic này).
        data (str): Chuỗi đầu vào từ người dùng.

    Returns:
        Tuple[str, bool, bool]: 
            - Một chuỗi văn bản chúc mừng sinh nhật.
            - `True` để tiếp tục hỏi lại cuộc hội thoại, `False` nếu không tiếp tục hỏi (chờ khẩu lệnh người dùng).
            - `True` để lưu câu trả lời để sử dụng lại sau, `False` nếu không lưu.
    """
    answers = [
        "Chúc mừng sinh nhật! Mong rằng bạn có một ngày thật vui vẻ và đầy ý nghĩa.",
        "Chúc mừng sinh nhật! Hy vọng năm mới của bạn sẽ đem lại nhiều thành công và niềm vui.",
        "Happy birthday! Chúc bạn luôn khỏe mạnh, hạnh phúc và thành công trong cuộc sống.",
        "Sinh nhật vui vẻ! Hãy tận hưởng ngày đặc biệt này cùng gia đình và bạn bè của bạn."
    ]
    # Lựa chọn ngẫu nhiên một câu trả lời từ danh sách
    text = random.choice(answers)
    
    # True: Tiếp tục hỏi lại cuộc hội thoại
    # False: Chờ người dùng đưa ra khẩu lệnh tiếp theo
    continue_asking = True  
    
    # True: Lưu câu trả lời để sử dụng lại trong tương lai
    # False: Không lưu thông tin
    temporary_save = True  
    
    return text, continue_asking, temporary_save


# Hàm chúc mừng năm mới
def skill__happy__new__year(skill, data):
    """
    Hàm xử lý logic cho skill chúc mừng năm mới.
    
    Args:
        skill (str): Tên của skill (không sử dụng trong logic này).
        data (str): Chuỗi đầu vào từ người dùng.

    Returns:
        Tuple[str, bool, bool]: 
            - Một chuỗi văn bản chúc mừng năm mới.
            - `True` để tiếp tục hỏi lại cuộc hội thoại, `False` nếu không tiếp tục hỏi (chờ khẩu lệnh người dùng).
            - `True` để lưu câu trả lời để sử dụng lại sau, `False` nếu không lưu.
    """
    answers = [
        "Chúc mừng năm mới! Mong rằng năm mới mang lại nhiều niềm vui, thành công và sức khỏe cho bạn.",
        "Chúc mừng năm mới! Hy vọng năm mới sẽ đem lại nhiều cơ hội và thành tựu lớn cho bạn.",
        "Happy New Year! Chúc bạn có một năm mới thật phát đạt và hạnh phúc.",
        "Năm mới an lành! Chúc bạn và gia đình có một kỳ nghỉ vui vẻ và đầy ý nghĩa."
    ]
    # Lựa chọn ngẫu nhiên một câu trả lời từ danh sách
    text = random.choice(answers)
    
    # True: Tiếp tục hỏi lại cuộc hội thoại
    # False: Chờ người dùng đưa ra khẩu lệnh tiếp theo
    continue_asking = True  
    
    # True: Lưu câu trả lời để sử dụng lại trong tương lai
    # False: Không lưu thông tin
    temporary_save = True  
    
    return text, continue_asking, temporary_save
