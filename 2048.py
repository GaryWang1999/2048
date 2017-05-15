#Pengpeng Wang and Micheal Hu on 5.15 2017
#2048
# import modules
import os
import pygame

# pygame specific locals/constants
from pygame.locals import *

# some resource related warnings
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')
import random
import math
pygame.init()

board=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
       #initialize a board to record the number

vis_board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
           #create a two-dimensional list to record if the board is changed
merge_num=0
# int a number to record how many times you made mergence
# which should be the main goal of the game I think-make more mergences

# Tile Images
IMAGENAME = "assets_2048.png"
TILE_SIZE = 100
HALF_TILE_SIZE = TILE_SIZE / 2
BORDER_SIZE = 45
change=0          
            
    
def merge(key):
    '''
    I first write the function of merge with the direction of left
    then tranform it into a function called limitless_merge
    The function is similar, therefore I rotate the 2D list and merge it to left and rotate it back
    '''
    global board,vis_board,change    
    if key == simplegui.KEY_MAP['up']:
        rotate_up()
        limitless_merge()
        rotate_up()
        rotate_up()
        rotate_up()

    elif key == simplegui.KEY_MAP['down']:
        rotate_up()
        rotate_up()
        rotate_up()
        limitless_merge()
        rotate_up()

    elif key == simplegui.KEY_MAP['left']:
        limitless_merge()

    elif key == simplegui.KEY_MAP['right']:
        rotate_right()
        limitless_merge()
        rotate_right()
     

    if( change ):
        change=0
        add()
        print_result()
    
def rotate_right():
    '''
    rotate function for merging to right
    '''
    for i in range (4):
        temp=board[i][0]
        board[i][0]=board[i][3]
        board[i][3]=temp
        temp=board[i][1]
        board[i][1]=board[i][2]
        board[i][2]=temp 
def rotate_up():
    '''
    rotate function for merging to up or down
    '''
    global board
    temp=[[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
    for i in range (4):
        m=3
        for j in range(4):
            temp[m][i]=board[i][j]
            m=m-1
    board=temp
    
def limitless_merge():
    global board,vis_board,change,merge_num
    for i in range(4):
            for j in range(1,4):
                m=j
                if (board[i][j]==0):
                    continue
                j=j-1
                while(board[i][j]==0):
                    if(j<0):
                        break
                    j=j-1        
                #if j=-1, then all the number before [i][j]is 0
                if (j==-1):
                    board[i][0]=board[i][m]
                    board[i][m]=0
                    #so we can just move it there
                    change=1
                else :
                    if(board[i][j]==board[i][m]):
                        if (vis_board[i][j]==0):
                            board[i][j]*=2
                            board[i][m]=0
                            vis_board[i][j]=1
                            change=1
                            merge_num = merge_num + 1
                        else:
                            board[i][j+1]=board[i][m]
                            if(j+1==m):
                                continue
                            else:
                                board[i][m]=0
                    else:#not equal to the number before it
                        board[i][j+1]=board[i][m]
                        if(j+1==m):
                            continue
                        else:
                            board[i][m]=0
                            change=1
    vis_board=[[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]
    
def print_result():
    for i in range (4):
        print board[i]
    print
    
def add():
    '''
    randomly add a 2 or 4 tile by giving 0 a number
    '''
    for i in range(10000):
            location_i=random.randrange(0,3)
            location_j=random.randrange(0,3)
            if(board[location_i][location_j]==0):
                board[location_i][location_j]=random.choice( [2,4,2,2,2] )
                break
def new_game():
    global board,merge_num
    board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    add()
    add()
    merge_num=0
    l2.set_text('Merge number '+str(merge_num))
    
def draw(canvas):
    '''
    the code copy from the poc_2048_gui provided by rice university on cousera
    with a little bit change
    '''
    global merge_num
    for row in range(4):
        for col in range(4):
                tile = board[row][col]
                if tile == 0:
                    val = 0
                else:
                    val = int(math.log(tile, 2))
                canvas.draw_image(simplegui.load_image('assets_2048.png'),
                    [HALF_TILE_SIZE + val * TILE_SIZE, HALF_TILE_SIZE],
                    [TILE_SIZE, TILE_SIZE],
                    [col * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE,
                     row * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE],
                    [TILE_SIZE, TILE_SIZE])   
    l2.set_text('Merge number '+str(merge_num))
                
print_result()
frame = simplegui.create_frame("2048", 500, 500)
frame.set_keydown_handler(merge)
frame.set_draw_handler(draw)
frame.set_canvas_background("#BCADA1")
frame.add_button('New Game', new_game)
l2=frame.add_label('')
frame.add_label('')
frame.add_label('The limit is 8196')


frame.start()
new_game()
