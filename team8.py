####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'We luv Mostafa' # Only 10 chars displayed.
#Vinh, Mostafa, Mitchell, Richard
strategy_name = 'What are we doing'
strategy_description = 'We are alternating and whatnot'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    #Scenario 1: when I am betrayed 3 times in a row return a collude, else continue betraying
    
    if len(their_history) >= 3 and their_history[-3] == 'b': #when they have more than 3 choices and B is chosen 3 times in a row
        len(their_history) <= int(3)
        return 'c' #return a collude
    else:
        return 'b' #if not, return a betray
        
    #Scenario 2: 
    if my_score < 0: #if my score goes under 0
        return 'b'  #then betray
    else:   #if it isn't under 0
        return 'c' # then collude
        
    #Scenario 3:
    if len(my_history)==0:# when we start the game, collude first
       return 'c'
    else: # after the start, betray all the time
       return 'b'
       
    #Scenario 4:
    if len(my_history) == 0:
        return 'c'
        #this makes us return will collude on our very first turn
    else:
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            if (prior_round_me == recent_round_me) and (prior_round_them == recent_round_them):
                return their_history[round]
        #this references both team's previous turns
        if their_history[-1] == 'b':
            return 'b'
            #returns betray if the other team's last turn was betray
        else:
            return 'c'
            #returns collude if the team's last turn wasn't betray
            
    #Scenario 5:
    
    if len(my_history) == 0: # when the game starts, betray
        return 'b'
    elif 'bbbbb' in my_history:    # if whenever we betrayed 5 times in a row, collude
        return 'c'
    else:                                     # otherwise, betray
        return 'b'


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
