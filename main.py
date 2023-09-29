import tkinter as tk

# Начальные параметры эллипса
initial_center_x = 200
initial_center_y = 200
initial_semi_axis_a = 100  # большая полуось
initial_semi_axis_b = 50   # малая полуось

center_x = initial_center_x
center_y = initial_center_y
semi_axis_a = initial_semi_axis_a
semi_axis_b = initial_semi_axis_b
step = 10  # Шаг изменения полуосей
colors = ['red', 'green', 'yellow']  # Список цветов для заливки
color_index = 0


def draw_ellipse():
    canvas.delete('ellipse')  # Удаление предыдущей фигуры
    canvas.create_oval(center_x - semi_axis_a, center_y - semi_axis_b,
                       center_x + semi_axis_a, center_y + semi_axis_b,
                       outline='white', fill=colors[color_index], tags='ellipse')


def on_key(event):
    global semi_axis_a, semi_axis_b, color_index
    if event.keysym == 'Left':
        semi_axis_a -= step
    elif event.keysym == 'Right':
        semi_axis_a += step
    elif event.keysym == 'Down':
        semi_axis_b -= step
    elif event.keysym == 'Up':
        semi_axis_b += step
    elif event.keysym == 'Prior':
        color_index = (color_index - 1) % len(colors)
    elif event.keysym == 'Next':
        color_index = (color_index + 1) % len(colors)
    elif event.keysym == 'Escape':
        root.quit()

    draw_ellipse()

def reset_ellipse():
    global center_x, center_y, semi_axis_a, semi_axis_b
    center_x = initial_center_x
    center_y = initial_center_y
    semi_axis_a = initial_semi_axis_a
    semi_axis_b = initial_semi_axis_b
    draw_ellipse()

root = tk.Tk()  # Создание окна
root.title("Управление эллипсом")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

draw_ellipse()

canvas.focus_set()
canvas.bind("<Key>", on_key)

reset_button = tk.Button(root, text="Сброс", command=reset_ellipse)
reset_button.pack()

root.mainloop()
