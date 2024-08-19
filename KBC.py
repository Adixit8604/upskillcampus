import pygame, sys
from pygame import *
from pygame.locals import *
import mysql.connector as sqlcon
import random
import time
from datetime import date

volume=0.03
p_level=0
n_level=0
level=()
down=0
i=0 

message=0
check=[5,9]
check_cash=0
life_line=0
breaking=1
life1="Images\half.png"
life2="Images\Double_Dip.png"
life3="Images\joker.png"
life4="Images\RaveSwitch.png"

q=[" ",(14,23,82),(100,355),(90,350)]
o1=[" ",(14,23,82),(110,460),(104,452)]
o2=[" ",(14,23,82),(530,460),(524,452)]
o3=[" ",(14,23,82),(110,535),(104,526)]
o4=[" ",(14,23,82),(530,535),(524,526)]
ans_text=[" ",(1),(2)]

Ques_Data = [
    [1, "Q) What Flies?", "Elephant", "Dog", "Eagle", "Lion", "Eagle", "Easy"],
    [2, "Q) What Barks?", "Dog", "Elephant", "Lion", "Eagle", "Dog", "Easy"],
    [3, "Q) What Has Trunk?", "Lion", "Dog", "Eagle", "Elephant", "Elephant", "Easy"],
    [4, "Q) What Roars?", "Elephant", "Eagle", "Dog", "Lion", "Lion", "Easy"],
    [5, "Q) What Meows?", "Cat", "Dog", "Rat", "Lion", "Cat", "Easy"],
    [6, "Q) What Lives in holes?", "Crane", "Dog", "Rabbit", "Lion", "Rabbit", "Easy"],
    [7, "Q) Which is an insect?", "Elephant", "Ant", "Eagle", "Lion", "Ant", "Easy"],
    [8, "Q) What Hisses?", "Elephant", "Dog", "Eagle", "Snake", "Snake", "Easy"],
    [9, "Q) Which has a long neck?", "Giraffe", "Dog", "Eagle", "Lion", "Giraffe", "Easy"],
    [10, "Q) Which is human-like?", "Elephant", "Ape", "Eagle", "Lion", "Ape", "Easy"],
    [11, "Q) Which animal hops?", "Dog", "Frog", "Cat", "Lion", "Frog", "Easy"],
    [12, "Q) What has spots?", "Elephant", "Dog", "Cheetah", "Lion", "Cheetah", "Easy"],
    [13, "Q) What animal is known as the king of the jungle?", "Elephant", "Dog", "Eagle", "Lion", "Lion", "Easy"],
    [14, "Q) What animal has tusks?", "Elephant", "Dog", "Lion", "Eagle", "Elephant", "Easy"],
    [15, "Q) What is known for its speed?", "Cheetah", "Dog", "Elephant", "Lion", "Cheetah", "Easy"],
    [16, "Q) Which has the thickest fur of any mammal?", "Bear", "Red Fox", "Lion", "Sea Otter", "Sea Otter", "Difficult"],
    [17, "Q) The age of a lion can be determined by its…?", "Nose", "Ear", "Teeth", "Tail", "Nose", "Difficult"],
    [18, "Q) What animal has the highest blood pressure?", "Elephant", "Giraffe", "Eagle", "Lion", "Giraffe", "Difficult"],
    [19, "Q) What type of farm animal can sunburn?", "Cow", "Horse", "Pig", "Hen", "Pig", "Difficult"],
    [20, "Q) What is the closest living relative to the T-rex?", "Elephant", "Dog", "Eagle", "Chicken", "Chicken", "Difficult"],
    [21, "Q) What male sea creature gives birth to its young?", "Sea Cucumber", "Seahorse", "Sea Oyster", "Goldfish", "Seahorse", "Difficult"],
    [22, "Q) Which sea creature can change its gender?", "Sea Cucumber", "Seahorse", "Oyster", "Goldfish", "Oyster", "Difficult"],
    [23, "Q) What is the deadliest creature in the world?", "Mosquito", "Shark", "Whale", "Elephant", "Mosquito", "Difficult"],
    [24, "Q) What type of fish mate for life?", "Shark", "Angelfish", "Blue Whale", "Star Fish", "Angelfish", "Difficult"],
    [25, "Q) What is a polar bear's skin color?", "White", "Brown", "Red", "Black", "Black", "Difficult"],
    [26, "Q) What is the largest animal on Earth?", "Elephant", "Blue Whale", "Shark", "Giraffe", "Blue Whale", "Difficult"],
    [27, "Q) Which animal never sleeps?", "Shark", "Elephant", "Lion", "Giraffe", "Shark", "Difficult"],
    [28, "Q) Which animal has the strongest bite?", "Lion", "Tiger", "Hippopotamus", "Crocodile", "Crocodile", "Difficult"],
    [29, "Q) Which animal can regrow its limbs?", "Starfish", "Shark", "Crab", "Octopus", "Starfish", "Difficult"],
    [30, "Q) What animal can recognize itself in a mirror?", "Dog", "Elephant", "Lion", "Dolphin", "Dolphin", "Difficult"]
]


frame_count = 0
frame_rate = 60
start_time = 30

music_button="Images\off_button.png"
music="off"
sound_button="Images\on_button.png"
sound="on"
mode_button="Images\off_button.png"
mode="Easy"
def pressed_start():
    if (event.type==pygame.MOUSEBUTTONDOWN):
        if(pygame.mouse.get_pressed()):
            if sound=="on":
                theme.play()
            Start_Game()


def Start_Game():
    global p_level,down,q,o1,o2,o3,o4,ans_text,correct,o3_space,wrong,n_level,level,i,life1,life2,life3,life4
    global Prize_pointer_x,Prize_pointer_y,frame_count,frame_rate,message,check,check_cash,life_line,breaking
    Prize_pointer_x=725
    Prize_pointer_y=275
    frame_count=0
    correct=0
    wrong=0
    down=0
    start=1
    while True:
        DISPLAYSURF.blit(background,(0,0))
        Q_space=pygame.Surface([725,70],pygame.SRCALPHA,32)
        Q_space.fill(q[1])
        Q_space.convert_alpha()
        Q_space_mask=pygame.mask.from_surface(Q_space)
    
        o1_space=pygame.Surface([302,50],pygame.SRCALPHA,32)
        o1_space.fill(o4[1])
        o1_space.convert_alpha()
        o1_space_mask=pygame.mask.from_surface(o1_space)

        o2_space=pygame.Surface([302,50],pygame.SRCALPHA,32)
        o2_space.fill(o4[1])
        o2_space.convert_alpha()
        o2_space_mask=pygame.mask.from_surface(o2_space)

        o3_space=pygame.Surface([302,50],pygame.SRCALPHA,32)
        o3_space.fill(o4[1])
        o3_space.convert_alpha()
        o3_space_mask=pygame.mask.from_surface(o3_space)
  
        o4_space=pygame.Surface([302,50],pygame.SRCALPHA,32)
        o4_space.fill(o4[1])
        o4_space.convert_alpha()
        o4_space_mask=pygame.mask.from_surface(o4_space)

        score_board=pygame.Surface([200,300],pygame.SRCALPHA,32)
        score_board.fill((14,23,82))
        
            


        if (start==2 and sound=="on"):
            time.sleep(6.5)
        elif(start>=2):
            
            DISPLAYSURF.blit(Quiz,(0,300))

            DISPLAYSURF.blit(Q_space,q[3])
            DISPLAYSURF.blit(o1_space,o1[3])
            DISPLAYSURF.blit(o2_space,o2[3])
            DISPLAYSURF.blit(o3_space,o3[3])
            DISPLAYSURF.blit(o4_space,o4[3])
            DISPLAYSURF.blit(score_board,(700,0))
            places=[(104,452),(524,452),(104,526),(524,526)]
            blit_start_game()
            for l in [o1,o2,o3,o4]:
                if ans_text[0]==l[0]:
                    ans_text[1]=l[3]
                    ans_text[2]=l[2]

            fifty=pygame.image.load(life1).convert_alpha()
            fifty_mask=pygame.mask.from_surface(fifty)
            double=pygame.image.load(life2).convert_alpha()
            double_mask=pygame.mask.from_surface(double)
            joker=pygame.image.load(life3).convert_alpha()
            joker_mask=pygame.mask.from_surface(joker)
            switch=pygame.image.load(life4).convert_alpha() 
            switch_mask=pygame.mask.from_surface(switch)

            DISPLAYSURF.blit(fifty,(30,10))
            DISPLAYSURF.blit(double,(30,90))
            DISPLAYSURF.blit(joker,(30,170))
            DISPLAYSURF.blit(switch,(30,250)) 
            if pointer_mask.overlap(fifty_mask,(30-pointer_rect.left,10-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down== 1):
                    if(pygame.mouse.get_pressed()):
                        if life1=="Images\half.png":
                            life1="Images\o-half.png"
                            places.remove(ans_text[1])
                            position=random.sample(places,k=2)
                            places.append(ans_text[1])
                            life_line=1
                        down=0

            elif pointer_mask.overlap(double_mask,(30-pointer_rect.left,90-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed()):
                        if life2=="Images\Double_Dip.png":
                            life2="Images\o-Double_Dip.png"
                            breaking=2
                        down=0

            elif pointer_mask.overlap(joker_mask,(30-pointer_rect.left,170-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed()):
                        if life3=="Images\joker.png":
                            life3="Images\o-joker.png"
                            life_line=3
                        down=0

            elif pointer_mask.overlap(switch_mask,(30-pointer_rect.left,250-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed(5)):
                        if life4=="Images\RaveSwitch.png":
                            life4="Images\o-RaveSwitch.png"
                            if(mode=="Easy"):
                                q_num=random.choice([i for i in range(0,15) if i not in level])
                            else:
                                q_num=random.choice([i for i in range(15,30) if i not in level])
                            data=Ques_Data[q_num]
                            q[0]=data[1]
                            o1[0]=data[2]
                            o2[0]=data[3]
                            o3[0]=data[4]
                            o4[0]=data[5]
                            ans_text[0]=data[6]
                            level=level +(q_num,)
                            life_line=0
                        down=0
            
           
            if(len(level)<=4):
                font_clock = pygame.font.SysFont("monospace", 25)
                total_seconds = frame_count // frame_rate

                total_seconds = 30 - (frame_count // frame_rate)
                if total_seconds < 0:
                    total_seconds = 0
 
                # Use modulus (remainder) to get seconds
                seconds = total_seconds % 60
 
                # Use python string formatting to format in leading zeros
                output_string = "{0:00}".format(seconds)
                if (seconds==30 and sound=="on"):
                    clock_tick.play()
                elif(seconds==0):
                    clock_tick.stop()
                    if sound=="on":
                        end_buzz.play()
                    time.sleep(2.0)
                    level=()
                    break
                # Blit to the screen
                text_clock = font_clock.render(output_string, True, "yellow")
 
                DISPLAYSURF.blit(text_clock, [430, 270])
 
                # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
                frame_count += 1 
            
            


            
            
            if pointer_mask.overlap(o1_space_mask,(105-pointer_rect.left,455-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed(3)):
                        if (o1[0]==ans_text[0]):
                            i=1
                            frame_count=0
                            clock_tick.stop()
                        else:
                            i=5
                            frame_count=0
                            clock_tick.stop()

            elif pointer_mask.overlap(o2_space_mask,(525-pointer_rect.left,455-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed(3)):
                        if (o2[0]==ans_text[0]):
                            i=2
                            frame_count=0
                            clock_tick.stop()
                        else:
                            i=6
                            frame_count=0
                            clock_tick.stop()
                        
            elif pointer_mask.overlap(o3_space_mask,(105-pointer_rect.left,530-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed(3)):
                        if (o3[0]==ans_text[0]):
                            i=3
                            frame_count=0
                            clock_tick.stop()
                        else:
                            i=7
                            frame_count=0
                            clock_tick.stop()
                            
            
                                
            if pointer_mask.overlap(o4_space_mask,(525-pointer_rect.left,530-pointer_rect.top)):
                if (event.type==pygame.MOUSEBUTTONDOWN):
                    down=1
                if (event.type==pygame.MOUSEBUTTONUP and down==1):
                    if(pygame.mouse.get_pressed(3)):
                        if (o4[0]==ans_text[0]):
                            i=4
                            frame_count=0
                            clock_tick.stop()
                        else:
                            i=8
                            frame_count=0
                            clock_tick.stop()
            if (i==1):

                correct3=pygame.Surface([302,50],pygame.SRCALPHA,32)
                correct3.fill((146,208,80))
                DISPLAYSURF.blit(correct3,(104,452))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o1[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o1[2])
                
                if (correct==1):
                    if sound=="on":
                        correct_ans.play()
                    time.sleep(6.0) 
                elif(correct==2): 
                    p_level+=1
                    Prize_pointer_y=Prize_pointer_y-20
                    down=0
                elif(correct>=3):
                    correct=-1
                    i=0
                    clock_tick.stop()
                correct+=1
            if (i==2):
                correct3=pygame.Surface([302,50],pygame.SRCALPHA,32)
                correct3.fill((146,208,80))
                DISPLAYSURF.blit(correct3,(524,452))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o2[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o2[2])
                if (correct==1):
                    if sound=="on":
                        correct_ans.play()
                    time.sleep(6.0) 
                elif(correct==2): 
                    p_level+=1
                    Prize_pointer_y=Prize_pointer_y-20
                    down=0
                elif(correct>=3):
                    correct=-1
                    i=0
                    clock_tick.stop()
                correct+=1
            if (i==3):
                correct3=pygame.Surface([302,50],pygame.SRCALPHA,32)
                correct3.fill((146,208,80))
                DISPLAYSURF.blit(correct3,(104,526))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o3[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o3[2])
                if (correct==1):
                    if sound=="on":
                        correct_ans.play()
                    time.sleep(6.0) 
                elif(correct==2):  
                    p_level+=1
                    Prize_pointer_y=Prize_pointer_y-20
                    down=0
                elif(correct>=3):
                    correct=-1
                    i=0
                    clock_tick.stop()
                correct+=1
            if (i==4):
                correct3=pygame.Surface([302,50],pygame.SRCALPHA,32)
                correct3.fill((146,208,80))
                DISPLAYSURF.blit(correct3,(524,526))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o4[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o4[2])
                if (correct==1):
                    if sound=="on":
                        correct_ans.play()
                    time.sleep(6.0) 
                elif(correct==2): 
                    p_level+=1
                    Prize_pointer_y=Prize_pointer_y-20
                    down=0
                elif(correct>=3):
                    correct=-1
                    i=0
                    clock_tick.stop()
                correct+=1
            if (i==5):
                
                wrong1=pygame.Surface([302,50],pygame.SRCALPHA,32)
                wrong1.fill((255,0,0))
                DISPLAYSURF.blit(wrong1,(104,452))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o1[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o1[2])
                if (wrong==1):
                    if sound=="on":
                        wrong_ans.play()
                    time.sleep(3.0) 
                elif(wrong==2):
                    clock_tick.stop()
                    if breaking==1:
                        p_level=0
                        n_level=0
                        level=()
                        down=0
                        i=0
                        break
                    if breaking==2:
                        breaking-=1
                        wrong=0
                        i=0
                wrong+=1
            
            if (i==6):
                
                wrong1=pygame.Surface([302,50],pygame.SRCALPHA,32)
                wrong1.fill((255,0,0))
                DISPLAYSURF.blit(wrong1,(524,452))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o2[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o2[2])
                if (wrong==1):
                    if sound=="on":
                        wrong_ans.play()
                    time.sleep(3.0) 
                elif(wrong==2): 
                    clock_tick.stop()
                    if breaking==1:
                        p_level=0
                        n_level=0
                        level=()
                        down=0
                        i=0
                        break
                    if breaking==2:
                        breaking-=1
                        wrong=0
                        i=0
                wrong+=1
            
            if (i==7):
                
                wrong1=pygame.Surface([302,50],pygame.SRCALPHA,32)
                wrong1.fill((255,0,0))
                DISPLAYSURF.blit(wrong1,(104,526))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o3[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o3[2])
                if (wrong==1):
                    if sound=="on":
                        wrong_ans.play()
                    time.sleep(3.0) 
                elif(wrong==2): 
                    clock_tick.stop()
                    if breaking==1:
                        p_level=0
                        n_level=0
                        level=()
                        down=0
                        i=0
                        break
                    if breaking==2:
                        breaking-=1
                        wrong=0
                        i=0

                wrong+=1
            
            if (i==8):
                
                wrong1=pygame.Surface([302,50],pygame.SRCALPHA,32)
                wrong1.fill((255,0,0))
                DISPLAYSURF.blit(wrong1,(524,526))
                text_font=pygame.font.SysFont("monospace",25)
                choice=text_font.render(o4[0],1,(0,0,0))
                DISPLAYSURF.blit(choice,o4[2])
                
                if (wrong==1):
                    if sound=="on":
                        wrong_ans.play()
                    time.sleep(3.0) 
                elif(wrong==2): 
                    
                    clock_tick.stop()
                    if breaking==1:
                        p_level=0
                        n_level=0
                        level=()
                        down=0
                        i=0
                        break
                    if breaking==2:
                        breaking-=1
                        wrong=0
                        i=0
                wrong+=1

            winner=pygame.Surface([700,400])
            winner.fill((255,255,255))
            check_pic= pygame.image.load("Images\prize_check.png") 
            check_font=pygame.font.SysFont("monospace",13)
            recent=str(date.today().strftime("%d/%m/%Y"))

            today=check_font.render(recent,1,(0,0,0))
            
            if (life_line==1):
                for k in position:
                    Binta_surface=pygame.Surface([302,50])
                    Binta_surface.fill((14,23,82))
                    DISPLAYSURF.blit(Binta_surface,k)
            
            elif(life_line==3):
                DISPLAYSURF.blit(winner,(100,50))
                ans_font=pygame.font.SysFont("monospace",30)
                ans="The answer is "+ans_text[0]
                answer=ans_font.render(ans,1,(0,0,0))
                DISPLAYSURF.blit(answer,(140,70))

                continue_pic= pygame.image.load("Images\message-continue.png").convert_alpha()
                continue_mask=pygame.mask.from_surface(continue_pic)
                DISPLAYSURF.blit(continue_pic,(215,350))
                if pointer_mask.overlap(continue_mask,(215-pointer_rect.left,350-pointer_rect.top)):
                        if (event.type==pygame.MOUSEBUTTONDOWN):
                            down=1
                        if (event.type==pygame.MOUSEBUTTONUP and down==1):
                            if(pygame.mouse.get_pressed(3)):
                                life_line=0


            if len(level)>12:
                check_text_value="1,00,00,000"
                
                DISPLAYSURF.blit(winner,(100,50))
                DISPLAYSURF.blit(check_pic,(220,70))
                DISPLAYSURF.blit(today,(580,135))
                check_text=check_font.render(check_text_value,1,(0,0,0))
                DISPLAYSURF.blit(check_text,(565,165))

                home_pic= pygame.image.load("Images\message-home.png").convert_alpha()
                home_mask=pygame.mask.from_surface(home_pic)
                DISPLAYSURF.blit(home_pic,(215,350))
                if (sound=="on"):
                    crore=pygame.mixer.Sound("Audio/crore.wav")
                    crore.play(1)
                quit_pic= pygame.image.load("Images\message-quit.png").convert_alpha()
                quit_mask=pygame.mask.from_surface(quit_pic)
                DISPLAYSURF.blit(quit_pic,(565,350))
                
                if pointer_mask.overlap(home_mask,(215-pointer_rect.left,350-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            level=()
                            break
                
                if pointer_mask.overlap(quit_mask,(565-pointer_rect.left,350-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            quit()
            
            if len(level) in check:
                check_cash=len(level)
                message=1
                if (len(level)==5):
                    check_text_value="40,000"
                elif (len(level)==9):
                    check_text_value="6,40,000"
                if message==1:

                    DISPLAYSURF.blit(winner,(100,50))
                    DISPLAYSURF.blit(check_pic,(220,70))
                    DISPLAYSURF.blit(today,(580,135))
                    check_text=check_font.render(check_text_value,1,(0,0,0))
                    DISPLAYSURF.blit(check_text,(565,165))

                    continue_pic= pygame.image.load("Images\message-continue.png").convert_alpha()
                    continue_mask=pygame.mask.from_surface(continue_pic)
                    DISPLAYSURF.blit(continue_pic,(215,350))

                    home_pic= pygame.image.load("Images\message-quit.png").convert_alpha()
                    home_mask=pygame.mask.from_surface(home_pic)
                    DISPLAYSURF.blit(home_pic,(565,350))

                    if pointer_mask.overlap(continue_mask,(215-pointer_rect.left,350-pointer_rect.top)):
                        if (event.type==pygame.MOUSEBUTTONDOWN):
                            down=1
                        if (event.type==pygame.MOUSEBUTTONUP and down==1):
                            if(pygame.mouse.get_pressed(3)):
                                message=0
                                check.remove(check_cash)

                    if pointer_mask.overlap(home_mask,(565-pointer_rect.left,350-pointer_rect.top)):
                        if (event.type==pygame.MOUSEBUTTONDOWN):
                            down=1
                        if (event.type==pygame.MOUSEBUTTONUP and down==1):
                            if(pygame.mouse.get_pressed(3)):
                                level=()
                                break    
                        
            if pygame.mouse.get_pos():
                pointer_rect.center=pygame.mouse.get_pos()
            DISPLAYSURF.blit(pointer,pointer_rect)
            pygame.mouse.set_visible(False)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
        start+=1
        pygame.display.update()
        clock.tick(80)

def blit_start_game():
    global q,o1,o2,o3,o4,ans_text,Prize_pointer_x,Prize_pointer_y,down
    global p_level,n_level,level,life_line,breaking
    
    if(p_level==n_level):
        if(mode=="Easy"):
            q_num=random.choice([i for i in range(0,15) if i not in level])
        else:
            q_num=random.choice([i for i in range(15,30) if i not in level])      
        
        if q_num in level:
            blit_start_game()
        else:
            data=Ques_Data[q_num]
            q[0]=data[1]
            o1[0]=data[2]
            o2[0]=data[3]
            o3[0]=data[4]
            o4[0]=data[5]
            ans_text[0]=data[6]
            level=level +(q_num,)
            n_level=n_level+1
            life_line=0
            breaking=1
        
    if pygame.mouse.get_pos():
        pointer_rect.center=pygame.mouse.get_pos()
    DISPLAYSURF.blit(pointer,pointer_rect)
    pygame.mouse.set_visible(False)

    Prize_pointer=pygame.image.load("Images\prize_pointer.png")
    
    DISPLAYSURF.blit(Prize_pointer,(Prize_pointer_x,Prize_pointer_y))
    
    text_font=pygame.font.SysFont("monospace",25)
    prize_font=pygame.font.SysFont("monospace",20)

    Ques=text_font.render(q[0],1,(200,161,68))
    Option_1=text_font.render(o1[0],1,(200,161,68))
    Option_2=text_font.render(o2[0],1,(200,161,68))
    Option_3=text_font.render(o3[0],1,(200,161,68))
    Option_4=text_font.render(o4[0],1,(200,161,68))
    
    money=["12. ₹1 crore","11. ₹50,00,000","10. ₹25,00,000"," 9. ₹12,50,000"," 8. ₹6,40,000"," 7. ₹3,20,000"," 6. ₹1,60,000"," 5. ₹80,000"," 4. ₹40,000"," 3. ₹20,000"," 2. ₹10,000"," 1. ₹5,000"]
    
    for i in range(0,len(money)):
        if (i%4==0):
            check_colour=(255,255,255)
        else:
            check_colour=(200,161,68)
        
        Prize=prize_font.render(money[i],1,check_colour)
        DISPLAYSURF.blit(Prize,(740,10+((i+1)*10)+(10*(i+1))))
    
    DISPLAYSURF.blit(Ques,q[2])  
    DISPLAYSURF.blit(Option_1,o1[2])
    DISPLAYSURF.blit(Option_2,o2[2])
    DISPLAYSURF.blit(Option_3,o3[2])
    DISPLAYSURF.blit(Option_4,o4[2])

def setting():
    global pointer,pointer_mask,pointer_rect,music_button,sound_button,mode_button
    global music,sound,mode,volume,down,music_track
    setting=0
    settin_text_font=pygame.font.SysFont("monospace", 50)
    setting_text_music=settin_text_font.render("Music:-",1,(255,255,255))
    setting_text_sound=settin_text_font.render("Sound:-",1,(255,255,255))
    setting_text_mode=settin_text_font.render("Hard:-",1,(255,255,255))

    back_pic= pygame.image.load("Images\s_back.png").convert_alpha()
    back_mask=pygame.mask.from_surface(back_pic)

    while True:
        DISPLAYSURF.blit(setting_bg,(0,0))

        music_button_pic= pygame.image.load(music_button).convert_alpha()
        music_button_mask=pygame.mask.from_surface(music_button_pic)
        sound_button_pic= pygame.image.load(sound_button).convert_alpha()
        sound_button_mask=pygame.mask.from_surface(sound_button_pic)
        mode_button_pic= pygame.image.load(mode_button).convert_alpha()
        mode_button_mask=pygame.mask.from_surface(mode_button_pic)
        
        
        if setting==2:
            time.sleep(1.0)
        elif setting>=2:
            DISPLAYSURF.blit(setting_text_music,(255,150))
            DISPLAYSURF.blit(music_button_pic,(455,150))
            DISPLAYSURF.blit(setting_text_sound,(255,250))
            DISPLAYSURF.blit(sound_button_pic,(455,250))
            DISPLAYSURF.blit(setting_text_mode,(255,350))
            DISPLAYSURF.blit(mode_button_pic,(455,350))
            DISPLAYSURF.blit(back_pic,(347,450))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if pointer_mask.overlap(back_mask,(350-pointer_rect.left,450-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            break
            if pointer_mask.overlap(music_button_mask,(450-pointer_rect.left,150-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            if music_button=="Images\on_button.png":
                                music_button="Images\off_button.png"
                                music="off"
                                mixer.music.stop()
                                down=0
                            elif music_button=="Images\off_button.png":
                                music_button="Images\on_button.png"
                                music="on"
                                mixer.music.play(loops=3)
                                down=0
            if pointer_mask.overlap(sound_button_mask,(450-pointer_rect.left,250-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            if sound_button=="Images\on_button.png":
                                sound_button="Images\off_button.png"
                                sound="off"
                                if music=="on" and sound=="off":
                                    volume=0.7
                                    mixer.music.stop()
                                    s_num=random.randrange(0,9)
                                    music_track=mixer.music.load("Audio\Music\\" + song[s_num])
                                    mixer.music.set_volume(volume)
                                    mixer.music.play(loops=3)
                                down=0
                            elif sound_button=="Images\off_button.png":
                                sound_button="Images\on_button.png"
                                sound="on"
                                if music=="on" and sound=="on":
                                    volume=0.03
                                    mixer.music.stop()
                                    mixer.music.set_volume(volume)
                                    pygame.mixer.music.play(-1)
                                down=0
            if pointer_mask.overlap(mode_button_mask,(450-pointer_rect.left,350-pointer_rect.top)):
                    if (event.type==pygame.MOUSEBUTTONDOWN):
                        down=1
                    if (event.type==pygame.MOUSEBUTTONUP and down==1):
                        if(pygame.mouse.get_pressed(3)):
                            if mode_button=="Images\on_button.png":
                                mode_button="Images\off_button.png"
                                mode="Easy"
                                down=0
                            elif mode_button=="Images\off_button.png":
                                mode_button="Images\on_button.png"
                                mode="Hard"
                                down=0

            

            if pygame.mouse.get_pos():   
                pointer_rect.center=pygame.mouse.get_pos()
            DISPLAYSURF.blit(pointer,pointer_rect)
            pygame.mouse.set_visible(False)
            
            
        setting+=1
        pygame.display.update()
        clock.tick(60)
    
def pressed_setting():
    if (event.type==pygame.MOUSEBUTTONDOWN):
        if(pygame.mouse.get_pressed()):
            setting()

                         

def pressed_quit():
    global down
    if (event.type==pygame.MOUSEBUTTONDOWN):
        down=1
    if (event.type==pygame.MOUSEBUTTONUP and down==1):
            if(pygame.mouse.get_pressed()):
                down=0
                pygame.quit()
                sys.exit()    

if (__name__=="__main__"):
    
    song=['somebody.wav','Myself.wav','without_me.wav','D&Me.wav','everything_black.wav','D.wav','rover.wav','Better.wav','control.wav']
    s_num=random.randrange(0,9)

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 600))
    clock=pygame.time.Clock()

    pygame.display.set_caption("KBC-Buzz by Abhishek Dixit")
    icon=pygame.image.load("Images\KBC_icon.ico")
    pygame.display.set_icon(icon)
    
    main_bg= pygame.image.load("Images\KBC_mainbg.png")
    main_pic= pygame.image.load("Images\KBC_mainimg.png")
    setting_bg=pygame.image.load("Images\setting_bg.png")
    background= pygame.image.load("Images\KBC_background.png")
    Quiz=pygame.image.load("Images\KBC_Quiz.png")

    pointer=pygame.image.load("Images\pointer.png")
    pointer_rect=pointer.get_rect()
    pointer_mask=pygame.mask.from_surface(pointer)

    start_pic= pygame.image.load("Images\start_button.png").convert_alpha()
    start_mask=pygame.mask.from_surface(start_pic)
    setting_pic= pygame.image.load("Images\setting_button.png").convert_alpha()
    setting_mask=pygame.mask.from_surface(setting_pic)
    quit_pic= pygame.image.load("Images\quit_button.png").convert_alpha()
    quit_mask=pygame.mask.from_surface(quit_pic)

    theme=mixer.Sound("Audio\kbc_theme.wav")
    correct_ans=mixer.Sound("Audio\kbc_option_lock_tune.wav")
    wrong_ans=mixer.Sound("Audio\kbc_Wrong.wav")
    clock_tick=mixer.Sound("Audio\Kbc_Clock.wav")
    end_buzz=mixer.Sound("Audio\end_buzz.wav")
    pygame.mixer.init()
    music_track=mixer.music.load("Audio\Music\\" + song[s_num])
    mixer.music.set_volume(volume)
    while True:
            check=[5,9]
            life1="Images\half.png"
            life2="Images\Double_Dip.png"
            life3="Images\joker.png"
            life4="Images\RaveSwitch.png"
  
            DISPLAYSURF.fill((191,0,255))
            DISPLAYSURF.blit(main_bg,(0,0))
            DISPLAYSURF.blit(main_pic,(315,80))
            DISPLAYSURF.blit(start_pic,(365,280))
            DISPLAYSURF.blit(setting_pic,(365,340))
            DISPLAYSURF.blit(quit_pic,(365,400))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.mouse.get_pos():
                pointer_rect.center=pygame.mouse.get_pos()
            DISPLAYSURF.blit(pointer,pointer_rect)
            pygame.mouse.set_visible(False)

            if pointer_mask.overlap(start_mask,(365-pointer_rect.left,280-pointer_rect.top)):
                pressed_start()
            elif pointer_mask.overlap(setting_mask,(365-pointer_rect.left,340-pointer_rect.top)):
                pressed_setting()
            elif pointer_mask.overlap(start_mask,(365-pointer_rect.left,400-pointer_rect.top)):
                pressed_quit()

            pygame.display.update()
            clock.tick(80)