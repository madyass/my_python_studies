import random

class game:
    
    table=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    @classmethod
    def draw(cls):#draws 2048 game's table
        for i in range(0,4,1):
            for j in range(0,4,1):
                print(cls.table[i][j],end="")
                if j!=3:
                    print(" ",end="")
            print(" ")
     
    @classmethod
    def add(cls,dir):
        if dir=="s":
            for k in range(0,4,1):#do it 4 times 
                for j in range(0,4,1):
                #sweep from the last row until the second row, not include first row 
                #because we do not need to look elements in the first row when direction is down,thanks to the this code
                    for i in range(3,0,-1):
                        if cls.table[i][j]!=0 and cls.table[i-1][j]==cls.table[i][j]:
                            cls.table[i][j]*=2
                            cls.table[i-1][j]=0
        elif dir=="w":
            for k in range(0,4,1): 
                for j in range(0,4,1):
                    for i in range(0,3,1):
                        if cls.table[i][j]!=0 and cls.table[i+1][j]==cls.table[i][j]:
                            cls.table[i][j]*=2
                            cls.table[i+1][j]=0
        elif dir=="a":
            for k in range(0,4,1): 
                for i in range(0,4,1):
                    for j in range(0,3,1):
                        if cls.table[i][j]!=0 and cls.table[i][j+1]==cls.table[i][j]:
                            cls.table[i][j]*=2
                            cls.table[i][j+1]=0      
        if dir=="d":
            for k in range(0,4,1): 
                for i in range(0,4,1):
                    for j in range(3,0,-1):
                        if cls.table[i][j]!=0 and cls.table[i][j-1]==cls.table[i][j]:
                            cls.table[i][j-1]*=2
                            cls.table[i][j]=0  
   
    @classmethod
    def random_number(cls):#get random cell  which is empty and add number 2 in that cell
        x=random.randint(0,3)
        y=random.randint(0,3)
        
        while cls.table[x][y]!=0:
            x=random.randint(0,3)
            y=random.randint(0,3)    
        cls.table[x][y]=2
        
    @classmethod
    def move(cls,dir):
        
        if dir=="w":
            for k in range(0,4,1):#do it 4 times
                #sweep from the second row until the end, not include first row 
                #because we do not need to move elements in the first row when direction is up
                for i in range(1,4,1):
                    for j in range(0,4,1):
                        #look cell is full and up cell is empty 
                        if cls.table[i][j]!=0 and cls.table[i-1][j]==0:
                            #move
                            cls.table[i-1][j]=cls.table[i][j]
                            cls.table[i][j]=0
        
        elif dir=="s":
            for k in range(0,4,1):
                for i in range(2,-1,-1):
                    for j in range(0,4,1):
                        if cls.table[i][j]!=0 and cls.table[i+1][j]==0:
                            cls.table[i+1][j]=cls.table[i][j]
                            cls.table[i][j]=0
        
        elif dir=="d":
            for k in range(0,4,1):
                for i in range(0,4,1):
                    for j in range(2,-1,-1):
                        if cls.table[i][j]!=0 and cls.table[i][j+1]==0:
                            cls.table[i][j+1]=cls.table[i][j]
                            cls.table[i][j]=0
        
        elif dir=="a":
            for k in range(0,4,1):
                for i in range(0,4,1):
                    for j in range(1,4,1):
                        if cls.table[i][j]!=0 and cls.table[i][j-1]==0:
                            cls.table[i][j-1]=cls.table[i][j]
                            cls.table[i][j]=0
            
    @classmethod
    def finish(cls):#if there is "2048", game over
        for i in range(3):
            for j in range(3):
                if cls.table[i][j]==2048:
                   print("GAME OVER!!!")
                   return False
        return True
    
    @classmethod
    def play(cls):
        directions=["w","a","s","d"]
        
        game.random_number()
        game.random_number()#get two random number on table for beginning
        
        while game.finish():
            
            game.draw()
        
            dir="k"
        
            while dir not in directions:#get only the one of the w,a,s,d
                dir=input("please enter direction which you want to move: ")
        
            for i in range(3):#since my functions we have to use this functions more than one
                game.move(dir)
                game.add(dir)
            game.random_number()
            game.random_number()#get two random number on table for each move 
            