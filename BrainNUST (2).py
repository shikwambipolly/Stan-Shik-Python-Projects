import time
import pygame
pygame.init()
pygame.font.init()

# Questions and Answers
q1 = "What is the name of the president of namibia?"
q2 = "x - 5 + y, when y = 5. Find x"
a1 = "Hage Geingob"
a2 = "10"
# Dictionary conecting questions with answers
qa = {q1: a1, q2: a2}

# Pygame Window
display_width = 1200
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Brain NUST")
clock = pygame.time.Clock()

# colours
black = pygame.color.Color("#e1e4e8")# grey
white = pygame.color.Color("#000000")# black
grey = pygame.color.Color("#ffffff")# white
lgreen = pygame.color.Color("#42d444")
dgreen = pygame.color.Color("#a2a8b0")# grey
red = pygame.color.Color("#d44242")
redred = pygame.color.Color("#ff0000")
# dimensions and position of the rectangles
x = 10
y = 600
width = 200
height = 80
space = 200/6
mid = 500

# image if needed
nust_logo = pygame.image.load("NUST logo.png")

# booleans for the while loops for each question
question_1 = True
question_2 = True

# captures the keys pressed in the pygame window
keys = pygame.key.get_pressed()


# this function prints/displays the text onto the pygame console
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message(string, coordinates, cent):
    text = pygame.font.SysFont("ArialRoundedMTBold", 75)
    TextSurf, TextRect = text_objects(string, text)
    if cent == 1:
        TextRect.center = coordinates
    elif cent == 0:
        TextRect = coordinates
    display.blit(TextSurf, TextRect)

# When time is 0
def time_0(q, a):
    display.fill(red)
    message(q, (0, 0), 0)
    message(str(time_left), ((display_width/2), (display_height/2)), 1)
    pygame.display.flip()
    time.sleep(4)
    message("Answer is " + a, ((display_width/2), (display_height/2 + 50)), 1)
    pygame.display.flip()
    time.sleep(2)
# answered before time
def beforeT(q, a):
    display.fill(lgreen)
    message(q, (0, 0), 0)
    time.sleep(2)
    message("Answer is " + a, ((display_width/2), (display_height/2)), 1)
    pygame.display.flip()
    time.sleep(5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # the time_left is here because of the while loops
    time_left = 30
    clock.tick(50)
    display.fill(black)
    message("What question do you want? ", ((display_width/2), 50), 1)
    display.blit(nust_logo, ((display_width/2) - 50, (display_height/2) - 50))

    mouse = pygame.mouse.get_pos()
    # this is the same as the interactive function that i wanted to make
    if x + width + space > mouse[0] > x + space and y + height > mouse[1] > y:
        pygame.draw.rect(display, lgreen, (x + mid - width * 2 - space * 2, y, width, height))
    else:
        pygame.draw.rect(display, dgreen, (x + space, y, width, height))

    pygame.draw.rect(display, dgreen, (x + mid - width - space, y, width, height))
    pygame.draw.rect(display, dgreen, (x + mid, y, width, height))
    pygame.draw.rect(display, dgreen, (x + mid + width + space, y, width, height))
    pygame.draw.rect(display, dgreen, (x + display_width - (space + width), y, width, height))

    # pygame.draw.rect(display, dgreen, (x + mid - width * 2 - space * 2, y - height - 20, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid - width * 2 - space * 2, y - height * 2 - 40, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid - width * 2 - space * 2, y - height * 3 - 60, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid - width * 2 - space * 2, y - height * 4 - 80, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid - width - space, y - height * 2 - 40, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid, y - height * 2 - 40, width, height))
    # pygame.draw.rect(display, dgreen, (x + mid + width + space, y - height * 2 - 40, width, height))
    # pygame.draw.rect(display, dgreen, (x + display_width - (space + width), y - height * 2 - 40, width, height))
    pygame.display.update()

    # gets the input keys in the pygame console
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        # if no. 1 is pressed
        if keys[pygame.K_1]:
            # turns the console black
            display.fill(black)
            while question_1:
                message(q1, (0,0), 0)
                pygame.display.flip()
                if time_left > 0:
                    while time_left > 0:
                        time.sleep(1)
                        time_left -= 1
                        display.fill(black)
                        message(q1, (0,0), 0)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                time_left = -1
                        message(str(time_left), ((display_width/2), (display_height/2)), 0)
                        pygame.display.flip()
                while time_left == 0:
                    time_0(q1, a1)
                    question_1 = False
                    break
                while time_left == -1:
                    beforeT(q1, a1)
                    question_1 = False
                    break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and question_1 == False:
            message("Question has already been asked", ((display_width/2), (display_height/2)), 1)
            pygame.display.flip()
            time.sleep(2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            display.fill(black)
            while question_2:
                message(q2, (0,0), 0)
                pygame.display.flip()
                while time_left > 0:
                    time.sleep(1)
                    time_left -= 1
                    display.fill(black)
                    message(q2, (0,0), 0)
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            time_left = -1
                            break
                    message( str(time_left), ((display_width/2), (display_height/2)), 0)
                    pygame.display.flip()
                while time_left == 0:
                    time_0(q2, a2)
                    question_2 = False
                    break
                while time_left == -1:
                    beforeT(q2, a2)
                    question_2 = False
                    break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_2] and question_2 == False:
            message("Question has already been asked", ((display_width/2), (display_height/2)), 1)
            pygame.display.flip()
            time.sleep(2)

    pygame.display.update()
pygame.quit()



