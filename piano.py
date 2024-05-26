import pygame
from pygame.locals import *
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
square_size = ai_settings.Screen_Heigth/5.2

# default mode is piano
modes = ['piano','guitar','flute','xilofono','xilofono2']
mode = 'piano'

# نت‌های موسیقی
notes = os.listdir(f"topics/{mode}")
current_note = 'do'

lesson1Note = [
    'do', 'do', 're','', 'do', 'fa', 'mi', 'do', 'do', 're', 'do', 'so', 'fa', 'do', 'do', 'do2', 'la', 'fa', 'mi', 're', 'la', 'la', 'la', 'fa', 'so', 'fa',    
    'do', 'do', 're', 'do', 'fa', 'mi', 'do', 'do', 're', 'do', 'so', 'fa', 'do', 'do', 'do2', 'la', 'fa', 'mi', 're', 'la', 'la', 'la', 'fa', 'so', 'fa', 'do', 
]


lesson2Note =  [
'mi', 'fa', 'so', 'fa', 'so', 'fa', 'so', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'fa', 'so', 'mi','',
'mi', 'fa', 'so', 'la', 'do', 'si', 'la', 'so', 'fa', 'mi', '',
'mi', 'fa', 'so', 'la', 'do', 'si', 'la', 'so', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
'mi', 'fa', 'so', 'la', 'si', 'do', '',
'la','si', 'do', 'la', 'si', 'do', '',
'do', 're', 'do', 'si', 'la', 'so', 'si', 'si', '',
'so', 'la', 'si', 'so', 'la', 'si', '',
'la','si', 'la', 'so', 'si', 'so', 'fa', 'so', 'fa', 'mi', '',
'la','si', 'la', 'so', 'la', 'so', 'fa', 'so', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
'do', 'si', 'do', 'si', 'do', 're', 'do2', 'do', 'si', 'la', '',
'si', 'la', 'si', 'so', 'la', 'si', 'si', 'do', 'si', 'la', 'so', '',
'la','so', 'fa', 'so', 'fa', 'mi', '',
'la','so', 'fa', 'so', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
'mi', 'fa', 'so', 'fa', 'so', 'la', 'fa', 'mi', '',
]

count = 0 

#قالب اتصال عبارات به نام فایل ها
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
        self.height = (65/100)*ai_settings.Screen_Heigth
        self.note = note[:-4]  # حذف .wav از اسم فایل
        self.font = pygame.font.Font(None, 24)
        self.image_default = pygame.image.load(image_path)
        self.image_active = pygame.image.load("images/key_selected.png")  # تصویر فعال شده
        self.image = self.image_default
        self.textColor = ai_settings.BLACK
        self.active = False  # وضعیت اولیه: غیر فعال

    def draw(self,training=False):
        if(training):
            # اول ایجاد شی فونت بعدش رندر گرفتن و بعد بلیت
            # چک کردن نوت فعال 
            if ( lesson2Note[count] == self.note[2:]) :
                text = self.font.render(f'** {self.note[2:]} **', True, self.textColor)
            else :
                text = self.font.render(self.note[2:], True, self.textColor)
            screen.blit(self.image_default, (self.x, self.y))
            # درج متن در وسط مربع ها
            screen.blit(text, (self.x + self.width // 2 - text.get_width() //
                        2, self.y + self.height // 2 - text.get_height() // 2))
        else:
            if(current_note == str(self.note[2:])):
                text = self.font.render(f'** {self.note[2:]} **', True, self.textColor)
            else :
                text = self.font.render(self.note[2:], True, self.textColor)
            screen.blit(self.image_default, (self.x, self.y))
            # درج متن در وسط مربع ها
            screen.blit(text, (self.x + self.width // 2 - text.get_width() //
                        2, self.y + self.height // 2 - text.get_height() // 2))

    def play(self):
        # پخش نوت   
        pygame.mixer.Sound(f"topics/{mode}/{self.note}.mp3").play()
        
        
    # def toggle_active(self,training=False):


# کلاس انتخاب
class Choice:
    def __init__(self, x, y, width, mode, color):
        self.x = x + 10
        self.y = y
        self.width = width
        self.height = (34/100)*ai_settings.Screen_Heigth
        self.mode = mode
        self.font = pygame.font.Font(None, 24)
        # self.image_active = pygame.image.load("images/key_selected.png")  # تصویر فعال شده
        self.color = color
        self.textColor = ai_settings.BLACK
        self.active = False  # وضعیت اولیه: غیر فعال

    def draw(self):
        # blit برای درج تصویر است
        pygame.draw.rect(screen,self.color,pygame.Rect(self.x,self.y,self.width,self.height),100,30)

        # اول ایجاد شی فونت بعدش رندر گرفتن و بعد بلیت
        # چک کردن نوت فعال 
        if ( mode == self.mode) :
            text = self.font.render(f'** {self.mode} **', True, self.textColor)
        else :
            text = self.font.render(self.mode, True, self.textColor)


        
        # درج متن در وسط مربع ها
        screen.blit(text, (self.x + self.width // 2 - text.get_width() //
                    2, self.y + self.height // 2 - text.get_height() // 2))

    # def play(self):
    #     # پخش نوت   
    #     pygame.mixer.Sound(f"topics/{mode}/{self.note}.mp3").play()
        
        
    def toggle_mode(self):
        return self.mode



class player:
    def __init__(self) -> None: pass

    def play(note, mode):
        print(note)
        # print(dictNotes.get(f'{note}'))
        pygame.mixer.Sound(f"topics/{mode}/{dictNotes.get(f'{note}')}.mp3").play()  # پخش نوت (توسط تابع سوند یک صدا از روی فایل تولید میشود)

image_paths = ["images/key_do.png", "images/key_re.png", "images/key_mi.png", "images/key_fa.png", "images/key_so.png", "images/key_la.png", "images/key_si.png", "images/key_do2.png"]  # مسیر عکس نوت ها
btn_color = ["blue", "red", "green", "yellow", "purple"]

# انوموریک یک تاپل با مقادیر شمارنده و ایتم بر میگرداند 
# تابع زیپ دو تا کالکشن یا تاپل رو باهم جوین میکند مثلا ایتم اول یکی با ایتم اول اون یکی و به همین ترتیب
squares = [Square(i * square_size, (35/100)*ai_settings.Screen_Heigth, note, image_path) for i, (note, image_path) in enumerate(zip(notes, image_paths))]

# دکمه ها
button_width = ai_settings.Screen_Width // 5.5
button_height = ai_settings.Screen_Heigth
buttons = [Choice(i * button_width + i*12, 0, button_width, mode, color)
           for i, (mode, color) in enumerate(zip(modes, btn_color))]

# ایجاد صفحه
screen = pygame.display.set_mode(
    (ai_settings.Screen_Width, ai_settings.Screen_Heigth))
pygame.display.set_caption("پیانو ساده")



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
                current_note = 'do'
                player.play('do', mode)
                print(squares[0].note)
            elif key == 50:  # key 2
                current_note = 're'
                player.play('re', mode)
                print(squares[1].note)
            elif key == 51:  # key 3
                current_note = 'mi'
                player.play('mi', mode)
                print(squares[2].note)
            elif key == 52:  # key 4
                current_note = 'fa'
                player.play('fa', mode)
                print(squares[3].note)
            elif key == 53:  # key 5
                current_note = 'so'
                player.play('so', mode)
                print(squares[4].note)
            elif key == 54:  # key 6
                current_note = 'la'
                player.play('la', mode)
                print(squares[5].note)
            elif key == 55:  # key 7
                current_note = 'si'
                player.play('si', mode)
                print(squares[6].note)
            elif key == 56:  # key 8
                current_note = 'do2'
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
                    current_note = str(square.note[2:])
                    square.play()
            for choice in buttons:
                if choice.x < x < choice.x + choice.width and choice.y < y < choice.y + choice.height:
                    mode = choice.toggle_mode()

    screen.fill(ai_settings.WHITE)
    # نمایش دکمه مود ها  
    for choice in buttons:
        choice.draw()

    # نمایش عکس ها
    for square in squares:
        square.image = square.image_active if square.active else square.image_default
        square.draw()
    
    if(lesson1Note[count] != '') : 
        player.play(lesson1Note[count], mode)
    count = count + 1
    pygame.time.delay(500)

    clock.tick(30)
    # آپدیت صفحه
    pygame.display.flip()

