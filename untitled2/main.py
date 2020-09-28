import pygame #импорт библиотеки pygame
import random #импорт библиотеки random

pygame.init() #иициализация библиотеки
display_height = 600
display_width = 800 #параметры экрана

display = pygame.display.set_mode((display_width, display_height)) #создание экрана
pygame.display.set_caption('Runner BOY') #заголовок окна
icon = pygame.image.load('icon.png') #загружаем иконку
pygame.display.set_icon(icon) #устанавливаем иконку

pygame.mixer_music.load('fon.mp3')
pygame.mixer_music.set_volume(0.1)

clock=pygame.time.Clock() #переменная для установки кадров

make_jump = False # используется в def jump()
jump_counter = 35 # высота прыжка

usr_wight = 90
usr_height = 120
usr_x = display_width // 3
usr_y = display_height-usr_height-80
usr_img = [pygame.image.load('user.png'), pygame.image.load('user1.png'),
           pygame.image.load('user2.png')]
usr_img_jump=[pygame.image.load('user_jump1.png'), pygame.image.load('user_jump2.png'),
           pygame.image.load('user_jump3.png')]
img_counter = 0
img_counter_jump = 0

cactus_width = 20
cactus_height = 50
cactus_x = display_width - 50
cactus_y = display_height-cactus_height-120
cactus_img_arr=[pygame.image.load('cactus1.png'), pygame.image.load('cactus2.png'),
                pygame.image.load('cactus3.png')]
speed_enemy=4



cloud_img = pygame.image.load('cloud.png')
cloud_x=display_width
cloud_y=display_height-500

ground_img=pygame.image.load('ground.png')
ground_y=display_height-100
ground_x=0

score = 0

class Cloud:
    def __init__(self,x,y,image,speed):
        self.x=x
        self.y=y
        self.image=image
        self.speed=speed

    def move(self):
        if self.x < -100:
            self.x = display_width
        else:
            self.x -= 4
            display.blit(self.image, (self.x, self.y))
            cloud_move()


class Cactus:
    def __init__(self, x, y, width, height, speed, img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.img = img
    def move(self):
        if self.x < -50:
            #self.x = display_width+50+random.randrange(100,150)
            self.x = display_width+50

        else:
            self.x -= self.speed
            display.blit(self.img, (self.x, self.y, self.width, self.height))



def menu():
    global menu, keys
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(pygame.image.load('bg1.png'), (0, 0))
        print_text('Runner BOY', display_width // 3, display_height / 2-100, font_color=(0,0,0),font_size=60 )
        print_text('Press Enter to START', display_width / 3, display_height / 2+50, )
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            menu = False
            run_game()
        pygame.display.update()
        clock.tick(15)


def run_game():
    global make_jump, img_counter_jump, usr_x
    pygame.mixer_music.play(-1)
    game = True
    cactus_arr = []
    cloud_arr=[]
    create_cactus_arr(cactus_arr)
    create_arr_cloud(cloud_arr)


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            usr_x -= 7
        if keys[pygame.K_RIGHT]:
            usr_x += 7
        if keys[pygame.K_SPACE]:
            make_jump = True
            img_counter_jump = 0
        if make_jump:
            jump()
        if keys[pygame.K_ESCAPE]:
            pause()


        display.blit (pygame.image.load('bg1.png'), (0, 0))

        draw_user_run()
        #draw_cactus()
        draw_arr_cactus(cactus_arr)
        draw_cloud(cloud_arr)
        print_text('Scores: ' + str(score), 650, 10)

        jump_img()
        #cloud_move()
        ground_move()

        #display.blit(usr_img,(usr_x, usr_y))
        pygame.display.update()
        clock.tick(140)

def create_cactus_arr(array):
    array.append(Cactus(display_width+50, display_height-170, 40, 70,4, cactus_img_arr[random.randrange(0,3)]))
    array.append(Cactus(display_width+200, display_height-170, 40, 70,4, cactus_img_arr[random.randrange(0,3)]))
    array.append(Cactus(display_width+500, display_height-170, 40, 70,4, cactus_img_arr[random.randrange(0,3)]))
    #array.append(Cactus(display_width+600, display_height-170, 40, 70,4, cactus_img_arr[random.randrange(0,4)]))

def draw_arr_cactus(array):
    for cactus in array:
        cactus.move()
"""def draw_cactus():
    global cactus_height, cactus_width, cactus_x, cactus_y, cactus_img_arr
    choice = random.randrange(0,3)

    enemy = cactus_img_arr[choice]
    display.blit(enemy, (cactus_x, cactus_y, cactus_width, cactus_height))

    if cactus_x < -50:
        cactus_x = display_width
    else:

        #cactus_x = random.randrange(display_width, display_width + 300)
        cactus_x -= speed_enemy
    #display.blit(enemy, (cactus_x, cactus_y, cactus_width, cactus_height))"""


def draw_user_run(): # анимация бега
    global img_counter
    if not make_jump:
        if img_counter == 16:
            img_counter = 0

        display.blit(usr_img[img_counter//8], (usr_x, usr_y))
        img_counter += 1


def jump(): # логика прыжка
    global usr_y, jump_counter, make_jump

    if jump_counter >= -35:
        usr_y -= jump_counter / 2
        jump_counter -= 2
    else:
        jump_counter = 35
        make_jump = False


def jump_img(): # анимация прыжка
    global img_counter_jump, make_jump
    if make_jump:
        if img_counter_jump == 36:
             img_counter_jump = 0

        display.blit(usr_img_jump[img_counter_jump // 12], (usr_x, usr_y))
        img_counter_jump += 1

def create_arr_cloud(array):
    array.append(Cloud(cloud_x+300+random.randrange(0,600), cloud_y+random.randrange(-100,30), cloud_img, speed=random.randrange(1,3)))
    array.append(Cloud(cloud_x+random.randrange(0,200), cloud_y+random.randrange(-100,30), cloud_img, 1))
    #array.append(Cloud(cloud_x+600+random.randrange(0,200), cloud_y+random.randrange(-100,30), cloud_img, 1))

def draw_cloud(array):

    for cloud in array:
        cloud.move()
def cloud_move():   # движение облака
    global cloud_x, cloud_y
    cloud_choice = random.randrange(0, 200)
    if cloud_x < -100:
        cloud_x = display_width
    else:
        #cloud=Cloud(cloud_x,cloud_y-random.randrange(0,200), cloud_img, 4)
        #display.blit(cloud, cloud_x, cloud_y)
        cloud_x -= 1
    display.blit(cloud_img, (cloud_x, cloud_y))


def ground_move(): #движение земли под ногами
    global ground_x, ground_y
    if ground_x < -1600:
        ground_x = 0
        display.blit(ground_img, (0, ground_y))
    else:
        ground_x -= 6
    display.blit(ground_img, (ground_x, ground_y))
    display.blit(ground_img, (ground_x+1600, ground_y))


def pause():       # функия паузы в игре
    pause=True
    pygame.mixer_music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Paused. Press Enter to continued',display_width/3,display_height/2,)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            pause=False
            pygame.mixer_music.play(-1)

        pygame.display.update()
        clock.tick(15)


def print_text (message, x, y, font_color = (255,255,255), font_type = '18930.ttf', font_size = 30): #вывод текста
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))



menu()
#run_game()