import pygame
import sys
import os

from setting import Settings
# مقداردهی اولیه
pygame.init()
clock = pygame.time.Clock()

# ابعاد صفحه
ai_settings = Settings()

border_width = 3
# ابعاد مربع‌ها
square_size = ai_settings.Screen_Heigth/3.56

# default mode is piano
mode = 'piano'
# نت‌های موسیقی
notes = os.listdir(f"topics/{mode}")
# دکمه ها
button_width = ai_settings.Screen_Width // 8
button_height = ai_settings.Screen_Heigth
buttons = [(i * button_width, 0, button_width, button_height)
           for i in range(8)]

dictNotes = {
    'do': '1_do',
    're': '2_re',
    'mi': '3_mi',
    'fa': '4_fa',
    'so': '5_so',
    'la': '6_la',
    'si': '7_si',
    'do2':  '8_do2',
}


# کلاس مربع


class Square:
    def __init__(self, x, y, note, image_path):
        self.x = x
        self.y = y
        self.width = square_size
        self.height = ai_settings.Screen_Heigth
        self.note = note[:-4]  # حذف .wav از اسم فایل
        self.font = pygame.font.Font(None, 24)
        self.image_default = pygame.image.load(image_path)
        self.image_active = pygame.image.load("images/key_selected.png")  # تصویر فعال شده
        self.image = self.image_default
        self.textColor = ai_settings.BLACK
        self.active = False  # وضعیت اولیه: غیر فعال

    def draw(self):
        screen.blit(self.image_default, (self.x, self.y))

        text = self.font.render(self.note[2:], True, self.textColor)

        screen.blit(text, (self.x + self.width // 2 - text.get_width() //
                    2, self.y + self.height // 2 - text.get_height() // 2))

    def play(self):
      
        
        pygame.mixer.Sound(f"topics/{mode}/{self.note}.mp3").play()
        
        
    def toggle_active(self):
        if self.active:
            self.image = self.image_default  # اگر فعال بود، به حالت غیر فعال برگردان
        else:
            self.image = self.image_active  # اگر غیر فعال بود، به حالت فعال تغییر بده
        self.active = not self.active  # تغییر وضعیت


class player:
    def __init__(self) -> None: pass

    def play(note, mode):
        print(note)
        print(dictNotes.get(f'{note}'))
        pygame.mixer.Sound(f"topics/{mode}/{dictNotes.get(f'{note}')}.mp3").play()

image_paths = ["images/key_do.png", "images/key_re.png", "images/key_mi.png", "images/key_fa.png", "images/key_so.png", "images/key_la.png", "images/key_si.png", "images/key_do2.png"]  # Replace with your image paths

squares = [Square(i * square_size, 0, note, image_path) for i, (note, image_path) in enumerate(zip(notes, image_paths))]


# ایجاد صفحه
screen = pygame.display.set_mode(
    (ai_settings.Screen_Width, ai_settings.Screen_Heigth))
pygame.display.set_caption("پیانو ساده")


note_states = {note: False for note in ["do", "re", "mi", "fa", "so", "la", "si", "do2"]}

# حلقه بی‌نهایت
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # click x(exit) icon
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  # just while key is down --> play sound
            key = event.dict.get('key')
            # key notes --> Start
            if key == 49:  # key 1
                player.play('do', mode)
                print(squares[0].note)
            elif key == 50:  # key 2
                player.play('re', mode)
                print(squares[1].note)
            elif key == 51:  # key 3
                player.play('mi', mode)
                print(squares[2].note)
            elif key == 52:  # key 4
                player.play('fa', mode)
                print(squares[3].note)
            elif key == 53:  # key 5
                player.play('so', mode)
                print(squares[4].note)
            elif key == 54:  # key 6
                player.play('la', mode)
                print(squares[5].note)
            elif key == 55:  # key 7
                player.play('si', mode)
                print(squares[6].note)
            elif key == 56:  # key 8
                player.play('do2', mode)
                print(squares[7].note)
            # key notes --> End
            # key modes --> Start
            if key == 1073741913:  # key 1 numpad
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

    # نمایش عکس ها
    screen.fill(ai_settings.WHITE)
    for square in squares:
        square.image = square.image_active if square.active else square.image_default
        square.draw()

    # آپدیت صفحه
    pygame.display.flip()
    clock.tick(30)
