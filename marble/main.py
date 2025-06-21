import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():
    """Main function to run the Marble application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()