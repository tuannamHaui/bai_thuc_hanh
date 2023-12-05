import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_signal(time, signal, title):
    plt.figure()
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def main():
    # Tạo dãy thời gian từ 0 đến 2 giây với bước 0.01 giây
    time = np.arange(0, 2, 0.01)

    # Tín hiệu hàm vuông
    square_wave = signal.square(2 * np.pi * 1 * time)

    # Tín hiệu hàm hình sin
    sine_wave = np.sin(2 * np.pi * 2 * time)

    # Vẽ dạng tín hiệu hàm
    plot_signal(time, square_wave, 'Square Wave')
    plot_signal(time, sine_wave, 'Sine Wave')

    # Tính tích chập giữa hai tín hiệu
    convolution_result = np.convolve(square_wave, sine_wave, mode='same')

    # Vẽ đồ thị của kết quả tích chập
    plot_signal(time, convolution_result, 'Convolution Result')

    # Xác định đáp ứng xung đơn vị của hệ thống
    system_response = signal.impulse([1, 2, 1], T=time)
    
    # Vẽ đồ thị đáp ứng xung đơn vị của hệ thống
    plot_signal(system_response[0], system_response[1], 'System Impulse Response')

if __name__ == "__main__":
    main()
