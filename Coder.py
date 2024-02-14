import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint

from CoderUi import Ui_MainWindow

ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
EXTRA_SYMBOLS = list(".,!?@#$%:*")
POLYBIUS_ALPHABET = [[(ALPHABET + EXTRA_SYMBOLS)[j] for j in range(i * 6, i * 6 + 6)] for i in range(6)]
ROW_LEN = len(POLYBIUS_ALPHABET[0])
COLUMN_LEN = len(POLYBIUS_ALPHABET)


def caesar_encrypt(line_to_encrypt, shift):
    encrypted_line = ""
    for i in line_to_encrypt:
        if i.isalpha() == 0:
            encrypted_line += i
        if i.isupper():
            encrypted_line += ALPHABET[(ALPHABET.index(i.lower()) + shift) % 26].upper()
        else:
            encrypted_line += ALPHABET[(ALPHABET.index(i) + shift) % 26]
    return encrypted_line


def caesar_decrypt(line_to_decrypt, shift):
    decrypted_line = ""
    for i in line_to_decrypt:
        if i.isalpha() == 0:
            decrypted_line += i
        if i.isupper():
            decrypted_line += ALPHABET[(ALPHABET.index(i.lower()) - shift) % 26].upper()
        else:
            decrypted_line += ALPHABET[(ALPHABET.index(i) - shift) % 26]
    return decrypted_line


def vigenere_encrypt(line_to_encrypt, key):
    extra_key = key
    encrypted_line = ""
    if len(line_to_encrypt) != len(key):
        while len(key) < len(line_to_encrypt):
            key += extra_key
    for i in range(len(line_to_encrypt)):
        encrypted_line += ALPHABET[((ALPHABET.index(line_to_encrypt[i]) + ALPHABET.index(key[i])) % 26)]
    return encrypted_line


def vigenere_decrypt(line_to_decrypt, key):
    extra_key = key
    encrypted_line = ""
    if len(line_to_decrypt) != len(key):
        while len(key) < len(line_to_decrypt):
            key += extra_key
    for i in range(len(line_to_decrypt)):
        encrypted_line += ALPHABET[((ALPHABET.index(line_to_decrypt[i]) - ALPHABET.index(key[i])) % 26)]
    return encrypted_line


def polybius_encrypt(line_to_encrypt, shift=0):
    encrypted_line = []
    for i in list(map(lambda symbol: symbol.lower(), line_to_encrypt)):
        for column in range(COLUMN_LEN):
            for row in range(ROW_LEN):
                if i == POLYBIUS_ALPHABET[column][row]:
                    y = (column + shift) % COLUMN_LEN
                    x = (row + shift) % ROW_LEN
                    y = COLUMN_LEN + y if y < 0 else y
                    x = ROW_LEN + x if x < 0 else x
                    encrypted_line.append(f"{y}{x}")
                    break
    return ' '.join(encrypted_line)


def polybius_decrypt(line_to_decrypt, shift=0):
    decrypted_line = ""
    for i in line_to_decrypt.split():
        column, row = (int(i[0]) - shift) % COLUMN_LEN, (int(i[1]) - shift) % ROW_LEN
        column, row = COLUMN_LEN + column if column < 0 else column, ROW_LEN + row if row < 0 else row
        decrypted_line += POLYBIUS_ALPHABET[column][row]
    return decrypted_line


def yaroslav_polybius_encrypt(line_to_encrypt):
    encrypted_line = []
    for i in list(map(lambda symbol: symbol.lower(), line_to_encrypt)):
        for column in range(COLUMN_LEN):
            for row in range(ROW_LEN):
                if i == POLYBIUS_ALPHABET[column][row]:
                    shift = randint(1, 9)
                    y = (column + shift) % COLUMN_LEN
                    x = (row + shift) % ROW_LEN
                    y = COLUMN_LEN + y if y < 0 else y
                    x = ROW_LEN + x if x < 0 else x
                    encrypted_line.append(f"{x}{y}{shift}")
                    break
    return encrypted_line


def yaroslav_polybius_decrypt(line_to_decrypt, shifts):
    decrypted_line = ""
    for i, v in enumerate(line_to_decrypt):
        shift = shifts[i]
        column, row = (int(v[0]) - shift) % COLUMN_LEN, (int(v[1]) - shift) % ROW_LEN
        column, row = COLUMN_LEN + column if column < 0 else column, ROW_LEN + row if row < 0 else row
        decrypted_line += POLYBIUS_ALPHABET[column][row]
    return decrypted_line


def yaroslav_encrypt(line_to_encrypt):
    encrypted_line = yaroslav_polybius_encrypt(line_to_encrypt)
    ranges = (1, 2, 3, 4, 5)
    step = (1, 2, 3, 4, 5)
    step_count = 0
    cnt = 0
    final_message = ''
    for line in encrypted_line:
        final_message += line + f'{"".join([str(randint(1, 9)) for _ in range(ranges[cnt])])}'
        cnt += step[step_count]
        if cnt > 4:
            step_count = (step_count + 1) % 5
            cnt = cnt % 5
    return final_message


def yaroslav_decrypt(message_to_decrypt):
    line = message_to_decrypt
    ranges = (1, 2, 3, 4, 5)
    step = (1, 2, 3, 4, 5)
    step_count = 0
    cnt = 0
    start = 0
    decrypted = ''
    while start < len(line):
        letter = line[start: start + 3]
        decrypted += polybius_decrypt(letter[1] + letter[0], int(letter[2]))
        start += ranges[cnt] + 3
        cnt += step[step_count]
        if cnt > 4:
            step_count = (step_count + 1) % 5
            cnt = cnt % 5
    return decrypted


class Coder(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encryptButton.clicked.connect(self.encrypt)
        self.encryptButton_2.clicked.connect(self.encrypt)
        self.encryptButton_3.clicked.connect(self.encrypt)
        self.encryptButton_4.clicked.connect(self.encrypt)
        self.decryptButton.clicked.connect(self.decrypt)
        self.decryptButton_2.clicked.connect(self.decrypt)
        self.decryptButton_3.clicked.connect(self.decrypt)
        self.decryptButton_4.clicked.connect(self.decrypt)

    def encrypt(self):
        current_tab = self.tabWidget.currentIndex()
        if current_tab == 0:
            text = self.message.text()
            key = self.key.text()
            if text != "" and all([let in ALPHABET for let in text]):
                if key != '' and all([let in ALPHABET for let in key]):
                    encrypted = vigenere_encrypt(text, key)
                    self.result.setText(encrypted)
                else:
                    self.statusbar.showMessage("Неверный формат ключа!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 1:
            text = self.message_2.text()
            shift = self.shift.text()
            if text != "" and all([let in ALPHABET for let in text]):
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
                    self.statusbar.showMessage("Вы не ввели сдвиг!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        else:
            text = self.message_4.text()
            if text != "" and all([let in ALPHABET for let in text]):
                encrypted_message = yaroslav_encrypt(text)
                self.result_4.setText(encrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")

    def decrypt(self):
        current_tab = self.tabWidget.currentIndex()
        if current_tab == 0:
            text = self.message.text()
            if text != "" and all([let in ALPHABET for let in text]):
                key = self.key.text().lower()
                if key != '' and all([let in ALPHABET for let in key]):
                    decrypted = vigenere_decrypt(text, key)
                    self.result.setText(decrypted)
                else:
                    self.statusbar.showMessage("Неверный формат ключа!")
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")
        elif current_tab == 1:
            text = self.message_2.text()
            if text != "" and all([let in ALPHABET for let in text]):
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
        else:
            message = self.message_4.text()
            if message.isdigit():
                decrypted_message = yaroslav_decrypt(message)
                self.result_4.setText(decrypted_message)
            else:
                self.statusbar.showMessage("Неверный формат сообщения!")


def my_excepthook(type, value, tback):
    sys.__excepthook__(type, value, tback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coder()
    sys.excepthook = my_excepthook
    ex.show()
    sys.exit(app.exec_())