from random import choice


def daily_workout():

    workouts = ['squats', 'push-ups', 'plank', 'side-planks (Each Side)', 'jumping jacks', 'sit-ups', 'burpees',
                'leg raises', 'mountain climbers']
    time = ['30 Seconds', '45 Seconds', '60 Seconds']
    reps = ['8', '12', '16', '20', '24', '30']
    exNum = [1, 2, 3]

    start = 0
    finish = 3

    while start < finish:

        pulled = choice(workouts)
        random_time = choice(time)
        random_reps = choice(reps)

        print('Exercise ' + str(exNum[0]) + ': ' + pulled.title())

        exNum.pop(0)

        if pulled == 'plank' or pulled == 'side-planks (Each Side)':
            print('Time: ' + random_time)
            print()
        else:
            print('Reps: ' + random_reps)
            print()

        workouts.remove(pulled)

        start += 1

daily_workout()