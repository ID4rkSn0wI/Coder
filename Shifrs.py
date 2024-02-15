ENGLISH_ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
RUSSIAN_ALPHABET = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
EXTRA_SYMBOLS = list(".,!?@#$%:*")
POLYBIUS_ALPHABET = [[(ENGLISH_ALPHABET + EXTRA_SYMBOLS)[j] for j in range(i * 6, i * 6 + 6)] for i in range(6)]
ROW_LEN = len(POLYBIUS_ALPHABET[0])
COLUMN_LEN = len(POLYBIUS_ALPHABET)


def caesar_encrypt(line_to_encrypt, shift):
    encrypted_line = ""
    for i in line_to_encrypt:
        if i.isalpha() == 0:
            encrypted_line += i
        if i.isupper():
            encrypted_line += ENGLISH_ALPHABET[(ENGLISH_ALPHABET.index(i.lower()) + shift) % 26].upper()
        else:
            encrypted_line += ENGLISH_ALPHABET[(ENGLISH_ALPHABET.index(i) + shift) % 26]
    return encrypted_line


def caesar_decrypt(line_to_decrypt, shift):
    decrypted_line = ""
    for i in line_to_decrypt:
        if i.isalpha() == 0:
            decrypted_line += i
        if i.isupper():
            decrypted_line += ENGLISH_ALPHABET[(ENGLISH_ALPHABET.index(i.lower()) - shift) % 26].upper()
        else:
            decrypted_line += ENGLISH_ALPHABET[(ENGLISH_ALPHABET.index(i) - shift) % 26]
    return decrypted_line


def vigenere_encrypt(line_to_encrypt, key):
    extra_key = key
    encrypted_line = ""
    if len(line_to_encrypt) != len(key):
        while len(key) < len(line_to_encrypt):
            key += extra_key
    for i in range(len(line_to_encrypt)):
        encrypted_line += ENGLISH_ALPHABET[((ENGLISH_ALPHABET.index(line_to_encrypt[i]) + ENGLISH_ALPHABET.index(key[i])) % 26)]
    return encrypted_line


def vigenere_decrypt(line_to_decrypt, key):
    extra_key = key
    encrypted_line = ""
    if len(line_to_decrypt) != len(key):
        while len(key) < len(line_to_decrypt):
            key += extra_key
    for i in range(len(line_to_decrypt)):
        encrypted_line += ENGLISH_ALPHABET[((ENGLISH_ALPHABET.index(line_to_decrypt[i]) - ENGLISH_ALPHABET.index(key[i])) % 26)]
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


def encrypt_katya(s):
    k = s[::-1]
    alf = RUSSIAN_ALPHABET
    h = ''
    for q in range(0, len(s)):
        for j in range(len(alf)):
            if k[q] == alf[j]:
                alf2 = alf[j:] + alf[:j]
        for z in range(0, len(alf)):
            if s[q] == alf2[z]:
                h += str(alf[z]) + alf2[-1] + ' '
    return h


def decrypt_katya(s):
    res = ''
    alf = RUSSIAN_ALPHABET
    s = s.split()
    if res == '':
        for i in s:
            q = i[0]
            w = i[1]
            for j in range(len(alf)):
                if q == alf[j]:
                    rs = j
            for t in range(len(alf)):
                if alf[t] == w:
                    al = alf[t+1:] + alf[:t+1]
            res += al[rs]
    return res


def encrypt_and_decrypt_anna(text, shift):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    lent = len(text)
    stra = ''
    for i in range(lent):
        stroka = (shift + i - alphabet.index(text[i]) + 26) % 26
        stra += alphabet[stroka]
    return stra
