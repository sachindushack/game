board=["-","-","-","-","-","-","-","-","-"]

game_going= True

winner=None

current_player="X"

def print_board():
  for i in board:
    row1= "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2= "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3= "|{}|{}|{}|".format(board[6],board[7],board[8])
  print(row1)
  print(row2)
  print(row3)



def play_game():
  print_board()
  while game_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner=="X" or winner=="O":
    print(winner +" " + "won")
  elif winner=="None":
    print("Tie")



def handle_turn(player):
  position=int(input("Enter position where you want to enter first(0-9)"))
  position=int(position-1)
  board[position]=player
  print_board()

def check_if_game_over():
  check_if_win()
  check_if_tie()
  
def check_if_win():
  
  global winner
  row_winner=check_rows()
  column_winner=check_column()
  diagonal_winner=check_diagonal()
  
  if row_winner:
    winner=row_winner
  elif column_winner:
    winner=column_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else:
    winner==None
  return
  
def check_rows():
  
  global game_going
  
  row1=board[0]==board[1]==board[3]!="-"
  row2=board[4]==board[5]==board[5]!="-"
  row3=board[6]==board[7]==board[8]!="-"
  
  if row1 or row2 or row3:
    game_going=False
    
  if row1:
    return board[0]
    
  elif row2:
    return board[3]
    
  elif row3:
    return board[6]
  
  return
  
def check_column():
  global game_going
  clm1=board[0]==board[3]==board[6]!="-"
  clm2=board[1]==board[4]==board[7]!="-"
  clm3=board[2]==board[5]==board[8]!="-"
  
  if clm1 or clm2 or clm3:
    game_going=False
    
  if clm1:
    return board[0]
    
  elif clm2:
    return board[1]
    
  elif clm3:
    return board[2]
  return

def check_diagonal():
  global game_going
  
  diag1=board[0]==board[4]==board[8]!="-"
  diag2=board[2]==board[4]==board[6]!="-"
  
  
  if diag1 or diag2 :
    game_going=False
    
  if diag1:
    return board[0]
    
  elif diag2:
    return board[6]
    
  
  return
  
def check_if_tie():
  
  global game_going
  
  if "-" not in board:
    game_going=False
    
  
  return

def flip_player():
  
  global current_player
  
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
  return
play_game()
    
