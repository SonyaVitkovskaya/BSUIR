import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import tracemalloc
import psutil
import os

tracemalloc.start()

key = Fernet.generate_key()
cipher = Fernet(key)

data_store = {
    "confidential": {},  
    "non_confidential": {} 
}

def add_data():
    key = entry_key.get()
    value = entry_value.get()
    is_confidential = var_confidential.get()

    if not key or not value:
        messagebox.showerror("Ошибка", "Ключ и значение не могут быть пустыми!")
        return

    if is_confidential:
        encrypted_value = cipher.encrypt(value.encode())
        data_store["confidential"][key] = encrypted_value
    else:
        data_store["non_confidential"][key] = value

    update_display()
    clear_entries()

def update_data():
    key = entry_key.get()
    value = entry_value.get()
    is_confidential = var_confidential.get()

    if not key or not value:
        messagebox.showerror("Ошибка", "Ключ и значение не могут быть пустыми!")
        return

    if is_confidential:
        if key in data_store["confidential"]:
            encrypted_value = cipher.encrypt(value.encode())
            data_store["confidential"][key] = encrypted_value
        else:
            messagebox.showerror("Ошибка", "Ключ не найден в конфиденциальных данных!")
    else:
        if key in data_store["non_confidential"]:
            data_store["non_confidential"][key] = value
        else:
            messagebox.showerror("Ошибка", "Ключ не найден в неконфиденциальных данных!")

    update_display()
    clear_entries()

def delete_data():
    key = entry_key.get()
    is_confidential = var_confidential.get()

    if not key:
        messagebox.showerror("Ошибка", "Ключ не может быть пустым!")
        return

    if is_confidential:
        if key in data_store["confidential"]:
            del data_store["confidential"][key]
        else:
            messagebox.showerror("Ошибка", "Ключ не найден в конфиденциальных данных!")
    else:
        if key in data_store["non_confidential"]:
            del data_store["non_confidential"][key]
        else:
            messagebox.showerror("Ошибка", "Ключ не найден в неконфиденциальных данных!")

    update_display()
    clear_entries()

def update_display():
    text_display.delete(1.0, tk.END)
    text_display.insert(tk.END, "Неконфиденциальные данные:\n")
    for key, value in data_store["non_confidential"].items():
        text_display.insert(tk.END, f"{key}: {value}\n")

    text_display.insert(tk.END, "\nКонфиденциальные данные:\n")
    for key, value in data_store["confidential"].items():
        text_display.insert(tk.END, f"{key}: [Зашифровано]\n")

def clear_entries():
    entry_key.delete(0, tk.END)
    entry_value.delete(0, tk.END)
    var_confidential.set(False)

import time
import tracemalloc
import psutil

# Функция для измерения времени
def measure_time_and_memory(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.time()
    func(*args, **kwargs)  # Выполнение функции
    elapsed_time = time.time() - start_time
    snapshot = tracemalloc.take_snapshot()
    tracemalloc.stop()
    memory_info = snapshot.statistics('lineno')
    process = psutil.Process()
    memory_usage = process.memory_info().rss
    print(f"Время выполнения: {elapsed_time:.4f} секунд")
    print(f"Использование памяти (RSS): {memory_usage / 1024 / 1024:.2f} МБ")
    print("Топ строк памяти:")
    for stat in memory_info[:10]:
        print(stat)

# Пример вызова



"""def create_memory_dump(filename):
    process = psutil.Process(os.getpid())

    with open(filename, "w", encoding="utf-8") as dump_file:  
        dump_file.write(f"Использование памяти (RSS): {process.memory_info().rss} байт\n")
        dump_file.write("Содержимое оперативной памяти:\n")
        dump_file.write(str(data_store))
        take_dump = dump_memory()
        for elem in take_dump:
            dump_file.write(elem + '\n')

def dump_memory():
    tracemalloc.start()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno') 
    tracemalloc.stop()
    result = [f"{'=' * 5} TOP STATS {'=' * 5}"]
    result.extend(list(map(str, top_stats[:10])))
    result.append(f"{'=' * 5} TOP DIFFS {'=' * 5}")
    return result"""

initial_snapshot = None

def create_memory_dump(filename):
    global initial_snapshot

    process = psutil.Process(os.getpid())
    with open(filename, "w", encoding="utf-8") as dump_file:
        dump_file.write(f"Использование памяти (RSS): {process.memory_info().rss} байт\n")
        
        dump_file.write("Содержимое оперативной памяти:\n")
        dump_file.write(str(data_store) + "\n")
        
        if initial_snapshot is None:
            tracemalloc.start()
            initial_snapshot = tracemalloc.take_snapshot()
            dump_file.write("===== INITIAL MEMORY SNAPSHOT =====\n")
            top_stats = initial_snapshot.statistics('lineno')
            dump_file.write(format_top_stats(top_stats))
        else:
            current_snapshot = tracemalloc.take_snapshot()
            diff = current_snapshot.compare_to(initial_snapshot, 'lineno')
            dump_file.write("===== MEMORY USAGE CHANGES =====\n")
            dump_file.write(format_top_stats(diff))
            initial_snapshot = current_snapshot

def format_top_stats(stats):
    result = []
    for stat in stats[:10]: 
        result.append(f"{stat.traceback.format()}: size={stat.size} B, count={stat.count}, average={stat.size // stat.count} B")
    return "\n".join(result) + "\n"


root = tk.Tk()
root.title("Управление данными")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Ключ:").grid(row=0, column=0, padx=5)
entry_key = tk.Entry(frame_input)
entry_key.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Значение:").grid(row=1, column=0, padx=5)
entry_value = tk.Entry(frame_input)
entry_value.grid(row=1, column=1, padx=5)

var_confidential = tk.BooleanVar()
check_confidential = tk.Checkbutton(frame_input, text="Конфиденциальные данные", variable=var_confidential)
check_confidential.grid(row=2, columnspan=2)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Добавить", command=add_data)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="Обновить", command=update_data)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Удалить", command=delete_data)
btn_delete.grid(row=0, column=2, padx=5)

btn_dump = tk.Button(frame_buttons, text="Дамп", command=lambda: create_memory_dump("memory_dump.txt"))
btn_dump.grid(row=0, column=3, padx=5)

text_display = tk.Text(root, width=50, height=15)
text_display.pack(pady=10)

#update_display()
#root.mainloop()


measure_time_and_memory(create_memory_dump, "memory_dump.txt")