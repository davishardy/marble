import os

from PySide6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QKeySequence
 
from core.retrieve import get_subfolders
from core.open_app import open_blender
from core.open_app import open_houdini
from core.open_app import open_nuke




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowFlags(Qt.WindowStaysOnTopHint) # For debugging, remove later
        username = os.path.basename(os.path.expanduser("~"))
        self.setWindowTitle(f"Marble - {username}")
        # self.setWindowTitle(f"Marble - dhardy21")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.setMovable(False)

        self.show_tab = QWidget()
        self.sequence_tab = QWidget()
        self.shot_tab = QWidget()
        self.assets_tab = QWidget()

        self.tab_widget.addTab(self.assets_tab, "Assets")
        self.tab_widget.addTab(self.show_tab, "Show")
        self.tab_widget.addTab(self.sequence_tab, "Sequence")
        self.tab_widget.addTab(self.shot_tab, "Shot")

        self.main_layout.addWidget(self.tab_widget)

        self.setup_assets_tab()
        self.setup_show_tab()
        self.setup_sequence_tab()
        self.setup_shot_tab()
        
        # Setup fullscreen toggle action
        self._setup_fullscreen_action()
        self._setup_tab_shortcuts()

    def _setup_fullscreen_action(self):
        """
        Sets up a QAction to toggle fullscreen mode.
        """
        fullscreen_action = QAction("Toggle Fullscreen", self)
        # To explicitly use F11 (which on many Macs requires pressing 'fn+F11'), use Qt.Key_F11.
        # The 'fn' key itself is not a standard modifier for QKeySequence.
        fullscreen_action.setShortcut(Qt.Key_F11)
        fullscreen_action.triggered.connect(self._toggle_fullscreen)
        self.addAction(fullscreen_action) # Add action to the main window to enable shortcut

    def _toggle_fullscreen(self):
        """
        Toggles the window between normal and fullscreen mode.
        """
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def _setup_tab_shortcuts(self):
        """
        Sets up keyboard shortcuts for switching tabs.
        """
        asset_tab_action = QAction("Go to Assets Tab", self)
        asset_tab_action.setShortcut(QKeySequence("Ctrl+1"))
        asset_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(0))
        self.addAction(asset_tab_action)

        show_tab_action = QAction("Go to Show Tab", self)
        show_tab_action.setShortcut(QKeySequence("Ctrl+2"))
        show_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(1))
        self.addAction(show_tab_action)

        sequence_tab_action = QAction("Go to Sequence Tab", self)
        sequence_tab_action.setShortcut(QKeySequence("Ctrl+3"))
        sequence_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(2))
        self.addAction(sequence_tab_action)

        shot_tab_action = QAction("Go to Shot Tab", self)
        shot_tab_action.setShortcut(QKeySequence("Ctrl+4"))
        shot_tab_action.triggered.connect(lambda: self.tab_widget.setCurrentIndex(3))
        self.addAction(shot_tab_action)


    def setup_show_tab(self):
        # Placeholder for Show tab content
        pass        

    def setup_assets_tab(self): # Renamed from setup_assets_tab to avoid conflict
        """
        Sets up the 'Assets' tab with nested sub-tabs.
        """

        # https://doc.qt.io/qtforpython-6/tutorials/basictutorial/tablewidget.html

        layout = QVBoxLayout(self.assets_tab)

        self.assets_sub_tab_widget = QTabWidget()
        self.assets_sub_tab_widget.setTabPosition(QTabWidget.West)

        self.characters_tab = QWidget()
        self.lights_tab = QWidget()
        self.materials_tab = QWidget()
        self.props_tab = QWidget()
        self.sets_tab = QWidget()

        self.assets_sub_tab_widget.addTab(self.characters_tab, "Characters")
        self.assets_sub_tab_widget.addTab(self.lights_tab, "Lights")
        self.assets_sub_tab_widget.addTab(self.materials_tab, "Materials")
        self.assets_sub_tab_widget.addTab(self.props_tab, "Props")
        self.assets_sub_tab_widget.addTab(self.sets_tab, "Sets")

        layout.addWidget(self.assets_sub_tab_widget)
        layout.addStretch()

        # Setup content for Characters tab
        characters_layout = QVBoxLayout(self.characters_tab)
        
        # Add a label
        characters_layout.addWidget(QLabel("Characters Content Here"))

        # Add a button
        blender_button = QPushButton("Open Blender")
        blender_button.clicked.connect(open_blender)

        houdini_button = QPushButton("Open Houdini")
        houdini_button.clicked.connect(open_houdini)

        nuke_button = QPushButton("Open Nuke")
        nuke_button.clicked.connect(open_nuke)



        characters_layout.addWidget(blender_button)
        characters_layout.addWidget(houdini_button)
        characters_layout.addWidget(nuke_button)


        #characters_layout.addStretch() # Push content to the top

    def setup_sequence_tab(self):
        # Placeholder for Sequence tab content
        pass

    def setup_shot_tab(self):
        # Placeholder for Shot tab content
        pass

    
