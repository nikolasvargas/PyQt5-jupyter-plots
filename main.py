#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""initial example with PyQt5"""
import sys

from typing import List, Union
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
)


def qpush_button_orientation(
    box_orientation: Union[QHBoxLayout, QVBoxLayout],
    button_name: List[str]
) -> Union[QHBoxLayout, QVBoxLayout]:
    """Create buttons in a specific direction. Useful when you are creating
    more than one button wiht QPushButton function.

    Args:
        box_orientation: [QHBoxLayout, QVBoxLayout]
            Used for set box orientation.

        button_name: List[str]
            Set the name inside of button container.

    Returns:
        object: Union[QHBoxLayout, QVBoxLayout]

        The returns can appended directly on main window.

    Example:
        Creating a window and append to in some buttons.

        >>> wdw = QWidget()
        >>> wdw.setLayout(qpush_button_orientation(QVBoxLayout, ['foo', 'bar']))
    """
    layout: Union[QHBoxLayout, QVBoxLayout] = box_orientation()
    for name in button_name:
        layout.addWidget(QPushButton(name))
    return layout


app = QApplication(sys.argv)
layout = qpush_button_orientation(QVBoxLayout, ['foo', 'bar'])

window = QWidget()
window.setWindowTitle('Kappa example')
window.setLayout(layout)
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)


if __name__ == '__main__':
    window.show()
    sys.exit(app.exec_())
