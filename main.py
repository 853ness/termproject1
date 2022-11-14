import pygame

pygame.init()
#Background and display settings 
win = pygame.display.set_mode((1000, 500))
scenes = ["city.png", "forest1_BG.png", "nighttime.png", "country-platform-back.png"]
scene_Ind = 0
bg_img = pygame.image.load(scenes[scene_Ind])
bg = pygame.transform.scale(bg_img, (1000, 500))
width = 1000
i = 0

counter = 200
cnt = 0

run = True
while run:
    cnt += .5


    print(cnt)
#change scene timer
    if cnt == counter:
        scene_Ind = (scene_Ind + 1) % 4
        print(scene_Ind)
        bg_img = pygame.image.load(scenes[scene_Ind])
        bg = pygame.transform.scale(bg_img, (1000, 500))
        cnt = 0

    win.fill((0, 0, 0))
    win.blit(bg, (i, 0))
    win.blit(bg, (width + i, 0))

    if i == -width:
        win.blit(bg, (width + i, 0))
        i = 0
    i -= 0.5
    pygame.display.update()









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
