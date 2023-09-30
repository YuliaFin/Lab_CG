import unittest
import tkinter as tk
from tkinter import Canvas
from main import draw_ellipse


class TestEllipseProgram(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def tearDown(self):
        self.root.destroy()

    def test_initial_ellipse_position(self):
        # Проверка начального положения эллипса
        ellipse = self.canvas.create_oval(150, 150, 250, 250, fill="blue")
        coords = self.canvas.coords(ellipse)
        self.assertEqual(coords, [150.0, 150.0, 250.0, 250.0])
    def test_change_color(self):
        # Проверка смены цвета эллипса
        ellipse = self.canvas.create_oval(150, 150, 250, 250, fill="blue")

        # Имитируем действие пользователя
        self.canvas.itemconfig(ellipse, fill="green")

        # Получаем новый цвет эллипса после действия пользователя
        new_color = self.canvas.itemcget(ellipse, "fill")

        # Проверяем, что цвет изменился
        self.assertNotEqual(new_color, "blue")


if __name__ == '__main__':
    unittest.main()
