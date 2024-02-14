from tkinter import *
from tkinter import font
import os as os
import numpy as np
import random

class Reg:

    def StartGame(self): #Создаём окно с игровым полем и открываем его
        self.root.destroy() #Закрываем лишние окна
        self.start.destroy()
        Game()     

    def Autorize(self):
        font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
        if os.path.exists("register.txt"):
            file = open("register.txt", "r+") #Открываем файл с данными пользователей
            if not (self.login.get() or self.password.get()):
                self.message["text"] = "Заполните все поля!"
            else:
                if (self.login.get() and self.password.get()) in file.read().split(): #Если введённые данные уже есть
                    self.start = Tk()
                    self.start.title("Начать игру")
                    self.start.geometry("300x100")
                    self.start.configure(background="#F8F8FF")
                    message = Label(master=self.start, anchor=W, bg="#F8F8FF", text="Вы успешно авторизовались!", font=font1)  #Авторизуем пользователя
                    message.pack(padx=6, pady=6)
                    btn = Button(master=self.start, text="Начать игру", anchor=W, bg="#6A5ACD", fg="#FFFFFF", font=font1, command=self.StartGame)
                    btn.pack(padx=6, pady=6) 
                    self.start.mainloop()
                else:
                    self.message["text"] = "Неверный логин или пароль!"
        else:  #Если данные введены впервые (файл данных пользователя отсутствует)
            self.message["text"] = "Неверный логин или пароль!"

    def Register(self):
        if self.login.get()=='' or self.password.get()=='':
            self.message["text"] = "Заполните все поля!"
        elif os.path.exists("register.txt"):
            file = open("register.txt", "r+") #Открываем файл с данными пользователей
            if self.login.get() in file.read().split(): #Если введённые данные уже есть
                self.message["text"] = "Такой пользователь уже зарегистрирован!"
            else: #Если данные введены впервые
                file.write(self.login.get() + " " + self.password.get() + "\n") #Регистрируем пользователя
                file.close()
                self.message["text"] = "Вы успешно зарегистрировались!"
        else:
            file = open("register.txt", "w") #Создаём файл с данными пользователей
            file.write(self.login.get() + " " + self.password.get() + "\n") #Регистрируем пользователя
            file.close()
            self.message["text"] = "Вы успешно зарегистрировались!"    

    def __init__(self):
        self.root = Tk()     # создаем корневой объект - окно
        self.root.title("Регистрация")     # устанавливаем заголовок окна
        self.root.geometry("500x350")    # устанавливаем размеры окна
        self.root.configure(background="#F8F8FF")
        font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
        hello = Label(font=font1, anchor=W, background="#F8F8FF", text="Добро пожаловать в игру 'Киммерийские шашки - поддавки!'\nДля продолжения авторизуйтесь") # создаем текстовую метку
        hello.pack(padx=6, pady=6)
        llogin = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш логин") # создаем текстовую метку
        llogin.pack(padx=6, pady=6) # размещаем метку в окне
        self.login=Entry(bd=2)
        self.login.pack(padx=6, pady=6)
        lpassword = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш пароль") 
        lpassword.pack(padx=6, pady=6)
        self.password=Entry(bd=2)
        self.password.pack(padx=6, pady=6)
        btn1 = Button(text="Войти", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=self.Autorize) #создаём кнопки и устанавливаем внутри окна
        btn1.pack(padx=6, pady=6) 
        plsreg = Label(font=font1, anchor=W, background="#F8F8FF", text="Нет профиля? Зарегистрируйтесь!") # создаем текстовую метку
        plsreg.pack(padx=6, pady=6)
        btn2 = Button(text="Зарегистрироваться", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=self.Register) #создаём кнопки и устанавливаем внутри окна
        btn2.pack(padx=6, pady=6)
        self.message = Label(anchor=W, bg="#F8F8FF", font=font1)
        self.message.pack(padx=6, pady=6)
        self.root.mainloop()
class Game:
        
    class Tile:

            def Create(self, i, j, canvas):
                    
                    def click(event): #клик на клетку с шашкой
                        position = canvas.coords(button_window) #получаем координаты шашки
                        print(position)
                        able_white = [key for key, value in self.white_coords.items() if value == True]
                        print("Доступные ходы")
                        print(able_white)
                        def check_step(able):
                            if able == able_white:
                                print("Белые")
                            else:
                                print("Чёрные")
                            def eliminate(len, step, coord):
                                for i in range(len-1):
                                    if able == able_white:
                                        if step[i] == -1 and step[i+1] == 0:
                                            self.priority.append(coord)
                                    else:
                                        if step[i] == 1 and step[i+1] == 0:
                                            self.priority.append(coord)

                            for coord in able:
                                x = coord[0]
                                y = coord[1]
                                diag1 = np.diag(self.pos, int(x/100)-int(y/100))
                                diag2 = np.diag(np.fliplr(self.pos), 7-(int(x/100)+int(y/100)))
                                if coord in self.king_coords:
                                    step11 = diag1[:int(y)]
                                    step12 = diag1[(-1)*int(y)+1:]
                                    step21 = diag2[:int(y)]
                                    step22 = diag2[(-1)*int(y)+1:]
                                    step11_len = len(step11)
                                    step12_len = len(step12)
                                    step21_len = len(step21)
                                    step22_len = len(step22)
                                    if step11_len >= 3:
                                        eliminate(step11_len, step11, coord)
                                    elif step12_len >= 3:
                                        eliminate(step12_len, step12, coord)
                                    elif step21_len >= 3:
                                        eliminate(step21_len, step21, coord)
                                    elif step22_len >= 3:
                                        eliminate(step22_len, step22, coord)
                                else:
                                    step11 = diag1[int(y)-2:len(diag1)-int(y)]
                                    step12 = diag1[int(x):len(diag1)-int(y)-2]
                                    step21 = diag2[int(y)-2:len(diag2)-int(y)]
                                    step22 = diag2[int(x):len(diag2)-int(y)-2]
                                    step11_len = len(step11)
                                    step12_len = len(step12)
                                    step21_len = len(step21)
                                    step22_len = len(step22)
                                    if step11_len == 2:
                                        eliminate(step11_len, step11, coord)
                                    elif step12_len == 2:
                                        eliminate(step12_len, step12, coord)
                                    elif step21_len == 2:
                                        eliminate(step21_len, step21, coord)
                                    elif step22_len == 2:
                                        eliminate(step22_len, step22, coord)
                            print("Приоритетные ходы")
                            print(self.priority)
                            if able == able_white:
                                if len(self.priority) > 0 and not ((position[0], position[1]) in self.priority) or not ((position[0], position[1]) in able):
                                    print("Ошибка!")
                                else:

                                    self.user_stepped = 1
                                    self.user_position = position
                                print(self.user_stepped)
                            else:
                                if len(self.priority) > 0:
                                    random_black = random.choice(self.priority)
                                else:
                                    random_black = random.choice(able)
                                return random_black

                        def computer_step():
                            print("Ход компьютера")
                            able_black = [key for key, value in self.black_coords.items() if value == True]
                            random_black = check_step(able_black)
                            print(random_black)
                            


                        def user_step(): #ход игрока обычной шашкой
                            print("Ход фишкой")
                            if self.pos[int(position[1]/100)][int(position[0]/100)] == 0 and position[1] == self.user_position[1]-100 and (position[0] == self.user_position[0]+100 or position[0] == self.user_position[0]-100):
                                self.tiles[int(position[0]), int(position[1])][0]["image"] = self.i1
                                self.pos[int(position[1]/100)][int(position[0]/100)] = 1
                                self.tiles[int(self.user_position[0]), int(self.user_position[1])][0]["image"] = ''
                                self.pos[int(self.user_position[1]/100)][int(self.user_position[0]/100)] = 0
                                if self.pos[int(position[1]/100)-1][int(position[0]/100)+1] == 0 or self.pos[int(position[1]/100-1)][int(position[0]/100)+1] == 0:
                                    self.white_coords[position[0], position[1]] = True
                            self.user_stepped = 0
                            print(self.pos)
                            computer_step()
                        def user_king_step():
                            print("Ход дамкой")

                            if self.pos[int(position[1]/100)][int(position[0]/100)] == 0 and abs(self.user_position[0] - position[0]) == abs(self.user_position[1] - position[1]):
                                self.tiles[int(position[0]), int(position[1])][0]["image"] = self.i2
                                self.pos[int(position[1]/100)][int(position[0]/100)] = 1
                                self.tiles[int(self.user_position[0]), int(self.user_position[1])][0]["image"] = ''
                                self.pos[int(self.user_position[1]/100)][int(self.user_position[0]/100)] = 0
                                self.user_stepped = 0
                                self.king_coords.remove(self.user_position)
                                self.king_coords.append(position)
                                computer_step()

                        if self.user_stepped == 0: 
                            if self.pos[int(position[1]/100)][int(position[0]/100)] == 1:
                                check_step(able_white)
                        elif self.user_stepped == 1: 
                            if not self.user_position in self.king_coords:
                                user_step()
                                
                            else:
                                user_king_step()
                            print(self.user_stepped)
                    if (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
                        self.tile = Button(master=canvas, width=100, height=100, bg="#000000", anchor=NW)
                    else:
                        self.tile = Button(master=canvas, width=100, height=100, bg="#FFFAFA", anchor=NW)
                        if j > 3:
                            if j==6 and (i==5 or i == 3):
                                self.tile["image"] = self.i2
                                self.king_coords.append([i*100, j*100]) #сохраняем координаты данных
                                self.white_coords[i*100, j*100] = True
                            else:
                                self.tile["image"] = self.i1  
                            if j > 0 and (i < 7 and self.pos[j-1][i+1] == 0 or i > 0 and self.pos[j-1][i-1] == 0): #Проверяем, может ли шашка совершить ход
                                self.white_coords[i*100, j*100] = True #сохраняем координаты белых шашек
                            else:
                                self.white_coords[i*100, j*100] = False
                        elif j < 3:
                            if j==0 and (i==5 or i == 3):
                                self.tile["image"] = self.i4
                                self.king_coords.append([i*100, j*100]) #сохраняем координаты данных
                                self.black_coords[i*100, j*100] = True
                            else:
                                self.tile["image"] = self.i3
                            if j < 6 and (i < 7 and self.pos[j+1][i+1] == 0 or i > 0 and self.pos[j+1][i-1] == 0): #Проверяем, может ли шашка совершить ход
                                self.black_coords[i*100, j*100] = True #сохраняем координаты чёрных шашек
                            else:
                                self.black_coords[i*100, j*100] = False
                        self.tile.bind('<Button-1>', click)   
                        self.tiles[i*100, j*100]= [self.tile]
                    button_window = canvas.create_window(i*100, j*100, anchor=NW, window=self.tile)
                    
      
    def __init__(self):
            self.pos = np.array([[0, -1, 0, -1, 0, -1, 0, -1], 
                                [-1, 0, -1, 0, -1, 0, -1, 0], 
                                [0, -1, 0, -1, 0, -1, 0, -1], 
                                [0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 1, 0, 1, 0, 1],
                                [1, 0, 1, 0, 1, 0, 1, 0],
                                [0, 1, 0, 1, 0, 1, 0, 1]])
            self.white_coords = {}
            self.black_coords = {}
            self.tiles = {}
            self.priority = []
            self.king_coords = []
            self.user_stepped = 0
            self.flag = 0
            self.game = Tk()
            self.game.title("Игра")
            self.canvas = Canvas(height=700, width=800)
            self.canvas.pack()
            self.i1=PhotoImage(file="1b.gif")
            self.i2=PhotoImage(file="1bk.gif")
            self.i3=PhotoImage(file="black.gif")
            self.i4=PhotoImage(file="black1.gif")
            for i in range(8):
                for j in range(7):
                    Game.Tile.Create(self, i, j, self.canvas)
            self.game.mainloop()   


   
Reg()
