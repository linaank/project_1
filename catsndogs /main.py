# загружаем библиотеку и меседжбокс из нее
import tkinter as tk
from tkinter import messagebox

# ввод главных переменных
current_player = 'cat' # всегда стартует кот
board = [''] * 9 # доска 3х3

# проверка победы и победные комбинации
def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '':
            return combo
    return None

# процесс обработки нажатия на клетку поля
# определение текущего игрока, проверка клетки на пустоту, проверка наличия победной комбинации на поле - выведение инфы о победе и последующий сброс
def check_draw():
    return all(cell != '' for cell in board)

def button_click(index):
    global current_player
    if board[index] == '':
        board[index] = 'cat' if current_player == 'cat' else 'dog'
        buttons[index].config(text='🐱' if current_player == 'cat' else '🐶')
        winner_combo = check_winner()

# случай победы vs случай ничьи

        # проверка наличия выигрышной комбинации
        if winner_combo:
            highlight_winner(winner_combo)
            messagebox.showinfo("Ура победа!", "Замурррчательно!")
            reset_game()

        # проверка наличия ничьи
        elif check_draw():
            messagebox.showinfo("Давай по новой!", "Ничейная собачья грусть..")
            reset_game()
        # смена игрока с собаки на кошку и наоборот. if текущий игрок был собачкой, то после выполнения строки он станет кошечкой, наоборот тоже
        current_player = 'dog' if current_player == 'cat' else 'cat'

# подсвечиваем выигрышное комбо милым розовым
def highlight_winner(combo):
    for index in combo:
        buttons[index].config(bg='pink')

# сброс игры
def reset_game():
    global board, current_player
    board = [''] * 9
    current_player = 'cat'
    # измененяю свойства button: текст задали в пустую строку, фон как 'SystemButtonFace'
    for button in buttons:

        button.config(text='', bg='SystemButtonFace')

# main игровое окно
root = tk.Tk()
root.title("Кошечки-Собачки")

# создание граф интерфейса с помощью tk
buttons = []
for i in range(9):
    button = tk.Button(root, text='', font=('Arial', 40), width=5, height=2,
                       command=lambda index=i: button_click(index))
# определение строки и столбца, в которую разместится кнопка 
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

root.mainloop()
# играем мурчим кайфуем
# предпочла длинному коду тот, что покороче, зато визуал приятнее
