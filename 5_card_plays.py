from itertools
import groupby
from itertools
import combinations
from collections
import defaultdict
import operator
values = {
  '3D': 1,
  '3C': 2,
  '3H': 3,
  '3S': 4,
  '4D': 5,
  '4C': 6,
  '4H': 7,
  '4S': 8,
  '5D': 9,
  '5C': 10,
  '5H': 11,
  '5S': 12,
  '6D': 13,
  '6C': 14,
  '6H': 15,
  '6S': 16,
  '7D': 17,
  '7C': 18,
  '7H': 19,
  '7S': 20,
  '8D': 21,
  '8C': 22,
  '8H': 23,
  '8S': 24,
  '9D': 25,
  '9C': 26,
  '9H': 27,
  '9S': 28,
  '0D': 29,
  '0C': 30,
  '0H': 31,
  '0S': 32,
  'JD': 33,
  'JC': 34,
  'JH': 35,
  'JS': 36,
  'QD': 37,
  'QC': 38,
  'QH': 39,
  'QS': 40,
  'KD': 41,
  'KC': 42,
  'KH': 43,
  'KS': 44,
  'AD': 45,
  'AC': 46,
  'AH': 47,
  'AS': 48,
  '2D': 49,
  '2C': 50,
  '2H': 51,
  '2S': 52
}
card_order_dict = {
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "0": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14,
  "2": 15
}
def play(hand, is_start_of_round, play_to_beat, round_history, player_no, hand_sizes, scores, round_no):
  ""
"
The parameters to this

function are:
  * `hand`: A list of card strings that are the card(s) in your hand.*`is_start_of_round`: A Boolean that indicates whether or not the `play`

function is being asked to make the first play of a round.*`play_to_beat`: The current best play of the trick.If no such play exists(you are the first play in the trick), this will be an empty list.*`round_history`: A list of * trick_history * entries.
A * trick_history * entry is a list of * trick_play * entries.
Each * trick_play * entry is a `(player_no, play)`
2 - tuple, where `player_no`
is an integer between 0 and 3(inclusive) indicating which player made the play, and `play`
is the play that said player made, which will be a list of card strings.*`player_no`: An integer between 0 and 3(inclusive) indicating which player number you are in the game.*`hand_sizes`: A 4 - tuple of integers representing the number of cards each player has in their hand, in player number order.*`scores`: A 4 - tuple of integers representing the score of each player at the start of this round, in player number order.*`round_no`: An integer between 0 and 9(inclusive) indicating which round number is currently being played.

This

function should
return an empty list(`[]`) to indicate a pass(see "Playing a Round"), or a list of card strings, indicating that you want to play these cards to the table as a valid play.
""
"
deck = list(values.keys())# card counter# example of what round_history = [
  [(3, ['AD']), (0, ['2S']), (1, [])][(0, ['3C']), (0, ['2S']), (1, [])]
]
played_cards = []# cards that can not be played A: because they already have been played and B: because they are in my hand
played_cards.extend(hand)
trick_plays = []
for item in round_history:
  for sublist in item:
  for i in sublist:
  trick_plays.append(i)
for item in trick_plays:
  if isinstance(item, list):
  played_cards.extend(item)
played_cards_values = []
for sublist in played_cards:
  valued = values.get(sublist)
played_cards_values.append(valued)
remaining_cards = (list(set(deck) - set(played_cards)))

mydict = {}
for k, g in groupby(hand, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
else :
  mydict[k] = list(g)
groups = [v
  for k, v in mydict.items()
]
hand_tt = []
fives = list(combinations(hand, 5))# all possible 5 card combos.lets me use poker hand formulas also: )
fives_fullhouse = []
fives_flush = []
fives_straight = []
fives_four = []
fives_straight_flush = []


# this is a stupidly long script
for checking what play_to_beat is.#full house p1
def check_full_house(play_to_beat):
  values2 = [i[0]
    for i in play_to_beat
  ]
value_counts = defaultdict(lambda: 0)
for v in values2:
  value_counts[v] += 1
if sorted(value_counts.values()) == [2, 3]:
  return True
return False# flush p1
def check_flush(play_to_beat):
  suits = [i[1]
    for i in play_to_beat
  ]
if len(set(suits)) == 1:
  return True
else :
  return False# straight p1
def check_straight(play_to_beat): #check straight
values2 = [i[0]
  for i in play_to_beat
]
value_counts = defaultdict(lambda: 0)
for v in values2:
  value_counts[v] += 1
rank_values = [card_order_dict[i]
  for i in values2
]
value_range = max(rank_values) - min(rank_values)
if len(set(value_counts.values())) == 1 and(value_range == 4):
  return True
else :
  return False# four of a kind p1
def check_four_of_a_kind(play_to_beat):
  values2 = [i[0]
    for i in play_to_beat
  ]
value_counts = defaultdict(lambda: 0)
for v in values2:
  value_counts[v] += 1
if sorted(value_counts.values()) == [1, 4]:
  return True
return False# straight flush
def check_straight_flush(play_to_beat):
  if check_flush(play_to_beat) and check_straight(play_to_beat):
  return True
else :
  return False



for sublist in fives: #check full house
values1 = [i[0]
  for i in sublist
]
value_counts = defaultdict(lambda: 0)
for v in values1:
  value_counts[v] += 1
if sorted(value_counts.values()) == [2, 3]:
  hand_tt.append(sublist)
fives_fullhouse.append(sublist)# check flush
suits = [h[1]
  for h in sublist
]
if len(set(suits)) == 1:
  hand_tt.append(sublist)
fives_flush.append(sublist)# check straight
value_counts = defaultdict(lambda: 0)
for v in values1:
  value_counts[v] += 1
rank_values = [card_order_dict[i]
  for i in values1
]
value_range = max(rank_values) - min(rank_values)
if len(set(value_counts.values())) == 1 and(value_range == 4):
  hand_tt.append(sublist)
fives_straight.append(sublist)# check four of a kind
value_counts = defaultdict(lambda: 0)
for v in values1:
  value_counts[v] += 1
if sorted(value_counts.values()) == [1, 4]:
  hand_tt.append(sublist)
fives_four.append(sublist)# check straight flush
if check_straight_flush(item):
  fives_straight_flush.append(item)

# cleaner uppers
hand_tt = [list(elem) for elem in hand_tt]
fives_fullhouse = [list(elem) for elem in fives_fullhouse]
fives_flush = [list(elem) for elem in fives_flush]
fives_straight = [list(elem) for elem in fives_straight]
fives_four = [list(elem) for elem in fives_four]
fives_straight_flush = [list(elem) for elem in fives_straight_flush]




for item in groups:
  if len(hand) == 4: #on the rarest occasion that I have 4 cards in my hand and all of them are teh same value / 4 of a kind - the 5 th cards
if len(item) == 4:
  hand_tt = list(combinations(item, 3))
hand_tt = [list(elem) for elem in hand_tt]
if len(item) == 3: #add already threes
hand_tt.append(item)
elif len(item) == 2: #add already threes
hand_tt.append(item)
elif len(item) == 1:
  hand_tt.append(item)# hand_tt is now built up of pairs, triples, singles and five card plays
hand_tt = sorted(hand_tt, key = lambda k: values[k[0]])

# start of trick or round.
if len(play_to_beat) == 0: #If we are the first play in a round, the 3 D must be in our hand.Play it.#Otherwise, we play a random card from our hand.
if is_start_of_round:
  if '3D' in hand:
  play = hand_tt[0]
return play
else :#start of round# group spam strat alot like the last one except more enclusive
if len(sorted(hand_tt, key = len, reverse = True)) > 1: #fail safe, avoid index error
if len(hand) > 2 and len(sorted(hand_tt, key = len, reverse = True)[-2]) > 1:
  hand_tt.sort(key = len, reverse = True)
play = hand_tt[0]
elif len(hand) == 2: #late game stratergy
play = hand_tt[-1]# plays best card before low card
elif len(hand) == 1:
  play = hand_tt[0]
if len(hand) < 9: #MASSIVE fail safe no opposing player would only be on 1 card on the first tick
if player_no == 3:
  if int(hand_sizes[0]) == 1: #one more fail safe.stops bot from thinking there is a 5 th player
play = hand_tt[-1]
else :
  play = hand_tt[0]
elif int(hand_sizes[player_no + 1]) == 1: #if upcoming player going to win
play = hand_tt[-1]
else :
  play = hand_tt[0]
return play
else :
  play = hand_tt[0]
return play

else :#game in action / not start of tick or round


lower_dominance = False
intermediate_dominance = False
upper_dominance = False
H4 = [i
  for i in hand
  if values.get(i) <= 9
]
H42 = [i
  for i in hand
  if values.get(i) >= 43
]
if len(H4) >= 4:
  lower_dominance = True#
if my hand is dominated by lower cards
else :
  intermediate_dominance = True#
if my hand isnt dominated by lower cards / not bad in the low card rankings
if len(H42) >= 4:
  upper_dominance = True#
if my hand is dominated by good cards# the following program modifys hand in to sublists containing same first character


pairs = False
threes = False
singles = False

fives = False

if len(play_to_beat) > 3: #5 card plays
fives = True
hand_fives = []# seprate list to relate 2
for item in hand_tt:
  if len(item) == 5: #add all five cards plays in hand
hand_fives.append(item)
ptb = []
for item in play_to_beat:
  ptb.append(values.get(item))
greater = []

if check_straight(play_to_beat): #setsup greater
for selected group
greater = [i
  for i in fives_straight
  if values.get(i[-1]) > max(ptb)
]
greater.extend(fives_flush)
greater.extend(fives_fullhouse)
greater.extend(fives_four)
greater.extend(fives_straight_flush)

if check_flush(play_to_beat): #setsup greater
for selected group
greater = [i
  for i in fives_flush
  if values.get(i[0]) > max(ptb)
]
greater.extend(fives_fullhouse)
greater.extend(fives_four)
greater.extend(fives_straight_flush)

if check_full_house(play_to_beat): #setsup greater
for selected group.This is where it gets stupid complicated.because we have to compare the best card in the the three and avoid the pair
mydict1 = {}
for k, g in groupby(play_to_beat, key = lambda x: x[0]):
  if k in mydict1:
  mydict1[k] += g
else :
  mydict1[k] = list(g)
ptb1 = [v
  for k, v in mydict1.items()
]
ptb1.sort(key = len, reverse = True)
ptb = []
if not ptb1:
  greater = []
else :
  for item in ptb1[0]:
  ptb.append(values.get(item))
f_f = []
for sublist in fives_fullhouse:
  mydict = {}
for k, g in groupby(sublist, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
else :
  mydict[k] = list(g)
f_f1 = [v
  for k, v in mydict.items()
]
f_f1.sort(key = len, reverse = True)
for item in f_f1[0]:
  f_f.append(values.get(item))
if max(f_f) > max(ptb):
  greater.append(sublist)
greater.extend(fives_four)
greater.extend(fives_straight_flush)


if check_four_of_a_kind(play_to_beat): #setsup greater
for selected group.now that fullhouses are done: ) lets go again: (
  mydict = {}
  for k, g in groupby(play_to_beat, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
  else :
    mydict[k] = list(g)
  ptb1 = [v
    for k, v in mydict.items()
  ] ptb1.sort(key = len, reverse = True) ptb = []
  if not ptb1:
  greater = []
  else :
    for item in ptb1[0]:
    ptb.append(values.get(item))
  for sublist in fives_four:
  mydict = {}
  for k, g in groupby(sublist, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
  else :
    mydict[k] = list(g)
  f_f1 = [v
    for k, v in mydict.items()
  ] f_f1.sort(key = len, reverse = True) f_f = []
  for item in f_f1[0]:
  f_f.append(values.get(item)) if max(f_f) > max(ptb):
  greater.append(sublist)

  greater.extend(fives_straight_flush)


  if check_straight_flush(play_to_beat): #setsup greater
  for selected group.Thank flip there is a easy one in here greater = [i
    for i in fives_straight_flush
    if values.get(i[-1]) > max(ptb)
  ]




  elif len(play_to_beat) == 2: #2 cards to beat pairs = True hand_pairs = []# seprate list to relate 2
  for item in groups:
  if len(item) > 2: #split everything into pairs item2 = list(combinations(item, 2)) item = [list(elem) for elem in item2] hand_pairs.extend(item) elif len(item) == 2: #add already pairs hand_pairs.append(item) ptb = []
  for item in play_to_beat:
  ptb.append(values.get(item)) greater = [i
    for i in hand_pairs
    if values.get(i[-1]) > max(ptb)
  ]

  elif len(play_to_beat) == 3: #3 cards to beat threes = True hand_threes = []# seprate list to relate 2
  for item in groups:
  if len(item) > 3: #split everything into pairs item2 = list(combinations(item, 3)) item = [list(elem) for elem in item2] hand_threes.extend(item) elif len(item) == 3: #add already threes hand_threes.append(item) ptb = []
  for item in play_to_beat:
  ptb.append(values.get(item)) greater = [i
    for i in hand_threes
    if values.get(i[-1]) > max(ptb)
  ]

  elif len(play_to_beat) == 1: #1 card to beat singles = True greater = [i
    for i in hand
    if values.get(i) > values.get(play_to_beat[-1])
  ]# list of cards in hand greater then card just played greater = [
    [i]
    for i in greater
  ]




  if len(hand) < 9: #MASSIVE fail safe no opposing player would only be on 1 card
  while I still have 10
  if player_no == 3:
  if int(hand_sizes[0]) == 1: #one more fail safe.stops bot from thinking there is a 5 th player
  if not greater: #failsafe
  if bot dosent have card
  return []
  else :
    play = greater[-1]
  return play
  elif int(hand_sizes[player_no + 1]) == 1: #if upcoming player going to win
  if not greater: #failsafe
  if bot dosent have card
  return []
  else :
    if not greater: #if bot cant beat
  return []
  else :
    play = greater[-1]# best card
  return play



  if len(hand) > 8: #if early game keeps bot from waisting high cards
  if lower_dominance:
  if pairs or threes:
  if len(greater) == 1:
  return []
  elif singles:
  if len(greater) == 2:
  return []
  if intermediate_dominance:
  if len(greater) == 1:
  return []
  if upper_dominance:
  if pairs or threes:
  if len(greater) == 1:
  return []
  if singles:
  if len(greater) == 4:
  return []

  if len(play_to_beat) == 5: #good failsafe in all other card plays(1, 2, 3) the bot would save its high cards
  while in 5 it didnt, heres the fix: )
if len(greater) == 1:
  for item in greater[0]:
  ptbb = []
ptbb.append(values.get(item))
if max(ptbb) > 44:
  return []

if len(hand) > 5: #update dont want to stop bot from winning when it could have
if singles: #makes sure card that is about to be played isn 't in pair or three
not_paired = []
for item in greater:
  if item in hand_tt:
  not_paired.append(item)
play = not_paired[0]
if not play:
  return []
else :
  return play

if not greater: #if bot cant beat
return []
else :
  if singles: #counting cards algorithm
for singles
beating_cards = range(values.get(greater[-1][-1]), 52)
if all(elem in beating_cards
  for elem in played_cards_values) and(len(hand) < 6): #I will get control of the board with this card
play = greater[-1]
return play
elif pairs: #counting cards algorithm
for pairs
mydict = {}
for k, g in groupby(remaining_cards, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
else :
  mydict[k] = list(g)
remaining_cards1 = [v
  for k, v in mydict.items()
]
remaining_cards1.sort(key = len, reverse = True)
for sublist in remaining_cards1:
  if not len(sublist) > 1:
  play = greater[0]
return play
rems = []
for item in sublist:
  rems.append(values.get(item))
pair = []
for sub in greater:
  for i in sub:
  pair.append(values.get(i))
if max(rems) > max(pair):
  play = sub
return play
elif threes: #counting cards algorithm
for threes
mydict = {}
for k, g in groupby(remaining_cards, key = lambda x: x[0]):
  if k in mydict:
  mydict[k] += g
else :
  mydict[k] = list(g)
remaining_cards1 = [v
  for k, v in mydict.items()
]
remaining_cards1.sort(key = len, reverse = True)
for sublist in remaining_cards1:
  if not len(sublist) > 2:
  play = greater[0]
return play
rems = []
for item in sublist:
  rems.append(values.get(item))
three = []
for sub in greater:
  for i in sub:
  three.append(values.get(i))
if max(rems) > max(three):
  play = sub
return play# working on counting cards algorithm
for fives(its not top of the prioraty list)
play = greater[0]
return play
return []

if __name__ == '__main__': #Write your own test cases
for your `play`

function here.#These can be run with the Run button and will not affect the tournament or marking.

#Here 's an example test case and testing code to kick you off.
TESTS = [#
  [expected
    return value, inputs
  ]
  [
    ['3D', '4D', '7D', '8D', '0D'],
    [
      ['3D', '4D', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [],
      [
        []
      ], 0, [13, 13, 13, 13],
      [0, 0, 0, 0], 0
    ]
  ],
  [
    ['3D', '3C'],
    [
      ['3D', '3C', '4H', '7D', '8D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [],
      [
        []
      ], 0, [13, 13, 13, 13],
      [0, 0, 0, 0], 0
    ]
  ],
  [
    ['3D', '3C', '3H', '4D', '4D'],
    [
      ['3D', '3C', '3H', '4D', '4D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [],
      [
        []
      ], 0, [13, 13, 13, 13],
      [0, 0, 0, 0], 0
    ]
  ],
  [
    ['3D', '4C', '5H', '6D', '7D'],
    [
      ['3D', '4C', '5H', '6D', '7D', '8H', '0D', '0C', 'JH', 'QC', 'QS', 'KH', 'AS'], True, [],
      [
        []
      ], 0, [13, 13, 13, 13],
      [0, 0, 0, 0], 0
    ]
  ],
  [
    [],
    [
      ['8C', '9D'], False, ['7H', '8S', '9C', '0S', 'JC'],
      [
        [
          [3, ['3D', '3H', '3S', '6C', '6S']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['5S']],
          [0, ['JH']],
          [1, ['KC']],
          [2, []],
          [3, ['KS']],
          [0, ['AC']],
          [1, []],
          [2, []],
          [3, ['2C']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['8D']],
          [0, ['2S']],
          [1, []],
          [2, []],
          [3, []]
        ],
        [
          [0, ['4H', '8H', '9H', 'QH', 'KH']],
          [1, []],
          [2, []],
          [3, []]
        ],
        [
          [0, ['5D']],
          [1, ['6H']],
          [2, []],
          [3, ['9S']],
          [0, ['QD']],
          [1, ['AH']],
          [2, []],
          [3, ['2H']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['0D']],
          [0, ['KD']],
          [1, ['AS']],
          [2, []],
          [3, []],
          [0, []]
        ],
        [
          [1, ['7H', '8S', '9C', '0S', 'JC']],
          [2, []],
          [3, []]
        ]
      ], 0, [2, 4, 13, 1],
      [0, 0, 0, 0], 0
    ]
  ],
  [
    ['KD'],
    [
      ['6D', '6S', '7H', '8S', '9C', '9S', '0D', 'JC', 'KD', 'KC', 'AD', 'AH'], False, ['QC'],
      [
        [
          [3, ['3D']],
          [0, ['3H']],
          [1, ['5C']],
          [2, ['JS']],
          [3, ['QC']]
        ]
      ], 0, [12, 12, 12, 11],
      [11, -9, 9, -11], 2
    ]
  ],
  [
    [],
    [
      ['4D', '5C', '5S', '7D', '8D', '0D', '0S', 'JH', 'QD', 'KD', 'KS', '2H', '2S'], False, ['5H', '6H', '7H', '8H', '9H'],
      [
        [
          [3, ['3D', '3C', '3H']],
          [0, ['6D', '6C', '6S']],
          [1, []],
          [2, []],
          [3, []]
        ],
        [
          [0, ['9D', '9C', '9S', 'QC', 'QS']],
          [1, ['5H', '6H', '7H', '8H', '9H']]
        ]
      ], 2, [5, 8, 13, 10],
      [26, -34, 61, -53], 8
    ]
  ],
  [
    ['9C', '9H', 'JD', 'JC', 'JS'],
    [
      ['4S', '5S', '6D', '8S', '9C', '9H', '9S', 'JD', 'JC', 'JS', 'KS', 'AD', '2C'], False, ['0D', '0H', '0S', '3C', '3D'],
      [
        [
          [3, ['0D', '0H', '0S', '3C', '3D']]
        ]
      ], 0, [13, 13, 13, 8],
      [-13, -117, 47, 83], 3
    ]
  ],
  [
    ['7C', '7H'],
    [
      ['4S', '5S', '6C', '7C', '7H', '8H', '9D', 'JH', 'KD', 'KS', 'AD', 'AS', '2C'], False, ['3D', '3S'],
      [
        [
          [1, ['3D', '3S']],
          [2, []],
          [3, []]
        ]
      ], 0, [13, 11, 13, 13],
      [84, -6, -39, -39], 1
    ]
  ],
  [
    ['2D', '2C', '2H'],
    [
      ['2D', '2C', '2H', '2S'], False, [],
      [
        [
          [2, ['3D']],
          [3, ['7C']],
          [0, ['7H']],
          [1, ['8D']],
          [2, ['8C']],
          [3, ['KC']],
          [0, ['AH']],
          [1, []],
          [2, []],
          [3, ['AS']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['3C', '3H', '6D', '6C', '6S']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['AC']],
          [0, []],
          [1, []],
          [2, []]
        ],
        []
      ], 3, [11, 12, 11, 4],
      [6, -25, -50, 69], 9
    ]
  ],
  [
    ['9C', '9H', '9S'],
    [
      ['9C', '9H', '9S'], False, [],
      [
        [
          [1, ['3D', '3H', '3S']],
          [2, []],
          [3, ['0S', '0H', '0C']],
          [0, []],
          [1, ['JD', 'JC', 'JH']],
          [2, []],
          [3, ['AS', 'AH', 'AC']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['3C']],
          [0, ['4S']],
          [1, ['7D']],
          [2, ['7H']],
          [3, ['KH']],
          [0, []],
          [1, ['2D']],
          [2, ['2H']],
          [3, []],
          [0, []],
          [1, []]
        ],
        [
          [2, ['QC', 'QH']],
          [3, []],
          [0, []],
          [1, []]
        ],
        [
          [2, ['KC', 'KS']],
          [3, []],
          [0, []],
          [1, []]
        ],
        [
          [2, ['4C']],
          [3, ['6C']],
          [0, ['QS']],
          [1, []],
          [2, ['2S']],
          [3, []],
          [0, []],
          [1, []]
        ],
        [
          [2, ['5H']],
          [3, ['2C']],
          [0, []],
          [1, []],
          [2, []]
        ],
        [
          [3, ['5S', '5C']],
          [0, ['6D', '6H']],
          [1, ['8C', '8H']],
          [2, []],
          [3, []],
          [0, ['8D', '8S']],
          [1, []],
          [2, []],
          [3, []]
        ],
        [
          [0, ['5D']],
          [1, ['7C']],
          [2, ['7S']],
          [3, []],
          [0, ['KD']],
          [1, []],
          [2, []],
          [3, []]
        ],
        [
          [0, ['6S']],
          [1, ['QD']],
          [2, []],
          [3, []],
          [0, ['AD']],
          [1, []],
          [2, []],
          [3, []]
        ],
        []
      ], 0, [3, 1, 3, 1],
      [4, 32, -26, -10], 2
    ]
  ]
]# This runs the above test cases.
for i, test in enumerate(TESTS):
  expected_return_value, inputs = test
actual_return_value = play( * inputs)
if actual_return_value == expected_return_value:
  print('PASSED {}/{}.'.format(i + 1, len(TESTS)))
else :
  print('FAILED {}/{}.'.format(i + 1, len(TESTS)))
print('    inputs:', repr(inputs))
print('  expected:', repr(expected_return_value))
print('    actual:', repr(actual_return_value))