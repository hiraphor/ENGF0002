''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction

class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        #self.random_next_move(gamestate)

                
    def appraise_position(self, gamestate):
        return 0
    
    
    def search_all_left(self, gamestate):
        left = Direction.LEFT
        numberofmoves = 1
        numberofrotations = 1
        movesorrotations = abs(numberofmoves-numberofrotations)
        movesandrotations=min(numberofmoves, numberofrotations)
        
        for i in range(16):
            clone = gamestate.clone(True)
            if numberofmoves<numberofrotations:
                    for j in range(movesandrotations):
                        clone.move(left)
                        clone.rotate()
                        clone.update()
                    for k in range(movesorrotations):
                        clone.rotate()
                        clone.update()
            elif numberofrotations<numberofmoves:
                    for j in range (movesandrotations):
                        clone.move(left)
                        clone.rotate()
                        clone.update()
                    for k in range (movesorrotations):
                        clone.move(left)
                        clone.update()
            elif numberofmoves==numberofrotations:
                for j in range(movesandrotations):
                    clone.move(left)
                    clone.rotate()
                    clone.update()

            while (clone.update() != True):
                clone.update()

            if numberofrotations<4:
                numberofrotations+=1
            elif numberofrotations==4:
                numberofrotations=1
                numberofmoves+=1

            if numberofmoves==4:
                numberofmoves=1
 
        
        
    def search_all_right(self, gamestate):
        right = Direction.RIGHT
        numberofmoves = 1
        numberofrotations = 1
        movesorrotations = abs(numberofmoves-numberofrotations)
        movesandrotations=min(numberofmoves, numberofrotations)
        
        for i in range(20):
            clone = gamestate.clone(True)
            if numberofmoves<numberofrotations:
                    for j in range(movesandrotations):
                        clone.move(right)
                        clone.rotate()
                        clone.update()
                    for k in range(movesorrotations):
                        clone.rotate()
                        clone.update()
            elif numberofrotations<numberofmoves:
                    for j in range (movesandrotations):
                        clone.move(right)
                        clone.rotate()
                        clone.update()
                    for k in range (movesorrotations):
                        clone.move(right)
                        clone.update()

            if numberofmoves==numberofrotations:
                for j in range(movesandrotations):
                    clone.move(right)
                    clone.rotate()
                    clone.update()

            while (clone.update() != True):
                clone.update()

            if numberofrotations<4:
                numberofrotations+=1
            elif numberofrotations==4:
                numberofrotations=1
                numberofmoves+=1

            if numberofmoves==4:
                numberofmoves=1
        
        
        
        
        ''' make a random move and a random rotation.  Not the best strategy! '''
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.move(direction)
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            gamestate.rotate(direction)
        gamestate.print_block_tiles()
        
