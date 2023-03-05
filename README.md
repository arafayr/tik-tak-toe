# Tic-Tac-Toe Game
This repository contains a Python implementation of the classic Tic-Tac-Toe game. The game is played between two players, with the goal of placing three markers (either 'X' or 'O') in a row, column or diagonal on a 3x3 grid. This implementation includes an AI computer player to play against. This project was made to get a better grasp on data structures in python!

# Implementation Details
The implementation consists of the following classes:

## node
This class represents a node in a linked list. It has two attributes:
* `data` to store the value of the node.
* `next` to store the reference to the next node in the list.

## stack
This class represents a stack data structure using a linked list. It has the following methods:

* `push(data)`: Adds an element to the top of the stack.
* `pop()`: Removes the top element from the stack.
* `isEmpty()`: Checks if the stack is empty.
* `peek()`: Returns the top element of the stack.
* `traverse()`: Prints all the elements of the stack.

## Array
This class represents a 1-dimensional array using ctypes. It has the following methods:

* `clear(value)`: Sets all elements in the array to the specified value.
* `__getitem__(index)`: Returns the element at the specified index.
* `__setitem__(index`, value): Sets the element at the specified index to the specified value.

## Array2d
This class represents a 2-dimensional array using an array of arrays. It has the following methods:

* `clear(value)`: Sets all elements in the array to the specified value.
* `copy()`: Creates a copy of the array.
* `noofrows()`: Returns the number of rows in the array.
* `noofcols()`: Returns the number of columns in the array.
* `__getitem__(ndxtpl)`: Returns the element at the specified index tuple.
*`__setitem__(ndxtpl, value)`: Sets the element at the specified index tuple to the specified value.

## tiktaktoe
This class represents the Tic-Tac-Toe game. It has the following methods:

* `show()`: Prints the current state of the game board.
* `playable()`: Returns True if there are any empty spaces left on the game board.
* `play()`: Starts the game and allows the player to make a move, followed by the computer's move.
* `computerMove()`: Calculates and returns the computer's move.

If you have any questions, feel free to ask, I will be happy to help.
