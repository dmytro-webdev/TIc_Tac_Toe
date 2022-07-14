import random
def show_game_field():
    print(
        f"""
                    _____________________
                   |     {game_field[0][0]}  | {game_field[0][1]}  | {game_field[0][2]}     |
                   |   ________________  |
                   |     {game_field[1][0]}  | {game_field[1][1]}  | {game_field[1][2]}     |
                   |   ________________  |
                   |     {game_field[2][0]}  | {game_field[2][1]}  | {game_field[2][2]}     |
                    _____________________
               """
    )

# def ai():
#     o_row = random.randint(0, 2)
#     o_column = random.randint(0, 2)
#     return o_row, o_column

game_field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

#every winner combination is equal to 15
magic_matrix = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4],
]



count_game_step = 0
end_of_game = False
player_1_score = 0
player_2_score = 0

while not end_of_game:
        show_game_field()
        print("Player 1. Choose the position of your 'x':")
        x_row = int(input("1.Row: "))
        x_column = int(input("2.Column: "))
        game_field[x_row - 1][x_column - 1] = "x"
        player_1_score += magic_matrix[x_row -1][x_column-1]
        #max for 'x' is equal to 5
        count_game_step += 1
        if count_game_step == 5:
            show_game_field()
            print("__________You have a DRAW!!!____________")
            break
        elif player_1_score == 15:
            print("______________PLAYER 1 WIN!_______________")
            show_game_field()
            break
        show_game_field()
        print("Player 2. Choose position of your 'o':")
        o_row = int(input("1.Row: "))
        o_column = int(input("2.Column: "))
        game_field[o_row - 1][o_column - 1] = "o"
        player_2_score += magic_matrix[o_row -1][o_column -1]
        if player_2_score == 15:
            print("___________PLAYER 2 WIN!_______________")
            show_game_field()
            break



