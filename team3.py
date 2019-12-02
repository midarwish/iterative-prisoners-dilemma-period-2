####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Okonkwo' # Only 10 chars displayed.
strategy_name = 'look at history and decide based on it'
strategy_description = 'find the most common used after 50 trials and choose option based on that and if it is not the needed output there will be another section which chooses the output based on previous code'

import random
def move(my_history, their_history, my_score, their_score):  #defines the various moves
    z = ['b','b','c','b']   #sets z to be betray, betray, collude, collude
    word_list = [their_history[i:i+1] for i in range(0, len(their_history))] #sets word list 
    word_counter = {}
    for word in word_list: # 
        if word in word_counter:  #if word is in the word counter
            word_counter[word] += 1 #set word counter to be word_coutner = word = 1
        else:
            word_counter[word] = 1  #sets the word to 1
    popular_words = sorted(word_counter, key = word_counter.get, reverse = True) #
    top_1 = popular_words[:1]
    if len(my_history) >= 50 and top_1 == ['c']: #
        return 'c'
    else:
        if len(my_history) >= 1 and their_history[-1] == 'b': #alternatively, if my_history is greater than or equal to 1 AND their previous history is betray
            return z[random.randint(0,2)] 
        if len(my_history) >= 1 and their_history[-1] == 'c': #if they have a number of colludes in their history one turn ago, reutn c
            return 'c'
    if len(my_history)==0: #return collude if my_history is 0
        return 'c'
