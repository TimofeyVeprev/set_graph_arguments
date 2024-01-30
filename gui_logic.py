from PyQt5 import QtWidgets
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from gui import Ui_Dialog

matplotlib.use('TkAgg')


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)

        # Установка пользовательского интерфейс
        self.setupUi(dialog)
        self.pushButton.clicked.connect(self.generate_digits)  # Вызов функции generate_digits по нажатию на кнопку


        # ПОЛЯ КЛАССА
        # Параметры 1-ого графика
        self.ax_1 = None
        self.fig_1 = None
        self.canvas_1 = None
        self.toolbar_1 = None
        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        # Инициализируем параметры 1-ого графика
        self.initialize_graph()

    # Вводить число необходимо без пробела, к примеру, если необходимо
    # задать начальные значения x = 2, y = 2, то вводить число нужно - 22

    def generate_digits(self):  # Функция, устанавливающая введенные значения
        string = self.lineEdit.text()  # Считывание текста из строки
        num1 = int(string[0])  # Конвертирование первого символа (цифры) в число
        num2 = int(string[-1])  # Конвертирование последнего символа (цифры) в число

        x = list(range(num1 + 1))
        y = list(range(num2 + 1))

        self.plotting(x, y)  # Устанавливаем значения графику
        pass



    def initialize_graph(self) -> None:
        """ Инициализирует фигуру matplotlib внутри контейнера GUI.
        Вызываем только один раз для инициализации объектов графика."""

        # Создание фигуры (self.fig и self.ax)
        self.fig_1 = Figure()  # Создание пустой фигуры
        self.ax_1 = self.fig_1.add_subplot(111)  # Место для графика, вид разделения
        # Создание холста
        self.canvas_1 = FigureCanvas(self.fig_1)
        self.plotLayout.addWidget(self.canvas_1)
        # Создание Toolbar
        self.toolbar_1 = NavigationToolbar(
            self.canvas_1, self.plotWindow, coordinates=True)
        self.plotLayout.addWidget(self.toolbar_1)

    def plotting(self, data_x, data_y):
        # Очищаем график
        self.ax_1.clear()
        # Задаем название осей
        self.ax_1.set_xlabel('x')  # Необязательно
        self.ax_1.set_ylabel('y')  # Необязательно

        # Строим график
        self.ax_1.plot(data_x, data_y, color='g')

        # Убеждаемся, что все помещается внутри холста
        self.fig_1.tight_layout()
        # Показываем новую фигуру в интерфейсе
        self.canvas_1.draw()

