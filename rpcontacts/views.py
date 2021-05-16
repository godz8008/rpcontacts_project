# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    Qwidget,
)

class Window(QmainWindow):
    """Main Window."""
    def __init__(self, perent=None):
        """Initializer."""
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
