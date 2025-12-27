import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class LinearRegressionPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Лінійна регресія (Ваш варіант)")
        self.setGeometry(200, 200, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot_regression()

    def plot_regression(self):
        x = np.array([1.0, 0.5, 0.3, 0.25, 0.2, 0.17, 0.14, 0.12], dtype=float)
        y = np.array([3.0, 2.0, 0.6, 1.5, 1.4, 1.3, 1.3, 1.2], dtype=float)

        # 1. Лінійна регресія (метод найменших квадратів)
        # fit = [a, b], де y = ax + b
        slope, intercept = np.polyfit(x, y, 1)

        # 2. Побудова точок для прямої лінії
        # Створюємо масив X від мінімального до максимального значення
        x_fit = np.linspace(min(x), max(x), 200)
        # Рахуємо Y для прямої
        y_fit = slope * x_fit + intercept

        # 3. Відображення на графіку
        self.ax.clear()
        
        # Експериментальні точки (розкид)
        self.ax.scatter(x, y, color='red', s=50, label='Експериментальні дані')
        
        # Лінія регресії
        self.ax.plot(x_fit, y_fit, color='blue', linewidth=2, 
                     label=f'Апроксимація: y = {slope:.2f}x + {intercept:.2f}')

        self.ax.set_title("Лінійна апроксимація даних")
        self.ax.set_xlabel('Значення X')
        self.ax.set_ylabel('Значення Y')
        self.ax.legend()
        self.ax.grid(True, linestyle='--')
        
        # Оновлення полотна
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LinearRegressionPlot()
    window.show()
    sys.exit(app.exec())