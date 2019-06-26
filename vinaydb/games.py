class Selectgame:
    def selectGame(self):    
        option = input('enter ok to add sports else no: ')
        print('cricket','badmintion','basketBall','volleyBall','baseBall','footBall')
        select = str(input('enter the selected game: '))    
        if (option=='ok'):
            if (select==('cricket' or 'badmintion' or 'basketBall' or 'volleyBall' or 'baseBall' or 'footBall')):
                print('thank you for your response') 
                return select   
            else:
                print('please enter correctly')
                print('cricket','badmintion','basketBall','volleyBall','baseBall','footBall')
                select = str(input('enter the selected game: '))
                return select
        elif(option == 'no'):
            select='thank you for your response'
            return select


