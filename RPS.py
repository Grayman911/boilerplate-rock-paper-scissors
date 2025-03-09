import random

def player(prev_play, opponent_history=[]):
    # Keep track of opponent's history
    if prev_play:
        opponent_history.append(prev_play)
    
    # Start with random move for the first game
    if not opponent_history:
        return random.choice(['R', 'P', 'S'])
    
    # Analyze opponent patterns
    last_5 = opponent_history[-5:]
    common_move = max(set(last_5), key=last_5.count)
    
    # Counter the most common recent move
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    next_move = counter_moves[common_move]
    
    # Switch strategies if opponent adapts
    if len(opponent_history) > 50:
        pattern = ''.join(opponent_history[-10:])
        if pattern.count('R') > 6:
            next_move = 'P'
        elif pattern.count('P') > 6:
            next_move = 'S'
        elif pattern.count('S') > 6:
            next_move = 'R'
    
    return next_move
def play_game():
    opponent_moves = ['R', 'P', 'S', 'R', 'P'] * 2  # Simulate opponent moves
    prev_play = ""
    
    print("Starting Rock-Paper-Scissors game simulation!")
    
    for i, move in enumerate(opponent_moves):
        my_move = player(prev_play)
        print(f"Round {i + 1}: You played {my_move}, Opponent played {move}")
        prev_play = move

# Run the test game
if __name__ == "__main__":
    play_game()

# This function should improve your win rate against predictable bots by recognizing patterns and adjusting!
# Let me know if you want me to refine the logic further or test it against specific bot behaviors. 
