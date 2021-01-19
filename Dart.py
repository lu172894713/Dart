def count ( number, name ):
    sure = 'n'
    print ( "player:", name )
    while ( sure == 'n' ):
        f = abs ( int ( input ( "1st: " )))
        ft = abs ( int ( input ( "1times: " )))
        ftotal = number - f * ft
        print ( ftotal )
        if ( ftotal < 0 ):
            print ( "Your score is over it! " )
            return number
        elif ( ftotal == 0 ):
            return ftotal
        s = abs ( int ( input ( "2nd: " )))
        st = abs ( int ( input ( "2times: " )))
        stotal = ftotal - s * st
        print ( stotal )
        if ( stotal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( stotal == 0 ):
            return stotal
        t = abs ( int ( input ( "3rd: " )))
        tt = abs ( int ( input ( "3times: " )))
        ttotal = stotal - t * tt
        print ( ttotal )
        if ( ttotal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( ttotal == 0 ):
            return ttotal
        fo = abs ( int ( input ( "4th: " )))
        fot = abs ( int ( input ( "4times: " )))
        fototal = ttotal - fo * fot
        print ( fototal )
        if ( fototal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( fototal == 0 ):
            return fototal
        fi = abs ( int ( input ( "5th: " )))
        fit = abs ( int ( input ( "5times: " )))
        fitotal = fototal - fi * fit
        print ( fitotal )
        if ( fitotal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( fitotal == 0 ):
            return fitotal
        sure = input ( "Are you sure? ( y/n ) " )
        sure = sure . lower()
    total = f * ft + s * st + t * tt + fo * fot + fi * fit
    number1 = number - total
    if ( number1 < 0 ):
        print ( "Your score is over it! ")
        return number
    elif ( number1 >= 0 ):
        return number1

def threecount ( number, name ):
    sure = 'n'
    print ( "player:", name )
    while ( sure == 'n' ):
        f = abs ( int ( input ( "1st: " )))
        ft = abs ( int ( input ( "1times: " )))
        ftotal = number - f * ft
        print ( ftotal )
        if ( ftotal < 0 ):
            print ( "Your score is over it! " )
            return number
        elif ( ftotal == 0 ):
            return ftotal
        s = abs ( int ( input ( "2nd: " )))
        st = abs ( int ( input ( "2times: " )))
        stotal = ftotal - s * st
        print ( stotal )
        if ( stotal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( stotal == 0 ):
            return stotal
        t = abs ( int ( input ( "3rd: " )))
        tt = abs ( int ( input ( "3times: " )))
        ttotal = stotal - t * tt
        print ( ttotal )
        if ( ttotal < 0 ):
            print  ( "Your score is over it! " )
            return number
        elif ( ttotal == 0 ):
            return ttotal
        sure = input ( "Are you sure? ( y/n ) " )
        sure = sure . lower()
    total = f * ft + s * st + t * tt 
    number1 = number - total
    if ( number1 < 0 ):
        print ( "Your score is over it! ")
        return number
    elif ( number1 >= 0 ):
        return number1

    


again = 'y'
while ( again == 'y' ):
    people = abs ( int ( input ( "\nEnter 2 ~ 3 person: " )))
    if ( people > 2 ):
        name1 = input ( "Enter 1P's Name: " )
        name2 = input ( "Enter 2P's Name: " )
        name3 = input ( "Enter 3P's Name: " )
        player1 = abs ( int ( input ( "Enter total scores: " )))
        player2 = player1
        player3 = player1
        choice = abs ( int ( input ( "Enter 3 shoots or 5 shoots? " )))
        if ( choice == 3 ):
            print ( "\n1P:", name1, "\t 2P:", name2, "\t\t 3P:", name3 )
            print ( format ( player1, '3,.2f' ), "\t", format ( player2, '3,.2f' ), "\t", format ( player3, '3,.2f' ))
            while ( player1 > 0 and player2 > 0 and player3 > 0 ):
                player1 = threecount ( player1, name1 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player1 == 0 ):
                    break
                player2 = threecount ( player2, name2 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player2 == 0 ):
                    break
                player3 = threecount ( player3, name3 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player3 == 0 ):
                    break
            if ( player1 == 0 ):
                print ( "\nThe Winner is ", name1, "!!!!!!" )
            if ( player2 == 0 ):
                print ( "\nThe Winner is ", name2, "!!!!!!" )
            if ( player3 == 0 ):
                print ( "\nThe Winner is ", name3, "!!!!!!" )
        
        if ( choice == 5 ):
            print ( "\n1P:", name1, "\t 2P:", name2, "\t\t 3P:", name3 )
            print ( format ( player1, '3,.2f' ), "\t", format ( player2, '3,.2f' ), "\t", format ( player3, '3,.2f' ))
            while ( player1 > 0 and player2 > 0 and player3 > 0 ):
                player1 = count ( player1, name1 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player1 == 0 ):
                    break
                player2 = count ( player2, name2 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player2 == 0 ):
                    break
                player3 = count ( player3, name3 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ), "\t", format ( player3, '5,.2f' ))
                if ( player3 == 0 ):
                    break
            if ( player1 == 0 ):
                print ( "\nThe Winner is ", name1, "!!!!!!" )
            if ( player2 == 0 ):
                print ( "\nThe Winner is ", name2, "!!!!!!" )
            if ( player3 == 0 ):
                print ( "\nThe Winner is ", name3, "!!!!!!" )
        
        
    if ( people == 2 ):
        name1 = input ( "Enter 1P's Name: " )
        name2 = input ( "Enter 2P's Name: " )
        player1 = abs ( int ( input ( "Enter total score: " )))
        player2 = player1
        choice = abs ( int ( input ( "Enter 3 shoots or 5 shoots? " )))
        if ( choice == 3 ):
            print ( "\n1P:", name1, "\t 2P:", name2,)
            print ( format ( player1, '3,.2f' ), "\t", format ( player2, '3,.2f' ))
            while ( player1 > 0 and player2 > 0 ):
                player1 = threecount ( player1, name1 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ))
                if ( player1 == 0 ):
                    break
                player2 = threecount ( player2, name2 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ))
                if ( player2 == 0 ):
                    break
            if ( player1 == 0 ):
                print ( "\nThe Winner is ", name1, "!!!!!!" )
            if ( player2 == 0 ):
                print ( "\nThe Winner is ", name2, "!!!!!!" )
            
        
        if ( choice == 5 ):
            print ( "\n1P:", name1, "\t 2P:", name2,)
            print ( format ( player1, '3,.2f' ), "\t", format ( player2, '3,.2f' ))
            while ( player1 > 0 and player2 > 0 ):
                player1 = count ( player1, name1 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ))
                if ( player1 == 0 ):
                    break
                player2 = count ( player2, name2 )
                print ( format ( player1, '5,.2f' ), "\t", format ( player2, '5,.2f' ))
                if ( player2 == 0 ):
                    break
            if ( player1 == 0 ):
                print ( "\nThe Winner is ", name1, "!!!!!!" )
            if ( player2 == 0 ):
                print ( "\nThe Winner is ", name2, "!!!!!!" )
            
        
        
        
    

    again = input ( "\nPlay Again? " )
    again = again . lower()
