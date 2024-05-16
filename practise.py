def calculate_score(rounds):
    shapes = {"A": 1, "B": 2, "C": 3}
    outcomes = {"X": 0, "Y": 3, "Z": 6}
    total_score = 0
    for round in rounds:
        opponent_move, outcome = round
        total_score += shapes[opponent_move] + outcomes[outcome]

        print(f"The total score is: {total_score}")

    file_patch = 'input_2_cap1.txt'
    
