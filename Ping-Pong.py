from pygame import *
from random import *
from time import time as timer
win = display.set_mode((800,600))
background = transform.scale(image.load('background.jpg'), (800, 600))
FPS = 60
clock = time.Clock()
game = True
start = False
finish = False
b = 0
score1 = 0
score2 = 0
font.init()
Font1 = font.Font(None, 90)
Font2 = font.Font(None, 60)
Text3 = Font2.render('Игрок 2 получил очко!', True, (255,255,255))
Text4 = Font2.render('Игрок 1 получил очко!', True, (255,255,255))
Text7 = Font2.render('Нажмите SPACE чтобы начать!', True, (255,255,255))
class character(sprite.Sprite):
    def __init__(self, speed, width, height, color1, color2, color3, x, y, number):
        super().__init__()
        self.speed = speed
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.Image = Surface((self.width, self.height))
        self.Image.fill((self.color1, self.color2, self.color3))
        self.rect = self.Image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.number = number
    def update(self):
        win.blit(self.Image, (self.rect.x, self.rect.y))
        if key_pressed[K_w] and self.rect.y > 0 and self.number == 1:
           self.rect.y -= self.speed
        elif key_pressed[K_UP] and self.rect.y > 0 and self.number == 2:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 450 and self.number == 1:
           self.rect.y += self.speed
        elif key_pressed[K_DOWN] and self.rect.y < 450 and self.number == 2:
           self.rect.y += self.speed
class Ball(sprite.Sprite):
    def __init__(self, speed, speed2, x, y, Image, direction):
        super().__init__()
        self.speed = speed
        self.speed2 = speed2
        self.Image = transform.scale(image.load(Image), (75, 75))
        self.rect = self.Image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
    def update(self):
        win.blit(self.Image, (self.rect.x, self.rect.y))
    def move(self):
        if self.direction == 1:
            self.rect.x -= self.speed
            self.rect.y += self.speed2
        elif self.direction == 2:
            self.rect.x += self.speed
            self.rect.y += self.speed2
        if self.rect.y <= 0:
            self.speed2 = self.speed2 * -1
        elif self.rect.y >= 530:
            self.speed2 = self.speed2 * -1
        if self.rect.x <= 0:
            self.rect.x = 360
            self.rect.y = 200
            self.speed = 0
            self.speed2 = 0
            global start
            global score2
            global b
            start = False
            b = 1
            score2 += 1
            self.direction = randint(1, 2)
            self.speed = randint(5, 7)
            self.speed2 = randint(-5, 5)
        elif self.rect.x >= 700:
            self.rect.x = 360
            self.rect.y = 200
            self.speed = 0
            self.speed2 = 0
            start = False
            b = 2
            global score1
            score1 += 1
            self.direction = randint(1, 2)
            self.speed = randint(5, 7)
            self.speed2 = randint(-5, 5)
    def change_dir1(self):
        self.direction = 2
        self.speed = randint(5, 7)
        self.speed2 = randint(-5, 5)
        print(self.direction)
    def change_dir2(self):
        self.direction = 1
        self.speed = randint(5, 7)
        self.speed2 = randint(-5, 5)
        print(self.direction)
player = character(5, 20, 150, 0, 255, 0, 100, 100, 1) # порядок - 1) скорость, 2) длина, 3) высота, 4) цвет 1 (RGB), 5) цвет 2 (RGB), 6) цвет 3 (RGB), 7) x, 8) y,  9) порядок
player2 = character(5, 20, 150, 0, 255, 0, 700, 100, 2) # порядок - 1) скорость, 2) длина, 3) высота, 4) цвет 1 (RGB), 5) цвет 2 (RGB), 6) цвет 3 (RGB), 7) x, 8) y, 9) порядок
ball = Ball(5, 0, 360, 200, 'ball.png', randint(1, 2))
while game:
    key_pressed = key.get_pressed()
    clock.tick(FPS)
    win.blit(background, (0,0))
    player.update()
    player2.update()
    ball.update()
    Text1 = Font1.render('Score: ' + str(score1), True, (255,255,255))
    Text2 = Font1.render('Score: ' + str(score2), True, (255,255,255))
    win.blit(Text1, (0,0))
    win.blit(Text2, (560,0))
    if sprite.collide_rect(player, ball):
        ball.change_dir1()
    if sprite.collide_rect(player2, ball):
        ball.change_dir2()
    if key_pressed[K_SPACE] and start == False and not finish:
        start = True
    if start == True:
        ball.move()
    if start == False and not finish:
        win.blit(Text7, (100,200))
        if b == 1:
            win.blit(Text4, (0,50))
        elif b == 2:
            win.blit(Text3, (330,50))
    if score1 >= 5:
        start = False
        finish = True
        Text5 = Font2.render('Игрок 1 выиграл!', True, (255,255,255))
        Text6 = Font2.render('Игрок 2 проиграл!', True, (255,255,255))
        win.blit(Text5, (0,110))
        win.blit(Text6, (430,1510))
    elif score2 >= 5:
        start = False
        finish = True
        Text5 = Font2.render('Игрок 1 проиграл!', True, (255,255,255))
        Text6 = Font2.render('Игрок 2 выиграл!', True, (255,255,255))
        win.blit(Text5, (0,110))
        win.blit(Text6, (430,110))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()