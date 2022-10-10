def main():
    player1 = input("(Player1): Rock(R), Paper(P), Scissors(S)")
    player2 = input("(Player2): Rock(R), Paper(P), Scissors(S)")

    def player1Wins(player1, player2):
        if player1 == "R" and player2 == "S":
            print("Player1 wins")
        elif player1 == "S" and player2 == "P":
            print("Player1 wins")
        elif player1 == "P" and player2 == "R":
            print("Player1 wins")

    def player2Wins(player1, player2):
        if player2 == "R" and player1 == "S":
            print("Player2 wins")
        elif player2 == "S" and player1 == "P":
            print("Player2 wins")
        elif player2 == "P" and player1 == "R":
            print("Player2 wins")

    def draw(player1, player2):
        if player1 == player2:
            print("It's a draw.")
    player1Wins(player1, player2)
    player2Wins(player1, player2)
    draw(player1, player2)


if __name__ == "__main__":
    main()
