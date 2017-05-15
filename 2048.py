#Pengpeng Wang
# implementation of Spaceship - program template for RiceRocks
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random
import simplegui

board=[[2,0,2,4],
       [0,0,2,2],
       [2,2,0,0],
       [8,16,16,8]]
vis_board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]

def merge(key):
    global board,vis_board
    if key == simplegui.KEY_MAP['up']:
        print 1
    elif key == simplegui.KEY_MAP['down']:
        print 1
    elif key == simplegui.KEY_MAP['left']:
        for i in range(4):
            for j in range(1,4):
                m=j
                if (board[i][j]==0):
                    continue
                j=j-1
                while(board[i][j]==0 & j>=0):
                    j=j-1
                #if j=-1, [i][j]前面全是0
                if (j==-1):#前面全是0
                    board[i][0]=board[i][m]
                    board[i][m]=0
                else :#和前面数值相等
                    
                    print board[i][j],board[i][m],vis_board[i][j]
                    print 
                    if(board[i][j]==board[i][m]):
                        if (vis_board[i][j]==0):
                            board[i][j]*=2
                            board[i][m]=0
                            vis_board[i][j]=1
                        else:
                            board[i][j+1]=board[i][m]
                            if(j+1==m):
                                continue
                            else:
                                board[i][m]=0
                    else:#和前面数值不等
                        board[i][j+1]=board[i][m]
                        if(j+1==m):
                            continue
                        else:
                            board[i][m]=0
        vis_board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
        for i in range (4):
            print board[i]
    elif key == simplegui.KEY_MAP['right']:
        print 1
frame = simplegui.create_frame("Pong", 1, 1)
frame.set_keydown_handler(merge)
