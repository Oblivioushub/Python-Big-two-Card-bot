values={'3D':1, '3C':2, '3H':3, '3S':4, '4D':5, '4C':6, '4H':7, '4S':8, '5D':9, '5C':10, '5H':11, '5S':12, '6D':13, '6C':14, '6H':15, '6S':16, '7D':17, '7C':18, '7H':19, '7S':20, '8D':21, '8C':22, '8H':23, '8S':24, '9D':25, '9C':26, '9H':27, '9S':28, '0D':29, '0C':30, '0H':31, '0S':32, 'JD':33, 'JC':34, 'JH':35, 'JS':36, 'QD':37, 'QC':38, 'QH':39, 'QS':40, 'KD':41, 'KC':42, 'KH':43, 'KS':44, 'AD':45, 'AC':46, 'AH':47, 'AS':48, '2D':49, '2C':50, '2H':51, '2S':52}
def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):  
  """
  The parameters to this function are:
  * `hand`: A list of card strings that are the card(s) in your hand.
  * `is_start_of_round`: A Boolean that indicates whether or not the `play` function is being asked to make the first play of a round.
  * `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
  * `round_history`: A list of *trick_history* entries.
    A *trick_history* entry is a list of *trick_play* entries.
    Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
  * `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
  * `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order. 
  * `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
  * `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.

  This function should return an empty list (`[]`) to indicate a pass (see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
  """
  # If we are starting a trick, we cannot pass.
  if len(play_to_beat) == 0:
    # If we are the first play in a round, the 3D must be in our hand. Play it.
    # Otherwise, we play a random card from our hand.
    if is_start_of_round:
      if '3D' in hand:
        play = ['3D']
      else:
        play = [hand[0]]
      return play
    else:
      if len(hand) == 2: #late game stratergy
        play = [hand[-1]] #plays best card before low card
        return play
      if len(hand) < 9: #MASSIVE fail safe no opposing player would only be on 1 card on the first tick
        if player_no == 3:
          if int(hand_sizes[0]) == 1: #one more fail safe. stops bot from thinking there is a 5th player
            play = [hand[-1]] #best card
          else:
            play = [hand[0]]
        elif int(hand_sizes[player_no + 1]) == 1: #if upcoming player going to win
          play = [hand[-1]] #best card
        else:
          play = [hand[0]]
      else:
        play = [hand[0]]
      return play

  else: #game in action/not start of tick or round


    lower_dominance = False
    intermediate_dominance = False
    upper_dominance = False
    H4 = [i for i in hand if values.get(i) <= 9]
    H42 = [i for i in hand if values.get(i) >= 43]
    if len(H4)>=4:
        lower_dominance = True #if my hand is dominated by lower cards
    else:
        intermediate_dominance = True #if my hand isnt dominated by lower cards/not bad in the low card rankings
    if len(H42)>=4:
        upper_dominance = True #if my hand is dominated by good cards

        
    greater = [i for i in hand if values.get(i) > values.get(play_to_beat[-1])] #list of cards in hand greater then card just played
    if len(hand) < 9: #MASSIVE fail safe no opposing player would only be on 1 card while I still have 10
      if player_no == 3:
        if int(hand_sizes[0]) == 1: #one more fail safe. stops bot from thinking there is a 5th player
          if not greater: #failsafe if bot dosent have card
            return []
          else:
            play = [greater[-1]]
            return play
      elif int(hand_sizes[player_no + 1]) == 1: #if upcoming player going to win
        if not greater: #failsafe if bot dosent have card
          return []
        else:
          if not greater:#if bot cant beat
            return []
          else:
            play = [greater[-1]] #best card
            return play
    if len(hand) > 6: #if early game keeps bot from waisting high cards
        if lower_dominance:
          if len(greater) == 2:
            return []
        if intermediate_dominance:
          if len(greater) == 1:
            return []
        if upper_dominance:
          if len(greater) == 4:
            return []


    if not greater:#if bot cant beat
        return []
    else:
        play = [greater[0]]
    return play
  return []  

if __name__ == '__main__':
  # Write your own test cases for your `play` function here.
  # These can be run with the Run button and will not affect the tournament or marking.
  
  # Here's an example test case and testing code to kick you off.
  TESTS = [  # [ expected return value, inputs ]
    [['3D'], [['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [], [[]], 0, [13, 13, 13, 13], [0, 0, 0, 0], 0]],
    # Add more tests here.
  ]
  # This runs the above test cases.
  for i, test in enumerate(TESTS):
    expected_return_value, inputs = test
    actual_return_value = play(*inputs)
    if actual_return_value == expected_return_value:
      print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
    else:
      print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
      print('    inputs:', repr(inputs))
      print('  expected:', repr(expected_return_value))
      print('    actual:', repr(actual_return_value))