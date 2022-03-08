import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow

from Ui_TitleWindow import Ui_TitleWindow

class TitleWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_TitleWindow()
        self.ui.setupUi(self.main_win)
        self.signals()

    def signals(self):
        self.ui.query_menu_button.clicked.connect()
        self.ui.update_database_menu_button.clicked.connect()
        self.ui.exit_button.clicked.connect(self.exit())

    # --- slots ---
    def exit(self):
        running = False


    def show(self):
        self.main_win.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = TitleWindow()
    main_win.show()
    sys.exit(app.exec())