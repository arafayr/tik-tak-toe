#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ctypes
import random

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def push(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            self.count+=1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.count+=1
            
    def pop(self):
        assert self.head != None, "Stack is empty"
        if self.head != None:
            
            curr = self.head
            prev = None
            
            while curr.next:
                prev = curr
                curr = curr.next
                
            self.tail = prev
            
            if curr == self.head:
                self.head = None
                self.tail = None
                self.count-=1
            else:
                prev.next = None
                self.count-=1
                
    def __len__(self):
        return self.count
    def isEmpty(self):
        return self.head == None
    def peek(self):
        return self.tail.data
    def traverse(self):
        curr = self.head
            
            
        while curr:
            print(curr.data)
            curr = curr.next
                
            
            
class Array:
    def __init__(self,size):
        
        self.size = size
        
        pyelement = ctypes.py_object * size
        self.array = pyelement()
        
        self.clear(None)
        
    def noofrows(self):
        return self.size
    
    def __len__(self):
        return self.size
        
    def clear(self,value):
        
        for i in range(self.noofrows()):
            self.array[i] = value
            
    def __getitem__(self,index):
        return self.array[index]
    def __setitem__(self,index,value):
        self.array[index] = value
        
class Array2d:
    
    def __init__(self,rows,cols):
        
        
        self.rows = Array(rows)
        
        for i in range(len(self.rows)):
            self.rows[i] = Array(cols)
    def clear(self,value):
        for i in range(len(self.rows)):
            self.rows[i].clear(value)
        
    def noofrows(self):
        return len(self.rows)
    
    def noofcols(self):
        return len(self.rows[0])
        
    def copy(self):
        CopyArray = Array2d(self.noofrows(),self.noofcols())
        
        for i in range(self.noofrows()):
            for j in range(self.noofcols()):
                CopyArray[i,j] = self.rows[i][j]
        return CopyArray
    def __getitem__(self,ndxtpl):
        r = ndxtpl[0]
        c = ndxtpl[1]
        
        row = self.rows[r]
        
        return row[c]
    def __setitem__(self,ndxtpl,value):
        r = ndxtpl[0]
        c = ndxtpl[1]
        row = self.rows[r]
        
        row[c] = value
        
class tiktaktoe:
    def __init__(self,gridrow,gridcol,player1_marker,player2_marker):
        self.player1_marker = player1_marker
        self.player2_marker = player2_marker
        self.game = Array2d(gridrow,gridcol)
        self.game.clear(".")
    
    def show(self):
        for i in range(self.game.noofrows()):
            print()
            for j in range(self.game.noofcols()):
                print(self.game[i,j],end = " | ")
                
                
            print()
            for k in range(self.game.noofrows()):
                if i == self.game.noofrows()-1:
                    break
                else:
                    print("_"*(j+1),end="")
                    
            print()
            
    def playable(self):
        for i in range(self.game.noofrows()):
            for j in range(self.game.noofcols()):
                if self.game[i,j]  == ".":
                    return True

    def play(self):
        while self.playable() :
            
            move = input("Player1 move: ")
            print("-----------Player1 move-----------")
            move = move.split()
            r = int(move[0])
            c = int(move[1])
            
            if self.game[r,c] ==".":
                self.game[r,c] = self.player1_marker
            else:
                print("This location has already been occupied")
            
            self.show()
            a = test()
            
            if a == True:
                print("-----------PLAYER-1 IS WINNER!!!-----------")
                return
            
            #computer wali MOVE
            if self.playable():
                print("-----------Computer Move-----------")
                b = self.computerMove()
                
                self.show()
                if b == "o":
                    #self.show()
                    print("-----------OPPS! Computer won, better luck next time-----------")
                    return
                
                a = test()
                if a == True:
                    print("-----------OPPS! Computer won, better luck next time-----------")
                    return
            
            if not self.playable():
                print("-----------DRAW-----------")
            
            
    def computerMove(self):
        
        #calculating mid
        mid = self.game.noofcols()//2
        
        #To save the initial position of the board
        gameboardCopy = self.game.copy()
        
        #Idher "o" player ka hai or "x" computer ka 
        move = 0 
        
        possibleMoves = []
        
        #We are checking every availaible moves
        for x in range(self.game.noofrows()):
            for y in range(self.game.noofcols()):
                
                if self.game[x,y] == ".":
                    possibleMoves.append([x,y])
                    
        #Asal algorithem
        for let in ["o","x"]:
            for i in possibleMoves:
                #print(self.game[i],end = " ")
                #making copy of actual game board every time cuz
                #hamein sirf ik move predict karni hai jis se comp ya samne wala 
                #jeet sakta ha
                
                #har possible move ke liye naya board
                self.game = gameboardCopy.copy()
                
                self.game[i] = let
                if test():
             #       print("koi jeet rah")
                    move = i
                    
                    #ku ke block karne ke liye or esi move chalne ke liye jis se
                    #comp jeet jaye dono sorto me "o" hi place hona hai
                    self.game[i] = "o"
                    return let
        #To restore the board in to its original position
        self.game = gameboardCopy.copy()
        
        #3rd case checking for corners
        cornerpossiblities = [[self.game.noofrows()-1,self.game.noofcols()-1],[0,0],[self.game.noofrows()-1,0],[0,self.game.noofcols()-1]]

        corners = []
        for i in cornerpossiblities:
            if self.game[i] == ".":
                
                corners.append(i)
                
                #print(corners)
                
        if len(corners)>0:
            
            move = random.choice(corners)
            #print("corners")
            self.game[move] = "o"
            return "no"
        #4rth case checking for mid
        if [mid,mid] in possibleMoves:
            self.game[mid,mid] = "o"
            return "no"
         
        #5th case checking for any possiblity
        if len(possibleMoves)>0:
            self.game[random.choice(possibleMoves)] = "o"
            #print("possible moves wali list ",possibleMoves)
            return "no"
        else:
            #print('draw')
            return "draw"
            
            
            

#obj.noofrows()
#obj.noofcols()
obj2 = tiktaktoe(3,3,"x","o")
obj = stack()
obj3 = stack()
obj4 = stack()
obj5 = stack()
#obj2.play()
#obj2.checkAll()
#obj.play()



def test():
    while not obj.isEmpty():
        obj.pop()
    while not obj3.isEmpty():
        obj3.pop()
        
    while not obj4.isEmpty():
        obj4.pop()
    while not obj5.isEmpty():
        obj5.pop()
        
    for i in range(obj2.game.noofrows()):
        for j in range(obj2.game.noofcols()):

            
            if  j >0 and obj2.game[j,i]!= ".":
                
                
                if obj2.game[j,i]== obj2.game[j-1,i]:
                    if obj.isEmpty():
                        obj.push([j,i])
                    elif obj.peek()[1] != i :
                        
                        while not obj.isEmpty():
                            obj.pop()
                        obj.push([j,i])
                    
                    elif obj.peek()[1] == i and obj.peek()[0] != j :
                        
                        obj.push([j,i])
                if len(obj) == obj2.game.noofrows()-1 or len(obj) == obj2.game.noofrows():
                    
                    return True
                    
            if j >0 and obj2.game[i,j]!= ".":
                
                if obj2.game[i,j]== obj2.game[i,j-1]:
                    if obj3.isEmpty():
                        obj3.push([i,j])
                        
                    
                    elif obj3.peek()[0] != i:
                        while not obj3.isEmpty():
                            obj3.pop()
                        obj3.push([i,j])

                    elif obj3.peek()[0] == i and obj3.peek()[1] != j :
                        
                        obj3.push([i,j])

                    
            if len(obj3) == obj2.game.noofrows()-1 or len(obj3) == obj2.game.noofrows() :
                
                
                return True
            
        if obj2.game[i,i]!=".":
                    
            if obj4.isEmpty():
                obj4.push([i,i])
                    
                    
            elif obj2.game[obj4.peek()[0],obj4.peek()[1]] == obj2.game[i,i]:
                obj4.push([i,i])
                

                    
        if len(obj4) == obj2.game.noofrows() :
            
            return True
                    
        if obj2.game[i,obj2.game.noofrows()-1-i]!=".":
            
                
                    
            if obj5.isEmpty():
                obj5.push([i,obj2.game.noofrows()-1-i])
                    
                    
            elif obj2.game[obj5.peek()[0],obj5.peek()[1]] == obj2.game[i,obj2.game.noofrows()-1-i]:
                obj5.push([i,obj2.game.noofrows()-1-i])
                

                    
        if len(obj5) == obj2.game.noofrows() :
            
            return True
                
    

def playoutside():
    
    for i in range(obj2.game.noofrows()):
        for j in range(obj2.game.noofcols()):


            obj2.game[i,j] = random.choice("xxxooo")
            obj2.show()
            print("\n")
            okay = test()
            if okay == True:
                #obj2.show()
                return True
            elif not obj2.playable():
                print("-----------DRAW-----------")
    


            #print("--------Vertical-Stack--------")
            #obj.traverse()
            #print("--------Hoizontal-Stack--------")
            #obj3.traverse()
            #print("--------Diagonal-Stack--------")        
            #obj4.traverse()
            #print("--------Other Diagonal-Stack--------")        
            #obj5.traverse()
            
            
            
    
    

#playoutside() 
obj2.play()
#obj2.computerMove()

