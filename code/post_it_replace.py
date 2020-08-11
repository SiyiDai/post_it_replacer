from PyQt5.QtWidgets import QApplication
from windows.main_window import MainWindow


def launch_main_window():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    launch_main_window()
