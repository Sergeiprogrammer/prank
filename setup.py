import os
import subprocess

# Команда для запуска программы
command = "python main.py"  # Убедитесь, что main.py в той же директории или укажите полный путь

# Список библиотек для установки
libraries = [
    "Pillow",   # Для работы с изображениями
    "pygame",   # Для работы с играми или мультимедиа
]

# Установка библиотек через os.system()
for lib in libraries:
    print(f"Installing {lib}...")
    os.system(f"pip install {lib}")
    print(f"{lib} installed successfully.")

# Запуск команды
process = subprocess.Popen(command, shell=True)
process.wait()  # Ждем завершения процесса (опционально)

print("All installed successfully and program started!")
