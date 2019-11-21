####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = ' Team 5 Mr.Turner' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
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
    
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result 
    match = len(my_history) # Counts the number of matcheds that have occured based off how many rounds are shown in the history.
    
    if len(my_history) == 0: # If the game has just begun, then betray.
        return 'b'
    while match >= 1 and match <= 23: # From matches 1 to 23...

        if their_history[-1] == 'b': # If your partner betrayed last round then betray.
            return 'b'
        elif their_history[-1] == 'c': # If your partner colluded last round then collude.
            return 'c'

    while match >23 and match <= 27 : # From matches 24 to 27...

        if their_history[-1] == 'b': # If your partner betrayed last round then collude.
            return 'c'
        elif their_history[-1] == 'c': # If your partner colluded last round then betray.
            return 'b'

    while match >27 and match <= 53: # From matches 28 to 53...
        
        if their_history[-1] == 'b' and their_history[-2] == 'b': # If your partner betrayed last round and the round before that then betray.
            return 'b'
        elif their_history[-1] == 'c': # If your partner colluded last round the also collude.
            return 'c'
        if my_score <= -250: # If your score is -250 or less...
            
            if their_score >= -250: # If your partner's score is greater than -250 then betray.
                return 'b'
            elif my_history[-1] == 'c': # If you colluded last round then collude.
                return 'c'
            elif my_history[-1] == 'b': # If you betrayed last round then betray again.
                return 'b'
                
        elif their_score >= 100: # If their score is greater than 100, or is 100, then collude.
            return 'c'
        else: # Otherwise betray.
            return 'b'
            
    while match >53 and match <=72: # From match 54 to match 72...

        if their_history[-1] == 'b' and their_history[-2] == 'c': # If they betrayed last round and colluded before that then betray.
            return 'b'
        elif their_history[-1] == 'c' and their_history[-3] == 'b': # If they colluded last round and betrayed two rounds before that then betray.
            return 'b'
        else: # Otherwise betray.
            return 'b'
            
    while match >72 and match <=91: # From match 73 to match 91...
           
        if their_history[-3] =='c' and my_history[-3] == 'b': # If they colluded three rounds ago and you betrayed three rounds ago then betray.
            return 'b'
        elif their_history[-3] == 'b' and my_history[-3] == 'c' : # If they betrayed three rounds ago and you colluded three rounds ago then collude.
            return 'c'
        else: # Otherwise betray.
            return 'b'
    
    while match >92 and match <=95: # From match 93 to match 95...
        
        if my_score <= -400: # If their score is less than or equal to -400 betray.
            return 'b' 
        elif my_score >= 300: # If my score is greater than or equal to 300 collude.
            return 'c'
        else: # Otherwise betray.
            return 'b'
            
    if my_score <= -600 and their_score >= -100: # If your score is less than or equal to -600 and their score is greater than or equal to -100 then betray.
        return 'b'
    elif their_score <= -600 and my_score >= 0 : # If their score is less than or equal to -600 and my score is greater than or equal to 0 then betray.
        return 'c' 
    else: # Otherwise betray.
        return 'b'
        
:
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
