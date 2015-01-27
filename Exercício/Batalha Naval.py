'''
Bom! Agora vamos usar uma função embutida do Python para gerar nosso tabuleiro, 
que criaremos como uma grade de 5 x5 repleta de "O"s, de "oceano".

print ["O"] * 5
exibirá ['O', 'O', 'O', 'O', 'O'], que é a base para uma linha do nosso tabuleiro.

Vamos fazer isso cinco vezes para criar cinco linhas (Como temos que fazer cinco vezes, um laço parece ser apropriado).
'''
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Vamos jogar Batalha Naval!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


# Tudo a partir daqui deve ir dentro do laco!
# Tenha certeza de recuar quatro espacos!
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Adivinhe a Linha:"))
    guess_col = int(raw_input("Adivinhe a Coluna:"))
    if guess_row == ship_row and guess_col == ship_col:
       print "Parabens, voce afundou meu couracado!"
       break
       
    else:
        if turn >= 3:
            print "Game Over"
        elif (guess_row < 0 or guess_row > 4) or (guess_col < 0          or guess_col > 4):
            print "Oops, isso nao e nem mesmo no oceano."
        elif(board[guess_row][guess_col] == "X"):
            print "Joce ja tentou esse."
        else:
          print "Voce errou meu couracado!"
          board[guess_row][guess_col] = "X"
    # Exiba aqui (turn + 1)!
    
    print_board(board)
