import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint
from Shifrs import *
from CoderUi import Ui_MainWindow


class Coder(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encryptButton.clicked.connect(self.encrypt)
        self.encryptButton_2.clicked.connect(self.encrypt)
        self.encryptButton_3.clicked.connect(self.encrypt)
        self.encryptButton_4.clicked.connect(self.encrypt)
        self.encryptButton_5.clicked.connect(self.encrypt)
        self.encryptButton_6.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.decryptButton_2.clicked.connect(self.decrypt)
        self.decryptButton_3.clicked.connect(self.decrypt)
        self.decryptButton_4.clicked.connect(self.decrypt)
        self.decryptButton_5.clicked.connect(self.decrypt)
        self.decryptButton_6.clicked.connect(self.decrypt)

    def encrypt(self):
        self.statusbar.showMessage("")
        current_tab = self.tabWidget.currentIndex()
        if current_tab == 0:
            text = self.message.text()
            key = self.key.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                if key != '' and all([let in ENGLISH_ALPHABET for let in key]):
                    encrypted = vigenere_encrypt(text, key)
                    self.result.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат ключа!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 1:
            text = self.message_2.text()
            shift = self.shift.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                if shift != '' and shift.isdigit():
                    encrypted = caesar_encrypt(text, int(shift))
                    self.result_2.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 2:
            text = self.message_3.text()
            shift = self.shift_2.text()
            if text != "":
                if shift != '' and shift.isdigit():
                    encrypted = polybius_encrypt(text, int(shift))
                    self.result_3.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 3:
            text = self.message_4.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                encrypted_message = yaroslav_encrypt(text)
                self.result_4.setText(encrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 4:
            text = self.message_5.text()
            if text != "" and all([b in RUSSIAN_ALPHABET for b in text]):
                encrypted_message = str(encrypt_katya(text))
                self.result_5.setText(encrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 5:
            text = self.message_6.text()
            shift = self.shift_3.text()
            if text != "":
                if shift != '' and shift.isdigit():
                    encrypted = encrypt_and_decrypt_anna(text, int(shift))
                    self.result_6.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 6:
            text = self.message_7.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                encrypted_message = yaroslav_encrypt(text)
                self.result_7.setText(encrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")

    def decrypt(self):
        self.statusbar.showMessage("")
        current_tab = self.tabWidget.currentIndex()
        if current_tab == 0:
            text = self.message.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                key = self.key.text().lower()
                if key != '' and all([let in ENGLISH_ALPHABET for let in key]):
                    decrypted = vigenere_decrypt(text, key)
                    self.result.setText(decrypted)
                else:
                    self.statusbar.showMessage("Неверный формат ключа!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 1:
            text = self.message_2.text()
            if text != "" and all([let in ENGLISH_ALPHABET for let in text]):
                shift = self.shift.text()
                if shift != '' and shift.isdigit():
                    decrypted = caesar_decrypt(text, int(shift))
                    self.result_2.setText(decrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 2:
            text = self.message_3.text()
            shift = self.shift_2.text()
            if text != "":
                if shift != '' and shift.isdigit():
                    decrypted = polybius_decrypt(text, int(shift))
                    self.result_3.setText(decrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 3:
            text = self.message_4.text()
            if text.isdigit():
                decrypted_message = decrypt_katya(text)
                self.result_4.setText(decrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 4:
            text = self.message_5.text()
            if text and all([all([a in RUSSIAN_ALPHABET for a in b]) for b in text.split()]):
                decrypted_message = decrypt_katya(text)
                self.result_5.setText(decrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 5:
            text = self.message_6.text()
            shift = self.shift_3.text()
            if text != "":
                if shift != '' and shift.isdigit():
                    encrypted = encrypt_and_decrypt_anna(text, int(shift))
                    self.result_6.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат сдвига!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 6:
            message = self.message_7.text()
            if message.isdigit():
                decrypted_message = yaroslav_decrypt(message)
                self.result_7.setText(decrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coder()
    ex.show()
    sys.exit(app.exec_())