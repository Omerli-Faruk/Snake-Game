import pygame
import time
import random

pygame.init()

# Oyun alanının boyutları
width = 500
height = 500

# Renkler
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Oyun alanını oluştur
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yılan Oyunu')

clock = pygame.time.Clock()

snake_block = 10  # Yılanın her bir bloğunun boyutu
snake_speed = 20  # Yılanın hızı

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 20)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    lines = msg.split('\n')
    for i, line in enumerate(lines):
        mesg = font_style.render(line, True, color)
        display.blit(mesg, [width / 10, height / 3 + i * 50])


def game_loop():
    game_over = False
    game_close = False

    # Yılanın başlangıç konumu
    x1 = width / 2
    y1 = height / 2

    # Yılanın başlangıç hareketi
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Yem oluştur
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close:
            display.fill(black)
            message("Oyunu tekrar oynamak için SPACE'e basın \n veya çıkmak için Q'ya basın \n Skor: " + str(score), white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)


        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1

        clock.tick(snake_speed)

    pygame.quit()


game_loop()

