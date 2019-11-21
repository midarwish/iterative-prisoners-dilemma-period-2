
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'C.L.A.S.S.' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'


#SAMARTH'S CODE:
def move(my_history, their_history, my_score, their_score):
    if len(their_history) >= 1 and their_history[-3] == 'c':
        return 'b'  #If they have colluded for the last three turns then take advantage and betray them
    if len(their_history) >= 1 and their_history[-1] == 'c':
        return 'c'  #If they collude last then collude
    elif len(their_history) >= 1 and their_history[-1] == 'b':
        return 'b'  #If their last turn is betrayal then betray
    else:
        return 'c'
#AUDREY'S CODE: 
    if len(my_history)==0: #this will make it start off with colluding
        return 'c'
    elif len(my_history) >= 1 and my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    elif len(my_history) >= 5 and (my_history[-5]) == 'b' and (my_history[-4]) and (my_history[-3]) and (my_history[-2]) and (my_history[-1]): #if my last 5 moves were d, collude
        return 'c'
    elif my_history == 25 and my_score < 100:
        return 'b'
    else:
        return 'c'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
#LIPITHA'S CODE:
    if len(my_history)==0: # It's the first round; betray.
        return 'c'
    else:
        return 'b' #Else Betray
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
#SAMENTHA'S CODE:
    if len(my_history)%2 == 0:
        return 'b'
    else:
        return 'c'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
#CAITLYN'S CODE:
    def total_b(their_history):
        total_b = 0
        for turn in their_history:
            if turn == 'b':
                print 'was b'
                total_b += 1
        percentage = total_b/len(their_history)
        return percentage
        if total_b(their_history) > 0.5:
            return 'b'
    def betray_afterbetrayal(my_history, their_history, my_score, their_score):
        if len(my_history) == 0:
            return 'c'
        elif my_history[-1] == 'c' and their_history[-1] == 'b':
            return 'b'
        else:
            return 'c'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
      
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
              

