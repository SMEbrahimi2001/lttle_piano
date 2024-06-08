import pygame
import pygame_gui
import sys
from piano import start_piano_game
from setting import Settings

pygame.init()
ai_setting = Settings()
screen_width = ai_setting.ScreenWidth_start
screen_height = ai_setting.ScreenHeigth_start


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Piano Game')

manager = pygame_gui.UIManager(
    (ai_setting.ScreenWidth_start, ai_setting.ScreenHeigth_start))

background_image = pygame.image.load("topics/background.jpg")

# حالت‌های مختلف بازی
MAIN_MENU = "main_menu"
GAME_SCREEN = "game"
SETTINGS_SCREEN = "settings"
current_screen = MAIN_MENU

# حلقه اصلی بازی
clock = pygame.time.Clock()
is_running = True

manager = pygame_gui.UIManager(
    (ai_setting.ScreenWidth_start, ai_setting.ScreenHeigth_start))

# دکمه‌های صفحه اصلی
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 150), (100, 50)),
    text='Start Game',
    manager=manager
)
settings_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 250), (100, 50)),
    text='Settings',
    manager=manager
)
back_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((250, 350), (100, 50)),
    text='Back',
    manager=manager
)


# تنظیمات صفحه نمایش


back_button.hide()


def show_main_menu():
    start_button.show()
    settings_button.show()
    back_button.hide()


def show_game_screen():
    start_button.hide()
    settings_button.hide()
    back_button.show()
    start_piano_game()  # اینجا تابع شروع بازی پیانو فراخوانی می‌شود


def show_settings_screen():
    start_button.hide()
    settings_button.hide()
    back_button.show()


while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if current_screen == MAIN_MENU:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    current_screen = GAME_SCREEN
                    show_game_screen()
                elif event.ui_element == settings_button:
                    current_screen = SETTINGS_SCREEN
                    show_settings_screen()

        elif current_screen in [GAME_SCREEN, SETTINGS_SCREEN]:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == back_button:
                    current_screen = MAIN_MENU
                    show_main_menu()

        manager.process_events(event)

    manager.update(time_delta)
    screen.blit(background_image, (0, 0))

    # screen.fill((ai_setting.BLACK))

    manager.draw_ui(screen)

    if current_screen == GAME_SCREEN:
        # اینجا کد مربوط به صفحه بازی را اضافه کنید
        font = pygame.font.Font(None, 74)
        game_text = font.render('Game Screen', True, (255, 255, 255))
        screen.blit(game_text, (250, 100))
        # این بخش می‌تواند شامل منطق و رسم گرافیک‌های مربوط به بازی پیانو باشد

    elif current_screen == SETTINGS_SCREEN:
        # اینجا کد مربوط به صفحه تنظیمات را اضافه کنید
        font = pygame.font.Font(None, 74)

        # این بخش می‌تواند شامل تنظیمات بازی باشد

    pygame.display.update()
    pygame.display.flip()
pygame.quit()
