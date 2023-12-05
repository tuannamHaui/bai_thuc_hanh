import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
file_path = 'Student_Performance.csv'
data = pd.read_csv(file_path)

# Hiển thị thông tin cơ bản về dữ liệu
print("Thông tin cơ bản về dữ liệu:")
print(data.info())

# Hiển thị 5 dòng đầu tiên của dữ liệu
print("\n5 dòng đầu tiên của dữ liệu:")
print(data.head())

# Thống kê mô tả của dữ liệu
print("\nThống kê mô tả của dữ liệu:")
print(data.describe())

# Tìm giá trị lớn nhất và nhỏ nhất của từng cột
print("\nGiá trị lớn nhất của từng cột:")
print(data.max())
print("\nGiá trị nhỏ nhất của từng cột:")
print(data.min())

# Vẽ biểu đồ phân bố của các cột số
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
for column in numerical_columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
