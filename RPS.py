# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)
#
#     guess = "R"
#     if len(opponent_history) > 2:
#         guess = opponent_history[-2]
#
#     return guess


def player(prev_play, opponent_history=[], my_history=[], play_order=[{
    "RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0,
}, {"RR": 0,
    "RP": 0,
    "RS": 0,
    "PR": 0,
    "PP": 0,
    "PS": 0,
    "SR": 0,
    "SP": 0,
    "SS": 0, }]):
    opponent_history.append(prev_play)
    guess = "P"
    pmost_frequent = "P"
    most_frequent = "P"

    if len(opponent_history) > 11:

        # ----------- auxiliary variables to determine if I play against mrugesh -----------
        pre_last_ten = my_history[-11:-1]
        last_ten = my_history[-10:]
        pmost_frequent = max(set(pre_last_ten), key=pre_last_ten.count)
        most_frequent = max(set(last_ten), key=last_ten.count)
        # -------------------------------------- end ---------------------------------------

        # ------------ auxiliary variables to determine if I play against abbey ------------
        pre_last_two = "".join(my_history[-3:-1])
        if len(pre_last_two) == 2:
            play_order[1][pre_last_two] += 1
        pre_plays = [my_history[-2] + "R", my_history[-2] + "P", my_history[-2] + "S"]
        pre_sub_order = {
            k: play_order[1][k]
            for k in pre_plays if k in play_order[1]
        }
        pre_prediction = max(pre_sub_order, key=pre_sub_order.get)[-1:]

        last_two = "".join(my_history[-2:])
        if len(last_two) == 2:
            play_order[0][last_two] += 1
        my_potential_plays = [my_history[-2] + "R", my_history[-2] + "P", my_history[-2] + "S"]
        sub_order = {
            k: play_order[0][k]
            for k in my_potential_plays if k in play_order[0]
        }
        prediction = max(sub_order, key=sub_order.get)[-1:]
        # -------------------------------------- end ---------------------------------------

        # --------------------- I check if I play against quincy --------------------------
        if (opponent_history[-1] == 'R') and (opponent_history[-2] == 'S') and \
                (opponent_history[-3] == 'P') and (opponent_history[-4] == 'P') and \
                (opponent_history[-5] == 'R'):
            guess = "P"
        elif (opponent_history[-1] == 'S') and (opponent_history[-2] == 'P') and \
                (opponent_history[-3] == 'P') and (opponent_history[-4] == 'R') and \
                (opponent_history[-5] == 'R'):
            guess = "P"
        elif (opponent_history[-1] == 'P') and (opponent_history[-2] == 'P') and \
                (opponent_history[-3] == 'R') and (opponent_history[-4] == 'R') and \
                (opponent_history[-5] == 'S'):
            guess = "R"
        elif (opponent_history[-1] == 'P') and (opponent_history[-2] == 'R') and \
                (opponent_history[-3] == 'R') and (opponent_history[-4] == 'S') and \
                (opponent_history[-5] == 'P'):
            guess = "S"
        elif (opponent_history[-1] == 'R') and (opponent_history[-2] == 'R') and \
                (opponent_history[-3] == 'S') and (opponent_history[-4] == 'P') and \
                (opponent_history[-5] == 'P'):
            guess = "S"


        # ------------------------ I check if I play against abbey ---------------------------
        elif (pre_prediction == 'R' and opponent_history[-1] == 'P') or \
                (pre_prediction == 'S' and opponent_history[-1] == 'R') or \
                (pre_prediction == 'P' and opponent_history[-1] == 'S'):

            if prediction == 'R':
                guess = "S"
            elif prediction == 'S':
                guess = "P"
            elif prediction == 'P':
                guess = "R"


        # ---------------------------- I check if I play against kris ------------------------
        elif (my_history[-2] == 'R' and opponent_history[-1] == 'P') or \
                (my_history[-2] == 'S' and opponent_history[-1] == 'R') or \
                (my_history[-2] == 'P' and opponent_history[-1] == 'S'):
            if my_history[-1] == 'R':
                guess = "S"
            elif my_history[-1] == 'S':
                guess = "P"
            elif my_history[-1] == 'P':
                guess = "R"


        # ---------------------------- I check if I play against mrugesh ---------------------
        elif pmost_frequent == 'R' and opponent_history[-1] == 'P' or \
                (pmost_frequent == 'S' and opponent_history[-1] == 'R') or \
                (pmost_frequent == 'P' and opponent_history[-1] == 'S'):
            if most_frequent == 'R':
                guess = "S"
            elif most_frequent == 'S':
                guess = "P"
            elif most_frequent == 'P':
                guess = "R"


        else:
            guess = 'R'

    my_history.append(guess)
    return guess
