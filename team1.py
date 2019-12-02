####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Pollo tenders' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'

    
def move(my_history, their_history, my_score, their_score):
    # this is the first thing it will test, 
    # it will check if we wanted to do a certain series of moves and then it will execute them in order
    

    # This first condition will go once there are more than 6 moves in the history so that it has enough moves to analize
    if len(my_history) >=6 and their_history >= 6:
            # This checks if their last 4 moves are cbcb we return the same
        if their_history[-4] == 'c' and their_history[-3] == 'b' and their_history[-2] == 'c' and their_history[-1] == 'b':
            return 'c'
        # If they are doing bb in between each c we make sure to c on their c
        elif their_history[-4] == 'c' and their_history[-3] == 'b' and their_history[-2] == 'b' and their_history[-1] == 'c':
            return 'b'
        # Same as first just opposite
        elif their_history[-4] == 'b' and their_history[-3] == 'c' and their_history[-2] == 'b' and their_history[-1] == 'c':
            return 'b'
        # If they alternate every two rounds we do the same.
        elif their_history[-6] == 'b' and their_history[-5] == 'b' and their_history[-4] == 'c' and their_history[-3] == 'c' and their_history[-2] == 'b' and their_history[-1] == 'b':
            return 'c'
        # If they follow this pattern we know to betray when they collude to get points.
        elif their_history[-6] == 'b' and their_history[-5] == 'b' and their_history[-4] == 'c' and their_history[-3] == 'b' and their_history[-2] == 'b' and their_history[-1] == 'c':
            return 'b'

    # condition executes within the first three moves of the game
    elif len(their_history) <= 3:
        #it counts how many times they did each letter 
        for letter in their_history:
            b = 0
            c = 0
            if letter == 'c':
                c += 1
            elif letter == 'b':
                b += 1
            else:
                print ('invalid input')
            #then it checks if the majority is c and b if it is true
            if c >= 2:
                return 'b'
        #otherwise, it will alternate
        else:
            if len(my_history) % 2 == 0:
                return 'c'

        
    
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')
              
                           
