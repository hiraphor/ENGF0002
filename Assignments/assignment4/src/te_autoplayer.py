''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction
import time

bestmove = [-100000, 0, 0, 0, 0]
counter1=0
counter2=0
counter3=0
somex=0


class AutoPlayer():

    


    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()


    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        if gamestate.get_falling_block_position()[1] == 1:
            self.search_all('right', gamestate)
            self.search_all('left', gamestate)
        else:
            self.makemove(gamestate)





    def makemove(self, gamestate):

        left = Direction.LEFT
        right = Direction.RIGHT
        global bestmove
        global counter1
        global counter2
        global counter3

        if bestmove[1] == -1:
            if counter1<bestmove[2]:
                gamestate.move(left)
                gamestate.rotate(left)
                counter1+=1

            elif counter1==bestmove[2]:
                if counter2<bestmove[3]:
                    gamestate.move(left)
                    counter2+=1

                elif counter2==bestmove[3]:
                    if counter3<bestmove[4]:
                        gamestate.rotate(left)
                        counter3+=1

                    elif counter3==bestmove[4]:
                            counter1=0
                            counter2=0
                            counter3=0
                            bestmove = [-100000, 0, 0, 0, 0]
            

        elif bestmove[1] == 1:
            if counter1<bestmove[2]:
                gamestate.move(right)
                gamestate.rotate(left)
                counter1+=1

            elif counter1==bestmove[2]:
                if counter2<bestmove[3]:
                    gamestate.move(right)
                    counter2+=1

                elif counter2==bestmove[3]:
                    if counter3<bestmove[4]:
                        gamestate.rotate(left)
                        counter3+=1

                    elif counter3==bestmove[4]:
                            counter1=0
                            counter2=0
                            counter3=0
                            bestmove = [-100000, 0, 0, 0, 0]


    def search_all(self, direction, gamestate):

        global bestmove
        left = Direction.LEFT
        right = Direction.RIGHT
    
        if direction == 'left':
            combinations = 20
            leftorright = left

        elif direction == 'right':
            combinations = 24
            leftorright = right

        numberofmoves = 0
        numberofrotations = 0

        gamescore = gamestate.get_score()

        for i in range(combinations):
            clone = gamestate.clone(True)
            movesandrotations = min(numberofmoves, numberofrotations)

            rotations = numberofrotations-movesandrotations
            moves = numberofmoves - movesandrotations

            movesorrotations = abs(moves-rotations)

            for j in range (movesandrotations):
                clone.move(leftorright)
                clone.rotate(left)
                clone.update()

            for k in range(movesorrotations):
                if moves>rotations:
                    clone.move(leftorright)
                    clone.update()
                elif rotations>moves:
                    clone.rotate(left)
                    clone.update()

            while not clone.update():
                pass

            clonescore = clone.get_score()

            if 100<(clonescore-gamescore)<200:
                rowscleared = 1
            elif 200<(clonescore-gamescore)<300:
                rowscleared=2
            elif 300<(clonescore-gamescore)<400:
                rowscleared=3
            elif 400<(clonescore-gamescore)<500:
                rowscleared=4
            elif 500<(clonescore-gamescore)<600:
                rowscleared=5
            else:
                rowscleared=0
            



            clone.print_tiles()
            gamelist = clone.get_tiles()
            current_score = score_calculator(gamelist, rowscleared)
            print (current_score)
            #time.sleep(3)
            print('M and R: ', movesandrotations)
            print('M: ', moves)
            print('R: ', rotations)




            for i in range(len(bestmove)):
                print('Best Move: ', bestmove[i])


            if current_score>bestmove[0]:
                bestmove[0] = current_score
                if leftorright == left:
                    bestmove[1] = -1
                elif leftorright == right:
                    bestmove[1] = 1
                bestmove[2] = movesandrotations
                bestmove[3] = moves
                bestmove[4] = rotations

            #time.sleep(0.5)

            if numberofrotations<3:
                numberofrotations+=1
            elif numberofrotations==3:
                numberofrotations=0
                numberofmoves+=1



        
def score_calculator(blocklist, rows_cleared):
    '''for i in range(len(blocklist)):
        print(blocklist[i])'''





    agg_height = 0
    bumpiness = 0
    column_height = 0
    number_of_holes = 0
    number_of_blocks = 0
    col_heights = []

    for columns in range (10):
        for rows in range (20):

            if blocklist[rows][columns]!=0:
                if column_height==0:
                    column_height+=(20-rows)
                number_of_blocks+=1

        col_heights.append(column_height)
        agg_height+=column_height
        number_of_holes += (column_height - number_of_blocks)
        column_height = 0
        number_of_blocks=0
    
    for cols in range (9):
        bumpiness+= abs(col_heights[cols+1]-col_heights[cols])



    '''for rows in range (20):
        a=0
        for columns in range(10):
            if blocklist[rows][columns]!=0:
                a+=1
        if a==10:
            number_of_rows+=1'''
        
    print('agg_height: ',agg_height, '\n', 'bumpiness: ',bumpiness, '\n', 'num_holes: ', number_of_holes, '\n', 'num_rows: ', rows_cleared)

    return ((-0.51*agg_height) + (-0.3566*number_of_holes) + (-0.18 * bumpiness) + (0.5*rows_cleared))

