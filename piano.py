import pygame
import sys
import os

# مقداردهی اولیه
pygame.init()
clock = pygame.time.Clock()

# ابعاد صفحه
Screen_Width = 800
Screen_Heigth = 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

border_width = 3
# ابعاد مربع‌ها
square_size = Screen_Heigth/3

# default mode is piano
mode = 'piano'
# نت‌های موسیقی
notes = os.listdir(f"topics/{mode}")
# دکمه ها
button_width = Screen_Width // 8
button_height = Screen_Heigth
buttons = [(i * button_width, 0, button_width, button_height)
           for i in range(8)]


# کلاس مربع


class Square:
    def __init__(self, x, y, note, color, textColor):
        self.x = x
        self.y = y
        self.width = square_size
        self.height = Screen_Heigth
        self.note = note[:-4]  # حذف .wav از اسم فایل
        self.font = pygame.font.Font(None, 24)
        self.color = color  # رنگ کلاویه‌ها به صورت متناوب سفید و مشکی
        self.textColor = textColor

    def draw(self):
        # pygame.draw.rect(screen, BLACK, button_rect, 2)

        pygame.draw.rect(screen, self.color, (
                         self.x, self.y, self.width-2, self.height-2))

        text = self.font.render(self.note, True, self.textColor)

        screen.blit(text, (self.x + self.width // 2 - text.get_width() //
                    2, self.y + self.height // 2 - text.get_height() // 2))

    def play(self):
        pygame.mixer.Sound(f"topics/{mode}/{self.note}.mp3").play()


class player :
   def __init__(self) -> None: pass
       
       
   def play(note, mode):
       pygame.mixer.Sound(f"topics/{mode}/{note}.mp3").play()


# ایجاد مربع‌ها با نت‌های به ترتیب
squares = [Square(i * square_size, 0, note, WHITE, BLACK)
           for i, note in enumerate(notes)]

# ایجاد صفحه
screen = pygame.display.set_mode((Screen_Width, Screen_Heigth))
pygame.display.set_caption("پیانو ساده")

# حلقه بی‌نهایت
while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:  # click x(exit) icon
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :  # just while key is down --> play sound
            key = event.dict.get('key')
            # key notes --> Start
            if key == 49 :  # key 1
                 player.play('do', mode)
            elif key == 50 :  # key 2
                 player.play('re', mode)
            elif key == 51 :  # key 3
                 player.play('mi', mode)
            elif key == 52 :  # key 4
                 player.play('fa', mode)
            elif key == 53 :  # key 5
                 player.play('sol', mode)
            elif key == 54 :  # key 6
                 player.play('la', mode)
            elif key == 55 :  # key 7
                 player.play('si', mode)
            elif key == 56 :  # key 8
                 player.play('do2', mode)
            # key notes --> End
            # key modes --> Start
            elif key == 1073741913:  # key 1 numpad
                # change mode to Piano
                mode = 'piano'
                break
            elif key == 1073741914:  # key 2 numpad
                mode = 'guitar'
                break
            elif key == 1073741915:  # key 3 numpad
                mode = 'flute'
                break
            elif key == 1073741916:  # key 3 numpad
                mode = 'xilofono'
                break
            elif key == 1073741917:  # key 3 numpad
                mode = 'xilofono2'
                break
            #  key modes --> End
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for square in squares:
                if square.x < x < square.x + square.width and square.y < y < square.y + square.height:
                    square.play()

    # نمایش مربع‌ها
    screen.fill(BLACK)
    for square in squares:
        square.draw()

    # آپدیت صفحه
    pygame.display.flip()
    clock.tick(30)
