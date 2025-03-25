from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QPushButton, QStatusBar,
                            QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QFont
from .theme_manager import ThemeManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bBiometrics")
        self.setMinimumSize(800, 600)
        self.is_dark_mode = False
        
        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(10, 10, 10, 10)
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create toolbar
        self.create_toolbar()
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Create main content area
        self.create_main_content()
        
        # Apply initial theme
        self.apply_theme()
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        new_action = QAction("New Session", self)
        open_action = QAction("Open Data", self)
        save_action = QAction("Save Data", self)
        file_menu.addActions([new_action, open_action, save_action])
        
        # View menu
        view_menu = menubar.addMenu("View")
        stats_action = QAction("Statistics", self)
        graphs_action = QAction("Graphs", self)
        view_menu.addActions([stats_action, graphs_action])
        
        # Settings menu
        settings_menu = menubar.addMenu("Settings")
        config_action = QAction("Configuration", self)
        theme_action = QAction("Toggle Theme", self)
        theme_action.triggered.connect(self.toggle_theme)
        settings_menu.addActions([config_action, theme_action])
        
    def create_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        
        # Add toolbar actions with icons (you'll need to add actual icons)
        start_action = QAction("Start Tracking", self)
        stop_action = QAction("Stop Tracking", self)
        export_action = QAction("Export Data", self)
        
        toolbar.addActions([start_action, stop_action, export_action])
        
    def create_main_content(self):
        # Create a container for the main content
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setSpacing(10)
        
        # Left panel for controls
        left_panel = QFrame()
        left_panel.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(10)
        
        # Add some example controls with modern styling
        tracking_status = QLabel("Tracking Status: Stopped")
        tracking_status.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        
        start_button = QPushButton("Start Tracking")
        stop_button = QPushButton("Stop Tracking")
        
        # Connect button signals
        start_button.clicked.connect(self.start_tracking)
        stop_button.clicked.connect(self.stop_tracking)
        
        left_layout.addWidget(tracking_status)
        left_layout.addWidget(start_button)
        left_layout.addWidget(stop_button)
        left_layout.addStretch()
        
        # Right panel for data display
        right_panel = QFrame()
        right_panel.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)
        
        # Add some example labels with modern styling
        stats_label = QLabel("Statistics")
        stats_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        data_label = QLabel("Data Display Area")
        
        right_layout.addWidget(stats_label)
        right_layout.addWidget(data_label)
        right_layout.addStretch()
        
        # Add panels to main layout
        content_layout.addWidget(left_panel, 1)
        content_layout.addWidget(right_panel, 2)
        
        # Add content to main layout
        self.layout.addWidget(content_widget)
        
    def apply_theme(self):
        if self.is_dark_mode:
            self.setPalette(ThemeManager.get_dark_theme())
            self.setStyleSheet(ThemeManager.get_dark_stylesheet())
        else:
            self.setPalette(ThemeManager.get_light_theme())
            self.setStyleSheet(ThemeManager.get_light_stylesheet())
            
    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.apply_theme()
        
    def start_tracking(self):
        self.status_bar.showMessage("Tracking started...")
        
    def stop_tracking(self):
        self.status_bar.showMessage("Tracking stopped.") 