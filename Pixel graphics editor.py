import pygame
import math
import numpy
from PIL import Image
import numpy as np
import itertools
from operator import add

win_x =1000
win_y = 1000

pixel_array = []

ratio = 10

array = []

save_size = (512,512)

active_palette = 0
color = 0
pixel_density = 50
clearing = True

def make_singular(l):
    try:
        if len(l) == 1:
            return l[0]
        else:
            return [make_singular(l_) for l_ in l]
    except:
        return l

palettes = (((0,0,178), (0,0,153), (0,0,127), (0,0,102), (0,0,76)),
            ((75,50,89), (105,91,169), (116,143,122), (212,202,133), (255,153,34)),
            ((66,5,45), (107,8,72), (163,10,59), (236,97,10), (255,193,0)),
            ((254,253,202), (255,224,163), (225,130,115), (148,57,57), (106,38,52)),
            ((82,46,145), (84,38,102), (88,45,145), (59,0,81), (72,10,154)),
            ((229,110,30), (204,98,27), (179,85,23), (153,73,20), (127,60,16)),
            ((35,58,72),(67,110,103), (108,149,133), (190,208,166), (229,227,206)),
            ((229,227,206), (229,227,206), (240,235,226), (203,192,170), (243,209,142)),
            ((239,79,134), (232,85,102), (244,123,90), (249,172,94), (249,221,103)),
            ((208,230,166), (191,211,122), (137,178,174), (91,129,142), (35,66,87)),
            ((7,140,169), (83,209,236), (242,242,242), (197,223,22), (221,241,86)),
            ((53,53,54), (70,69,71), (83,83,84), (146,145,148), (214,214,214)),
            ((212,255,232), (202,231,231), (188,199,214), (173,169,195), (162,141,184)),
            ((59,139,235),(28,119,172), (15,40,98), (255,168,0), (250,197,28)),
            ((159,127,135), (180,143,139), (201,162,148), (225,189,165), (236,202,171)))

current_palette = palettes[active_palette]
current_color = current_palette[color]

pygame.init()

run = True

isActivated = True

pos = (0, 0)

size = 10
hex_radius = math.floor(math.cos(0.5235987756)*size)
oct_radius = ((1+math.sqrt(2)) / 2)*size

array_settings = {'shape': (pixel_density,pixel_density, 3), 'typestr':'|i8', "version":3}

#triangle_a = math.sqrt(size**2 - radius**2)

n = 4

win = pygame.display.set_mode((win_x, win_y))

def draw_current_palette():
    pygame.draw.rect(win, current_palette[0], (0, 0,win_x/pixel_density*(math.floor(pixel_density/5))*1,win_y/pixel_density))
    pygame.draw.rect(win, current_palette[1], (win_x/pixel_density*(math.floor(pixel_density/5))*1, 0,win_x/pixel_density*(math.floor(pixel_density/5))*2,win_y/pixel_density))
    pygame.draw.rect(win, current_palette[2], (win_x/pixel_density*(math.floor(pixel_density/5))*2, 0,win_x/pixel_density*(math.floor(pixel_density/5))*3,win_y/pixel_density))
    pygame.draw.rect(win, current_palette[3], (win_x/pixel_density*(math.floor(pixel_density/5))*3, 0,win_x/pixel_density*(math.floor(pixel_density/5))*4,win_y/pixel_density))
    pygame.draw.rect(win, current_palette[4], (win_x/pixel_density*(math.floor(pixel_density/5))*4, 0,win_x/pixel_density*(math.floor(pixel_density/5))*5,win_y/pixel_density))

while run:

    current_palette = palettes[active_palette]
    current_color = current_palette[color]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = event.pos
            except AttributeError:
                pass

            if n == 0:
                pygame.draw.circle(win, current_color, pos, size)

            if n == 4:
                for i in pixel_array:
                    if  pos[0] - i[0] < win_x/pixel_density and pos[0]-i[0]>0:
                        if pos[1] - i[1] < win_y/pixel_density and pos[1]-i[1]> 0:
                            pygame.draw.rect(win, current_color, (i[0],i[1], win_x/pixel_density, win_y/pixel_density))
                            i.append(current_color)
                            del i[2]
            
            #if n == 6: #overly complex hexagon drawing function
                #pygame.draw.polygon(win, current_color, ((pos[0] + size/2, math.floor(pos[1] + hex_radius)), (math.floor(pos[0] + hex_radius), pos[1]), (pos[0] + size/2, math.floor(pos[1]-hex_radius)),(pos[0] - size/2, math.floor(pos[1]-hex_radius)),(math.floor(pos[0]-hex_radius), pos[1]), (pos[0]-size/2, math.floor(pos[1]+hex_radius))))
            #elif n == 8: #the same but this time it's an octagon
                #pygame.draw.polygon(win, current_color, ((pos[0]+size/2, math.floor(pos[1]+oct_radius)), (math.floor(pos[0]+oct_radius), pos[1]+size/2), (math.floor(pos[0]+oct_radius), pos[1]-size/2), (pos[0]+size/2, math.floor(pos[1]-oct_radius)),(pos[0]-size/2, math.floor(pos[1]-oct_radius)), (math.floor(pos[0]-oct_radius), pos[1]-size/2), (math.floor(pos[0]-oct_radius), pos[1]+size/2), (pos[0]-size/2, math.floor(pos[1]+oct_radius))))
                #pygame.draw.polygon()
        if event.type == pygame.KEYDOWN:
            #palette settings
            if event.key == pygame.K_1:
                active_palette = 0
            if event.key == pygame.K_z:
                active_palette = 9
            if event.key == pygame.K_x:
                active_palette = 10
            if event.key == pygame.K_c:
                active_palette = 11
            if event.key == pygame.K_v:
                active_palette = 12
            if event.key == pygame.K_b:
                active_palette = 13
            if event.key == pygame.K_n:
                    active_palette = 14
            if event.key == pygame.K_2:
                active_palette = 1
            if event.key == pygame.K_3:
                active_palette = 2
            if event.key == pygame.K_4:
                active_palette = 3
            if event.key == pygame.K_5:
                active_palette = 4
            if event.key == pygame.K_6:
                active_palette = 5
            if event.key == pygame.K_7:
                active_palette = 6
            if event.key == pygame.K_8:
                active_palette = 7
            if event.key == pygame.K_9:
                active_palette = 8

            #brush and environment settings
            if event.key == pygame.K_s:
                n = 0
            if event.key == pygame.K_d:
                n = 8
            if event.key == pygame.K_f:
                n = 6
            if event.key == pygame.K_UP:
                size = size+1
            elif event.key == pygame.K_DOWN:
                size = size - 1
                if size < 2:
                   size = 2
            if event.key == pygame.K_p:
                n = 4
                win.fill((255, 255, 255))
                for i in range(pixel_density):
                    pygame.draw.line(win , (0, 0, 0), (i*(win_x/pixel_density),0),  (i*(win_x/pixel_density), win_y))
                    pygame.draw.line(win , (0, 0, 0), (0, i*(win_y/pixel_density)), (win_x, i*(win_y/pixel_density)))
                for i in range(pixel_density):
                    for u in range(pixel_density):
                        pixel_array.append([int(i*(win_x/pixel_density)),int(u*(win_y/pixel_density))])
                for i in pixel_array:
                    i.append((255, 255, 255))
                #print(pixel_array)
            if event.key == pygame.K_o:
                win.fill((255, 255, 255))        
                    
            #color settings
            if event.key == pygame.K_q:
                color = 0
            if event.key == pygame.K_w:
                color = 1
            if event.key == pygame.K_e:
                color = 2
            if event.key == pygame.K_r:
                color = 3
            if event.key == pygame.K_t:
                color = 4

            #saving
            if event.key == pygame.K_ESCAPE:
                img = Image.new('RGB', (win_x, win_y), (255, 255, 255))
                img_data = img.load()
                #print(img_data)
                #for i in range(len(pixel_array)):
                 #   pixel_array[i][2]=tuple(pixel_array[i][2])
                  #  pixel_array[i]= tuple(pixel_array[i])
                #pixel_array = tuple(pixel_array)
                #try:
                 #   for i in range(1,len(pixel_array)+1):
                  #      for u in range(ratio):
                   #         img_data[((i%pixel_density)*ratio)-u, (math.floor(i/pixel_density)*ratio)-u]=pixel_array[i-1][2]
                #except IndexError:
                 #   pass
                #print(pixel_array[0])
                for i in pixel_array:
                    for u in range(1):
                        del i[u]
                        #print(i[u])
                #print(pixel_array)
                #print(pixel_array[0])
                for i in pixel_array:
                    del i[0]
                        #print(i[u])
                #print(pixel_array)
                #pixel_array.__array_interface__ = lambda: None
                #setattr(pixel_array, __array_interface__, array_settings)
                #print(pixel_array)
                #pixel_array =  np.array(pixel_array)
                #print(np.shape(pixel_array))
                #pixel_array.reshape((pixel_density,pixel_density))
                #print(pixel_array)
                #print(len(pixel_array))
                array = np.array(pixel_array).reshape(pixel_density,pixel_density,3)
                #print(array)
                counter_i = -1
                counter_u = -1
                #for i in array:
                    #for u in i:
                        #pixel_pos = np.where(i == u)
                        #for j in range(pixel_pos[0][0]):
                            #for k in range(pixel_pos[0][1]):
                                    #img_data[j,k]=tuple(array[j][k])
                #img = img.resize((pixel_density*ratio, pixel_density*ratio))
                for i in range(win_x):
                    for u in range(win_y):
                        img_data[i, u] = tuple(win.get_at((i , u)))
                img.save("Image.bmp")
                print("done")
                
                    
                        
    draw_current_palette()
    pygame.display.update()
