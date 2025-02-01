# def rock_paper_scissors(player1, player2):
#     choices = ["rock", "paper", "scissors"]
    
#     if player1 == player2:
#         return "Tie"
#     elif (player1 == "rock" and player2 == "scissors") or \
#          (player1 == "scissors" and player2 == "paper") or \
#          (player1 == "paper" and player2 == "rock"):
#         return "Player 1 wins"
#     else:
#         return "Player 2 wins"



def winner(player1, player2):
    player1_score = player1[0] + player1[1] + (player1[0] + player1[1]) * (player1[2] / 10)
    player2_score = player2[0] + player2[1] + (player2[0] + player2[1]) * (player2[2] / 10)
    
    if player1_score > player2_score:
        return "Player 1 wins"
    elif player2_score > player1_score:
        return "Player 2 wins"
    else:
        return "Tie"

player1 = [5, 6, 8]  
player2 = [10, 7, 6]  

print(winner(player1, player2))