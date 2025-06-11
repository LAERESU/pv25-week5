import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QComboBox, QPushButton, QVBoxLayout, QFormLayout, QMessageBox, QShortcut
)
from PyQt5.QtGui import QKeySequence

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation App - Yusril Ibtida Ramdhani | F1D022102")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # Input Fields
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.age_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 999 9999 9999;_")
        self.address_input = QTextEdit()
        self.gender_input = QComboBox()
        self.gender_input.addItems(["--Select--", "Male", "Female"])
        self.education_input = QComboBox()
        self.education_input.addItems(["--Select--", "SD", "SMP", "SMA", "Kuliah"])

        form_layout.addRow("Name", self.name_input)
        form_layout.addRow("Email", self.email_input)
        form_layout.addRow("Age", self.age_input)
        form_layout.addRow("Phone", self.phone_input)
        form_layout.addRow("Address", self.address_input)
        form_layout.addRow("Gender", self.gender_input)
        form_layout.addRow("Education", self.education_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)

        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

        layout.addLayout(form_layout)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().replace(" ", "")
        address = self.address_input.toPlainText().strip()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        if not name:
            return self.show_warning("Name is required.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return self.show_warning("Email format is invalid.")
        if not age.isdigit():
            return self.show_warning("Age must be a number.")
        if int(age) < 10:  # Extra rule
            return self.show_warning("Age must be at least 10 years old.")
        if len(phone) < 13:
            return self.show_warning("Phone number must be 13 digits.")
        if not address:
            return self.show_warning("Address is required.")
        if gender == "--Select--":
            return self.show_warning("Please select a gender.")
        if education == "--Select--":
            return self.show_warning("Please select education level.")

        QMessageBox.information(self, "Success", "Form submitted successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
