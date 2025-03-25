from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class ThemeManager:
    @staticmethod
    def get_dark_theme():
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
        return palette

    @staticmethod
    def get_light_theme():
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorRole.Base, QColor(240, 240, 240))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(245, 245, 245))
        palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
        palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
        palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
        palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
        return palette

    @staticmethod
    def get_dark_stylesheet():
        return """
            QMainWindow {
                background-color: #353535;
            }
            QWidget {
                background-color: #353535;
                color: white;
                border: none;
            }
            QPushButton {
                background-color: #2a82da;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3292ea;
            }
            QPushButton:pressed {
                background-color: #1a72ca;
            }
            QLabel {
                color: white;
            }
            QMenuBar {
                background-color: #2a2a2a;
                color: white;
            }
            QMenuBar::item {
                padding: 8px 12px;
            }
            QMenuBar::item:selected {
                background-color: #2a82da;
            }
            QMenu {
                background-color: #2a2a2a;
                color: white;
            }
            QMenu::item:selected {
                background-color: #2a82da;
            }
            QToolBar {
                background-color: #2a2a2a;
                border: none;
            }
            QToolButton {
                background-color: transparent;
                color: white;
                padding: 8px;
                border-radius: 4px;
            }
            QToolButton:hover {
                background-color: #2a82da;
            }
            QStatusBar {
                background-color: #2a2a2a;
                color: white;
            }
        """

    @staticmethod
    def get_light_stylesheet():
        return """
            QMainWindow {
                background-color: white;
            }
            QWidget {
                background-color: white;
                color: black;
                border: none;
            }
            QPushButton {
                background-color: #2a82da;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3292ea;
            }
            QPushButton:pressed {
                background-color: #1a72ca;
            }
            QLabel {
                color: black;
            }
            QMenuBar {
                background-color: #f0f0f0;
                color: black;
            }
            QMenuBar::item {
                padding: 8px 12px;
            }
            QMenuBar::item:selected {
                background-color: #2a82da;
                color: white;
            }
            QMenu {
                background-color: white;
                color: black;
            }
            QMenu::item:selected {
                background-color: #2a82da;
                color: white;
            }
            QToolBar {
                background-color: #f0f0f0;
                border: none;
            }
            QToolButton {
                background-color: transparent;
                color: black;
                padding: 8px;
                border-radius: 4px;
            }
            QToolButton:hover {
                background-color: #2a82da;
                color: white;
            }
            QStatusBar {
                background-color: #f0f0f0;
                color: black;
            }
        """ 