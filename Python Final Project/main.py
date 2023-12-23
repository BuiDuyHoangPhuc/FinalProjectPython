import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint
import os
import time
import webbrowser
from pygame.locals import *
import pygame.mixer
pygame.init() 
clock = pygame.time.Clock()


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

def exit_game():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    musicvu_path = os.path.join(script_dir, "bip.wav")
    pygame.mixer.music.load(musicvu_path)
    pygame.mixer.music.play()
    if messagebox.askokcancel("Exit", "Do you really want to exit the game?"):
        musicvu_path = os.path.join(script_dir, "bip.wav")
        pygame.mixer.music.load(musicvu_path)
        pygame.mixer.music.play()
        root.destroy()

def start_game():
    # Destroy the main window
    root.destroy()
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    # Specify image file paths
    musicc1_path = os.path.join(script_dir, "giuagame.wav")
    pygame.mixer.music.load(musicc1_path)
    pygame.mixer.music.play(-1)
    background_path = os.path.join(script_dir, "congueh.png")
    truck_path = os.path.join(script_dir, "truck.jpg")
    containers_path = os.path.join(script_dir, "containers.png")

    img = [0, 0, 0]
    y = -20
    x = randint(10, 700)

    game = tk.Tk()
    game.title("Picking Containers")
    # Manhinh
    canvas = tk.Canvas(master=game, width=800, height=720, background="white")
    canvas.pack()

    #Background
    img[0] = ImageTk.PhotoImage(Image.open(background_path).resize((850, 660)))
    img[1] = ImageTk.PhotoImage(Image.open(truck_path).resize((180, 90))) 
    img[2] = ImageTk.PhotoImage(Image.open(containers_path).resize((80, 80)))

    backgr1 = canvas.create_image(0, 0, anchor=tk.NW, image=img[0])
    backgr2 = canvas.create_image(800, 0, anchor=tk.NW, image=img[0])

    truck = canvas.create_image(0, 520, anchor=tk.NW, image=img[1])
    containers = canvas.create_image(x, y, anchor=tk.NW, image=img[2])

    canvas.update()

    score = 0
    text_score = canvas.create_text(500, 50, text="SCORE : " + str(score), fill="red", font=("Times", 20))
    background_speed = 5

    def PickingContainers():
        nonlocal containers, score, y, x
        nonlocal backgr1, backgr2

        # Di chuyển cả hai hình nền từ phải sang trái
        canvas.move(backgr1, -background_speed, 0)
        canvas.move(backgr2, -background_speed, 0)

        # Kiểm tra nếu hình nền 1 đi ra khỏi màn hình, thiết lập lại vị trí
        if canvas.coords(backgr1)[0] <= -800:
            
            canvas.coords(backgr1, 800, 0)

        # Kiểm tra nếu hình nền 2 đi ra khỏi màn hình, thiết lập lại vị trí
        if canvas.coords(backgr2)[0] <= -800:
            canvas.coords(backgr2, 800, 0)
            
        canvas.move(containers, 0, 10)

        if canvas.coords(containers)[1] > 620:
            canvas.delete(containers)
            y = -20
            x = randint(10, 750)
            containers = canvas.create_image(x, y, anchor=tk.NW, image=img[2])

        if (
            canvas.coords(containers)[0] >= canvas.coords(truck)[0]
            and canvas.coords(containers)[0] <= canvas.coords(truck)[0] + 180
            and canvas.coords(containers)[1] >= canvas.coords(truck)[1]
            and canvas.coords(containers)[1] <= canvas.coords(truck)[1] + 90
        ):
                
                canvas.delete(containers)
                y = -20
                x = randint(10, 750)
                containers = canvas.create_image(x, y, anchor=tk.NW, image=img[2])
                score = score + 1
                canvas.itemconfig(text_score, text="SCORE:" + str(score))
                
                # Check if the score is 10 to move to the next level
                if score == 10:
                    music1_path = os.path.join(script_dir, "quaman.wav")
                    pygame.mixer.music.load(music1_path)
                    pygame.mixer.music.play()
                    canvas.itemconfig(text_score, text="SCORE: 10 \n Moving to the next level")
                    game.after(1000, move_to_next_level)
                    
        # Schedule the next call after 50 milliseconds
        game.after(50, PickingContainers)

    def move_to_next_level():
        musicc1_path = os.path.join(script_dir, "giuagame.wav")
        pygame.mixer.music.load(musicc1_path)
        pygame.mixer.music.play(-1)
        # Close the current game window
        game.destroy()

        #Call your function to start the new game or level
        #NEW GAME
        pygame.init() 
        clock=pygame.time.Clock()

        #Khai báo biến
        t=0
        gameplay=True
        pressvc=True
        answer=False
        fps=120
        ranques=1       

        #Tiêu đề và icon
    
        icon_path = os.path.join(script_dir, 'gapic1.png')
        logogame= pygame.image.load(icon_path)

        #City
        bg_path = os.path.join(script_dir, 'uehntp.png')
        bg = pygame.image.load(bg_path)

        #City 2
        bg2_path = os.path.join(script_dir, 'ueh11.jpg')
        bg2 = pygame.image.load(bg2_path)

        #Font chữ
        font=pygame.font.Font(pygame.font.get_default_font(),16)

        #road
        road_path = os.path.join(script_dir, 'pngtree-empty-straight-road-asphalt-marking-png-image_6361888.png')
        road = pygame.image.load(road_path)

        #Cloud
        cloud_path = os.path.join(script_dir, 'white-cloud-clipart-design-illustration-free-png.webp')
        cloud = pygame.image.load(cloud_path)

        #Truck
        truck_path = os.path.join(script_dir, 'truck.jpg')
        truck = pygame.image.load(truck_path)

        truck_y = 700
        truck_x = 0
        truck_hcn=truck.get_rect(center=(truck_x,truck_y))

        #xe phụ 1
        xe_path = os.path.join(script_dir, 'red-sport-car-design-transparent-background-free-png.webp')
        xe = pygame.image.load(xe_path)

        car = pygame.transform.scale_by(xe, 0.4)
        car_x = 500
        car_y = 700
        car_hcn=car.get_rect(center=(car_x,car_y))

        #xe phụ 2
        xe2_path = os.path.join(script_dir, 'z4957778406822_88d0a02cbbf5fa1de20d19bdfdd5b8da.jpg')
        xe2 = pygame.image.load(xe2_path)

        car2=pygame.transform.scale_by(xe2, 0.4)
        car2_x= 500
        car2_y= 600
        car2_hcn=car.get_rect(center=(car2_x,car2_y))

        #Chốt
        chot_path = os.path.join(script_dir, 'stop.png')
        chot = pygame.image.load(chot_path)

        chot_scale = pygame.transform.scale_by(chot,0.6)
        chot_hcn = chot_scale.get_rect(center=(600,600))

        #Nổ
        no_path = os.path.join(script_dir, 'crash2.jpg')
        no = pygame.image.load(no_path)

        crash=pygame.transform.scale_by(no, 0.5)
        crash_x = 500
        crash_y = 600
        crash_hcn=car.get_rect()

        #Mặt trời
        sun_path = os.path.join(script_dir, 'sunn.jpg')
        sun = pygame.image.load(sun_path)

        #Bầu trời
        sky_path = os.path.join(script_dir, '800x600-light-sky-blue-solid-color-background.jpg')
        sky = pygame.image.load(sky_path)
        sky2=pygame.transform.scale_by(sky, 1.1)

        #Cửa sổ game
        manhinh = pygame.display.set_mode((800,800))
        #Check va chạm
        def checkvc():
                if (car_hcn.centery==truck_hcn.centery and truck_hcn.centerx+250==car_hcn.centerx and t in [1,5,9]) or (car2_hcn.centery==truck_hcn.centery and truck_hcn.centerx+250==car2_hcn.centerx and t in [3,7]):
                        return False
                else:
                        return True
                
        #Check tránh va chạm
        def press():
            if (checkvc()==True and truck_hcn.colliderect(car_hcn) and t in [1,5,9]) or (checkvc()==True and truck_hcn.colliderect(car2_hcn) and t in [3,7]):
                return False
            else:
                return True

        #Vòng lặp xử lý game
        
        transition = True
        def transition():
            font=pygame.font.Font(pygame.font.get_default_font(),50)
            pygame.draw.rect(manhinh,(0,128,0),pygame.Rect(0,0,800,800))
            text11=font.render(f'Round 2 is coming up',True,(255,255,255))
            text11_rect=text11.get_rect()
            text11_rect.center=(400,350)
            text12=font.render(f'Good luck!!!',True,(255,255,255))
            text12_rect=text12.get_rect()
            text12_rect.center=(400,500)
            text13=font.render(f'Delivery Goods',True,(255,255,255))
            text13_rect=text13.get_rect()
            text13_rect.center=(400,420)
            manhinh.blit(text12,text12_rect)
            manhinh.blit(text11,text11_rect)
            manhinh.blit(text13,text13_rect)
            pygame.display.update()
            time.sleep(4)
            return True
        transition=transition()
        running=True
        while running and transition:
            pressvc=press()
            gameplay=checkvc()

            #Chỉnh FPS
            clock.tick(fps)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False

            #Tạo nút điều khiển cho xe
                if event.type==pygame.KEYDOWN:
                    if (event.key==pygame.K_w or event.key==pygame.K_UP) and gameplay and pressvc:
                        truck_y=truck_y-100
                    if (event.key==pygame.K_s or event.key==pygame.K_DOWN) and gameplay and pressvc:
                        truck_y=truck_y+100
                    if (event.key==pygame.K_w or event.key==pygame.K_UP) and gameplay and pressvc==False:
                        truck_y=truck_y
                    if (event.key==pygame.K_s or event.key==pygame.K_DOWN) and gameplay and pressvc==False:
                        truck_y=truck_y 
                    if (event.key==pygame.K_SPACE) and gameplay==False:
                        gameplay=True
                        t=0
                        truck_x=0
            truck_x += 5
            if truck_hcn.left==800:
                    truck_x=0
                    t+=1
                    car_x=500
                    car2_x=500

            #Tạo xe xuất hiện và chuyển động
            if t in [1,5,9]:
                car_x+=2
            if t in [3,7]:
                car2_x+=2

            #Tạo border
            if truck_y > 700:
                    truck_y = 700
            if truck_y < 600:
                    truck_y = 600

            #Biểu diễn game
            if gameplay and truck_hcn.colliderect(chot_hcn) and t in [10] and answer==False:
                    gameplay = False
                    pressvc = False
                    if gameplay==False and t in [10]:
                        manhinh.blit(sky,(0,0))
                        manhinh.blit(bg,(0,30))
                        manhinh.blit(road,(0,530))
                        manhinh.blit(cloud,(30,100))
                        manhinh.blit(cloud,(400,50))
                        manhinh.blit(sun,(550,0))
                        manhinh.blit(chot_scale,chot_hcn)
                        manhinh.blit(chot_scale,(chot_hcn.centerx,chot_hcn.centery-50))
                        manhinh.blit(truck,truck_hcn)
                        #
                        if ranques==1:
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,50,800,100))
                            font=pygame.font.Font(pygame.font.get_default_font(),20)
                            text=font.render(f'You have reached the toll plaza! Answer 3 questions to get through.',True,(255,255,255))
                            text_rect=text.get_rect()
                            text_rect.center=(400,100)
                            manhinh.blit(text,text_rect)
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,150,800,20))
                            text1=font.render(f'Question 1: When was UEH established?',True,(255,255,255))
                            text1_rect=text1.get_rect()
                            text1_rect.center=(400,150)
                            manhinh.blit(text1,text1_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,200,100,50))
                            text2=font.render(f'A.1967',True,(255,255,255))
                            text2_rect=text2.get_rect()
                            text2_rect.center=(150,230)
                            manhinh.blit(text2,text2_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,200,100,50))
                            text3=font.render(f'B.1976',True,(255,255,255))
                            text3_rect=text3.get_rect()
                            text3_rect.center=(650,230)
                            manhinh.blit(text3,text3_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,300,100,50))
                            text4=font.render(f'D.1977',True,(255,255,255))
                            text4_rect=text4.get_rect()
                            text4_rect.center=(650,330)
                            manhinh.blit(text4,text4_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,300,100,50))
                            text5=font.render(f'C.1974',True,(255,255,255))
                            text5_rect=text5.get_rect()
                            text5_rect.center=(150,330)
                            manhinh.blit(text5,text5_rect)
                            #
                            clicked=pygame.mouse.get_pressed()[0]
                            def click():
                                if clicked==True:
                                        return False
                            clicked=click()
                            mouse_x=pygame.mouse.get_pos()[0]
                            mouse_y=pygame.mouse.get_pos()[1]
                            #
                            if  mouse_x in range(600,701) and mouse_y in range(200,251) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu12_path = os.path.join(script_dir, "dung.wav")
                                pygame.mixer.music.load(musicvu12_path)
                                pygame.mixer.music.play()
                                gameplay=True
                                pressvc=True
                                ranques=ranques+1
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                texta=font.render(f'Correct Answer. Goob job',True,(255,255,255))
                                texta_rect=texta.get_rect()
                                texta_rect.center=(400,450)
                                manhinh.blit(texta,texta_rect)
                            elif mouse_x in range(600,701) and mouse_y in range(300,351) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu6_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu6_path)
                                pygame.mixer.music.play()
                                answer=False
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            elif mouse_x in range(100,201) and mouse_y in range(200,251) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu62_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu62_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            elif mouse_x in range(100,201) and mouse_y in range(300,351) and clicked==False:   
                                pygame.init()
                                pygame.mixer.init()
                                musicvu63_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu63_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            pygame.display.update()  
                        if ranques==2: 
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,150,800,50))
                            text1a=font.render(f'Question 2: When was Open Lab established?',True,(255,255,255))
                            text1a_rect=text1a.get_rect()
                            text1a_rect.center=(400,180)
                            manhinh.blit(text1a,text1a_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,200,100,50))
                            text2a=font.render(f'A.2009',True,(255,255,255))
                            text2a_rect=text2a.get_rect()
                            text2a_rect.center=(150,230)
                            manhinh.blit(text2a,text2a_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,200,100,50))
                            text3a=font.render(f'B.2011',True,(255,255,255))
                            text3a_rect=text3a.get_rect()
                            text3a_rect.center=(650,230)
                            manhinh.blit(text3a,text3a_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,300,100,50))
                            text4a=font.render(f'D.2012',True,(255,255,255))
                            text4a_rect=text4a.get_rect()
                            text4a_rect.center=(650,330)
                            manhinh.blit(text4a,text4a_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,300,100,50))
                            text5a=font.render(f'C.2010',True,(255,255,255))
                            text5a_rect=text5a.get_rect()
                            text5a_rect.center=(150,330)
                            manhinh.blit(text5a,text5a_rect)
                            #
                            clicked=pygame.mouse.get_pressed()[0]
                            def click():
                                if clicked==True:
                                        return False
                            clicked = click()
                            mouse_x=pygame.mouse.get_pos()[0]
                            mouse_y=pygame.mouse.get_pos()[1]
                            #
                            if  mouse_x in range(100,201) and mouse_y in range(300,351) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu123_path = os.path.join(script_dir, "dung.wav")
                                pygame.mixer.music.load(musicvu123_path)
                                pygame.mixer.music.play()
                                answer=True
                                gameplay=True
                                pressvc=True
                                ranques=ranques+1
                            elif mouse_x in range(600,701) and mouse_y in range(300,351) and clicked==False:
                                
                                pygame.init()
                                pygame.mixer.init()
                                musicvu611_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu611_path)
                                pygame.mixer.music.play()
                                answer=False
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6a=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6a_rect=text6a.get_rect()
                                text6a_rect.center=(400,450)
                                manhinh.blit(text6a,text6a_rect)
                            elif mouse_x in range(100,201) and mouse_y in range(200,251) and clicked==False:
                                                        
                                pygame.init()
                                pygame.mixer.init()
                                musicvu612_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu612_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6a=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6a_rect=text6a.get_rect()
                                text6a_rect.center=(400,450)
                                manhinh.blit(text6a,text6a_rect)
                            elif mouse_x in range(600,701) and mouse_y in range(200,251) and clicked==False:                           
                                pygame.init()
                                pygame.mixer.init()
                                musicvu633_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu633_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6a=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6a_rect=text6a.get_rect()
                                text6a_rect.center=(400,450)
                                manhinh.blit(text6a,text6a_rect)
                            pygame.display.update()
                        if ranques == 3:
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,150,800,50))
                            text1b=font.render(f'Question 3: How many majors is 3i Institute training (as of 2023)?',True,(255,255,255))
                            text1b_rect=text1b.get_rect()
                            text1b_rect.center=(400,180)
                            manhinh.blit(text1b,text1b_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,200,100,50))
                            text2b=font.render(f'2',True,(255,255,255))
                            text2b_rect=text2b.get_rect()
                            text2b_rect.center=(150,230)
                            manhinh.blit(text2b,text2b_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,200,100,50))
                            text3b=font.render(f'4',True,(255,255,255))
                            text3b_rect=text3b.get_rect()
                            text3b_rect.center=(650,230)
                            manhinh.blit(text3b,text3b_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(600,300,100,50))
                            text4b=font.render(f'3',True,(255,255,255))
                            text4b_rect=text4b.get_rect()
                            text4b_rect.center=(650,330)
                            manhinh.blit(text4b,text4b_rect)
                            #
                            pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(100,300,100,50))
                            text5b=font.render(f'5',True,(255,255,255))
                            text5b_rect=text5b.get_rect()
                            text5b_rect.center=(150,330)
                            manhinh.blit(text5b,text5b_rect)
                            #
                            clicked=pygame.mouse.get_pressed()[0]
                            def click():
                                if clicked==True:
                                        return False
                            clicked=click()
                            mouse_x=pygame.mouse.get_pos()[0]
                            mouse_y=pygame.mouse.get_pos()[1] 
                            #
                            if  mouse_x in range(100,201) and mouse_y in range(200,251) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu1222_path = os.path.join(script_dir, "dung.wav")
                                pygame.mixer.music.load(musicvu1222_path)
                                pygame.mixer.music.play()
                                answer=True
                                gameplay=True
                                pressvc=True
                            elif mouse_x in range(600,701) and mouse_y in range(300,351) and clicked==False:
                                pygame.init()
                                pygame.mixer.init()
                                musicvu6555_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu6555_path)
                                pygame.mixer.music.play()
                                answer=False
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            elif mouse_x in range(600,701) and mouse_y in range(200,251) and clicked==False:                               
                                pygame.init()
                                pygame.mixer.init()
                                musicvu6122_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu6122_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            elif mouse_x in range(100,201) and mouse_y in range(300,351) and clicked==False:                                                     
                                pygame.init()
                                pygame.mixer.init()
                                musicvu6111_path = os.path.join(script_dir, "sai.wav")
                                pygame.mixer.music.load(musicvu6111_path)
                                pygame.mixer.music.play()
                                answer=False 
                                gameplay=False
                                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(200,400,400,100))
                                font=pygame.font.Font(pygame.font.get_default_font(),20)
                                text6=font.render(f'Wrong answer. Please choose again',True,(255,255,255))
                                text6_rect=text6.get_rect()
                                text6_rect.center=(400,450)
                                manhinh.blit(text6,text6_rect)
                            pygame.display.update()                           
                        if gameplay==True and t in [10] and answer==True and ranques==3:
                                    truck_x=400
                                    manhinh.blit(sky,(0,0))
                                    manhinh.blit(bg,(0,30))
                                    manhinh.blit(road,(0,530))
                                    manhinh.blit(cloud,(30,100))
                                    manhinh.blit(cloud,(400,50))
                                    manhinh.blit(sun,(550,0))
                                    manhinh.blit(chot_scale,chot_hcn)
                                    manhinh.blit(chot_scale,(chot_hcn.centerx,chot_hcn.centery-50))
                                    truck_hcn.centerx=truck_x 
                                    truck_hcn.centery=truck_y
                                    manhinh.blit(truck,truck_hcn)
                                    pygame.display.update()
            if gameplay and t in [10]:
                        manhinh.blit(sky,(0,0))
                        manhinh.blit(bg,(0,30))
                        manhinh.blit(road,(0,530))
                        manhinh.blit(cloud,(30,100))
                        manhinh.blit(cloud,(400,50))
                        manhinh.blit(sun,(550,0)) 
                        manhinh.blit(chot_scale,chot_hcn)
                        manhinh.blit(chot_scale,(chot_hcn.centerx,chot_hcn.centery-50))
                        truck_hcn.centery=truck_y
                        truck_hcn.centerx=truck_x
                        manhinh.blit(truck,truck_hcn)
                        pygame.display.update()
            if gameplay and t in [0,2,4,6,8,11]:
                    manhinh.blit(sky,(0,0))
                    manhinh.blit(bg,(0,30))
                    manhinh.blit(road,(0,530))
                    manhinh.blit(cloud,(30,100))
                    manhinh.blit(cloud,(400,50))
                    manhinh.blit(sun,(550,0)) 
                    truck_hcn.centery=truck_y
                    truck_hcn.centerx=truck_x
                    manhinh.blit(truck,truck_hcn)
                    pygame.display.update()
            if gameplay and t in [1,5,9]:
                    manhinh.blit(sky,(0,0))
                    manhinh.blit(bg,(0,30))
                    manhinh.blit(road,(0,530))
                    manhinh.blit(cloud,(30,100))
                    manhinh.blit(cloud,(400,50))
                    manhinh.blit(sun,(550,0))
                    if car_y==600:
                        car_hcn.centerx=car_x
                        car_hcn.centery=car_y
                        manhinh.blit(car,car_hcn)
                        truck_hcn.centery=truck_y
                        truck_hcn.centerx=truck_x
                        manhinh.blit(truck,truck_hcn)
                    if car_y==700: 
                        truck_hcn.centery=truck_y
                        truck_hcn.centerx=truck_x
                        manhinh.blit(truck,truck_hcn)
                        car_hcn.centerx=car_x
                        car_hcn.centery=car_y
                        manhinh.blit(car,car_hcn)
                    pygame.display.update()
            if gameplay and t in [3,7]:
                    manhinh.blit(sky,(0,0))
                    manhinh.blit(bg,(0,30))
                    manhinh.blit(road,(0,530))
                    manhinh.blit(cloud,(30,100))
                    manhinh.blit(cloud,(400,50))
                    manhinh.blit(sun,(550,0))
                    if car2_y==600:
                        car2_hcn.centerx=car2_x
                        car2_hcn.centery=car2_y
                        manhinh.blit(car2,car2_hcn) 
                        truck_hcn.centery=truck_y
                        truck_hcn.centerx=truck_x
                        manhinh.blit(truck,truck_hcn)
                    if car2_y==700:
                        truck_hcn.centery=truck_y
                        truck_hcn.centerx=truck_x
                        manhinh.blit(truck,truck_hcn)
                        car2_hcn.centerx=car2_x
                        car2_hcn.centery=car2_y
                        manhinh.blit(car2,car2_hcn) 
                    pygame.display.update()
            if gameplay and t==12:
                manhinh.blit(sky2,(0,-30))
                manhinh.blit(bg2,(100,170))
                manhinh.blit(road,(0,530))
                manhinh.blit(sun,(550,0))
                if truck_x<400:
                    truck_hcn.centery=truck_y
                    truck_hcn.centerx=truck_x
                    manhinh.blit(truck,truck_hcn)
                if truck_x>=400:
                    gameover=font.render(f'You have reached UEH. You win!!!',True,(255,255,255))                    
                    manhinh.blit(truck,truck_hcn)
                    pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,100,800,100))
                    font=pygame.font.Font(pygame.font.get_default_font(),30)
                    gameover_rect=gameover.get_rect()
                    gameover_rect.center=(400,150)
                    manhinh.blit(gameover,gameover_rect)
                pygame.display.update()                  
            if gameplay==False and t in [1,5,9]:
                manhinh.blit(sky,(0,0))
                manhinh.blit(bg,(0,30))
                manhinh.blit(road,(0,530))
                manhinh.blit(cloud,(30,100))
                manhinh.blit(cloud,(400,50))
                manhinh.blit(sun,(550,0))
                manhinh.blit(car,car_hcn)
                manhinh.blit(truck,truck_hcn)
                manhinh.blit(crash,(truck_hcn.right-150, truck_hcn.centery-100))
                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,100,800,100))
                font=pygame.font.Font(pygame.font.get_default_font(),30)
                gameover=font.render(f'Game over!! Press space to play again.',True,(255,255,255))
                gameover_rect=gameover.get_rect()
                gameover_rect.center=(400,150)
                manhinh.blit(gameover,gameover_rect)
                pygame.display.update()
            if gameplay==False and t in [3,7]:
                manhinh.blit(sky,(0,0))
                manhinh.blit(bg,(0,30))
                manhinh.blit(road,(0,530))
                manhinh.blit(cloud,(30,100))
                manhinh.blit(cloud,(400,50))
                manhinh.blit(sun,(550,0))
                manhinh.blit(car2,car2_hcn)
                manhinh.blit(truck,truck_hcn)
                manhinh.blit(crash,(truck_hcn.right-150, truck_hcn.centery-100))
                pygame.draw.rect(manhinh,(255,0,0),pygame.Rect(0,100,800,100))
                font=pygame.font.Font(pygame.font.get_default_font(),30)
                gameover=font.render(f'Game over!! Press Space to play again.',True,(255,255,255))
                gameover_rect=gameover.get_rect()
                gameover_rect.center=(400,150)
                manhinh.blit(gameover,gameover_rect)
                pygame.display.update()
          
    #End new game
    # Control Panels
    def right(event):
        if canvas.coords(truck)[0] < 680:
            canvas.move(truck, 20, 0)
    def left(event):
        if canvas.coords(truck)[0] > 0:
            canvas.move(truck, -20, 0)

    canvas.bind_all("<KeyPress-Right>", right)
    canvas.bind_all("<KeyPress-Left>", left)

    # Schedule the first call after 50 milliseconds
    game.after(50, PickingContainers)
    game.mainloop()

# Create the main window
root = tk.Tk()
root.title("Picking Containers")

# Create elements in the interface
# Function to show Donate

def open_donation_link():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    musicvu_path = os.path.join(script_dir, "bip.wav")
    pygame.mixer.music.load(musicvu_path)
    pygame.mixer.music.play()
    webbrowser.open("https://youtube.com/@soccershortclip147?si=x9YMaANdS-0t9Hwm")

# Function to show instructions
def show_instructions():
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    musicvu_path = os.path.join(script_dir, "bip.wav")
    pygame.mixer.music.load(musicvu_path)
    pygame.mixer.music.play()
    instructions_window = tk.Toplevel(root)
    instructions_window.title("Instructions")
    instructions_label = tk.Label(instructions_window, text="You have to pick up 📦containers for the customers.\n In each containers, there are a lot of gadgets that support our studying such as: 📚books,📝pen,📝pencils,..\n The customers, in this case, are UEHers (presumably members of the University of Economics 🎓 Ho Chi Minh City).\n Once you have enough containers, you drive your 🚗 car to the university to deliver them. Before doing so, you need to pass a poll by answering some questions.\n Good luck to you! 👍", font=("Arial", 12))
    instructions_label.pack(padx=20, pady=20)
    # Set a different background color
    instructions_window.configure(bg="lightgray")

# Create elements in the interface  
label = tk.Label(root, text="Final project of Computer Science by: 3TM", font=("Time", 15), bg="white")
start_button = tk.Button(root, text="Start Game", font=("Arial", 12), command=start_game)
exit_button = tk.Button(root, text="Exit Game", font=("Arial", 12), command=exit_game)
donate_button = tk.Button(root, text="Donate", font=("Arial", 12), command= open_donation_link)
instructions_button = tk.Button(root, text="Instructions", font=("Arial", 12), command=show_instructions)

# Set the position and size of elements in the window
label.pack(pady=20)
start_button.pack(pady=10)
exit_button.pack(pady=10)
donate_button.pack(pady=10)
instructions_button.pack(pady=10)

# Configure the size of the window
window_width = 800
window_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Start the event loop
root.mainloop()
