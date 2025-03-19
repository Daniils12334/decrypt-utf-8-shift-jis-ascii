def xor_decrypt(data, key=0xAA):
    return bytes([b ^ key for b in data])

def try_decrypt_with_multiple_keys(file_path, keys=[0xAA, 0xFF, 0x55, 0x77]):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

            # Пробуем расшифровать с несколькими ключами
            for key in keys:
                decrypted_data = xor_decrypt(encrypted_data, key)
                print(f"Попытка с ключом {hex(key)}:")
                print(decrypted_data.decode(errors='ignore'))  # Преобразуем в строку, игнорируя ошибки
    except Exception as e:
        print(f"Ошибка: {e}")

# Путь к твоему файлу
file_path = "/home/danbar/Documents/Violated Princess　Ver1.00/www/save/file19.rpgsave"
try_decrypt_with_multiple_keys(file_path)

def xor_decrypt_and_decode(data, key=0xAA, encoding='utf-8'):
    decrypted_data = xor_decrypt(data, key)
    try:
        return decrypted_data.decode(encoding)
    except UnicodeDecodeError:
        return None  # Невозможно декодировать в этом кодировании

# Попробуем декодировать с помощью нескольких кодировок
def try_decrypt_with_multiple_encodings(file_path, keys=[0xAA, 0xFF], encodings=['utf-8', 'shift_jis']):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

            for key in keys:
                for encoding in encodings:
                    decoded_data = xor_decrypt_and_decode(encrypted_data, key, encoding)
                    if decoded_data:
                        print(f"Попытка с ключом {hex(key)} и кодировкой {encoding}:")
                        print(decoded_data)
                    else:
                        print(f"Не удалось декодировать с ключом {hex(key)} и кодировкой {encoding}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Дополнительная проверка для всех ключей и кодировок
def try_decrypt_all_combinations(file_path, keys=[0xAA, 0xFF, 0x55, 0x77], encodings=['utf-8', 'shift_jis', 'ascii']):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

            # Пробуем расшифровать с каждым ключом и кодировкой
            for key in keys:
                for encoding in encodings:
                    decrypted_data = xor_decrypt(encrypted_data, key)
                    decoded_data = xor_decrypt_and_decode(encrypted_data, key, encoding)
                    print(f"Попытка с ключом {hex(key)} и кодировкой {encoding}:")
                    if decoded_data:
                        print(decoded_data)
                    else:
                        print(f"Не удалось декодировать с ключом {hex(key)} и кодировкой {encoding}")
    except Exception as e:
        print(f"Ошибка: {e}")

# Пробуем все возможные комбинации
try_decrypt_all_combinations(file_path)

def filter_mostly_printable(data):
    # Преобразуем байты в текст и фильтруем те, которые не являются печатными символами
    return ''.join([chr(b) if 32 <= b <= 126 else ' ' for b in data])

def try_decrypt_with_cleaning(file_path, keys=[0xAA, 0xFF, 0x55, 0x77], encodings=['utf-8', 'shift_jis']):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

            for key in keys:
                decrypted_data = xor_decrypt(encrypted_data, key)
                print(f"Попытка с ключом {hex(key)}:")

                # Преобразуем расшифрованные данные в текст с фильтрацией
                filtered_data = filter_mostly_printable(decrypted_data)
                decoded_data = xor_decrypt_and_decode(encrypted_data, key)

                if decoded_data:
                    print(f"Декодировано с ключом {hex(key)}:\n{decoded_data}")
                else:
                    print(f"Не удалось декодировать с ключом {hex(key)}.")
                print(f"Очищенные данные:\n{filtered_data}")

    except Exception as e:
        print(f"Ошибка: {e}")

# Пробуем расшифровку с фильтрацией
try_decrypt_with_cleaning(file_path)


try_decrypt_with_multiple_encodings(file_path)
