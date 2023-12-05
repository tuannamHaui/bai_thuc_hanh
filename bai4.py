import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    try:
        # Đọc dữ liệu từ file CSV, bỏ qua các dòng không phải dữ liệu
        data = pd.read_csv("diemPython.csv", encoding='latin1', skiprows=1)
        return data
    except FileNotFoundError:
        print("Không tìm thấy file CSV.")
        return None
    except pd.errors.EmptyDataError:
        print("File CSV rỗng.")
        return None
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu: {e}")
        return None

def generate_report(data):
    if data is not None:
        # Hiển thị thông tin mẫu về dữ liệu
        print("Dữ liệu mẫu:")
        print(data.head())

        # Vẽ biểu đồ hoặc thực hiện các thao tác khác để tạo báo cáo
        # Dưới đây là một ví dụ về việc vẽ biểu đồ cột cho điểm số học viên
        columns_to_plot = ['Lo?i A+', 'Lo?i A', 'Lo?i B+', 'Lo?i B', 'Lo?i C+', 'Lo?i C', 'Lo?i D+', 'Lo?i D', 'Lo?i F']

        # Kiểm tra xem tất cả các cột cần vẽ biểu đồ có trong DataFrame không
        if all(column in data.columns for column in columns_to_plot):
            data[columns_to_plot].plot(kind='bar', stacked=True)
            plt.title('Biểu Đồ Điểm Số Học Viên')
            plt.xlabel('Số SV')
            plt.ylabel('Số Lượng')
            plt.legend(title='Loại Điểm')
            plt.show()
        else:
            print("Các cột cần thiết không tồn tại trong dữ liệu.")

if __name__ == "__main__":
    file_path = "du_lieu.csv"  # Đặt tên file CSV của bạn ở đây

    # Đọc dữ liệu từ file CSV
    data = read_data(file_path)

    # Tạo báo cáo nếu dữ liệu tồn tại
    if data is not None:
        generate_report(data)
