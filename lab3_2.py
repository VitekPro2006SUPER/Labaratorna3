import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class InverseRegressionPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регресія: y = a + b/x")
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

        # === ОБЧИСЛЕННЯ КОЕФІЦІЄНТІВ ===
        # Модель: y = a + b * (1/x)
        # Робимо лінеаризацію: замінюємо X на 1/X
        x_inv = 1 / x  
        b, a = np.polyfit(x_inv, y, 1)

        # === ПОБУДОВА ГРАФІКА ===
        # Створюємо плавний діапазон X для красивої лінії
        x_fit = np.linspace(min(x), max(x), 200)
        
        # Рахуємо Y для моделі
        y_fit = a + b / x_fit

        # Очищення та малювання
        self.ax.clear()
        
        # Експериментальні точки
        self.ax.scatter(x, y, color='red', s=50, label='Експериментальні точки', zorder=5)
        
        # Теоретична крива
        label_text = f'y = {a:.2f} + {b:.2f}/x'
        self.ax.plot(x_fit, y_fit, color='blue', linewidth=2, label=label_text)
        
        # Налаштування вигляду
        self.ax.set_title("Апроксимація функцією y = a + b/x")
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.legend()
        self.ax.grid(True, linestyle='--')
        
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InverseRegressionPlot()
    window.show()
    sys.exit(app.exec())