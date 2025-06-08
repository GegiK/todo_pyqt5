import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
            QHBoxLayout,QLineEdit, QPushButton,
            QListWidget, QListWidgetItem,QCheckBox, QComboBox)
from PyQt5.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To Do List')
        self.setGeometry(520, 200, 400, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText('Add new task')
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_task)
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)

        self.layout.addLayout(self.input_layout)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.bottom_layout = QHBoxLayout()
        self.filter_box = QComboBox()
        self.filter_box.addItems(["All", "Active", "Completed"])
        self.filter_box.currentIndexChanged.connect(self.apply_filter)
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_selected)
        self.bottom_layout.addWidget(self.filter_box)
        self.bottom_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.bottom_layout)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            item = QListWidgetItem()
            checkbox = QCheckBox(task_text)
            checkbox.stateChanged.connect(self.apply_filter)
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, checkbox)
            self.task_input.clear()

    def apply_filter(self):
        filter_mode = self.filter_box.currentText()
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            widget = self.task_list.itemWidget(item)
            if filter_mode == "All":
                item.setHidden(False)
            elif filter_mode == "Active":
                item.setHidden(widget.isChecked())
            elif filter_mode == "Completed":
                item.setHidden(not widget.isChecked())

    def delete_selected(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            row = self.task_list.row(item)
            widget = self.task_list.itemWidget(item)
            self.task_list.takeItem(row)
            if widget:
                widget.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())






