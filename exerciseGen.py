from random import choice


def daily_workout():
    """A function that gives three sets of three different exercises, with reps/seconds provided. This one taught me
    about pulling random items from a list using the choice method"""

    # This indicates the order of sets
    sets = [1, 2, 3]
    # Variable to indicate 0 as the start for sets
    setStart = 0
    # And finish set for 3, to be used with the entire set loop
    setFinish = 3

    # This is the set loop. With each loop, three exercises will be generated, and the loop runs three times
    while setStart < setFinish:
        # The first list contains the different exercises
        workouts = ['squats', 'push-ups', 'plank', 'side-planks (Each Side)', 'jumping jacks', 'sit-ups', 'burpees',
                    'leg raises', 'mountain climbers']
        # Here, a list of the seconds (for exercises that are timed)
        time = ['30 Seconds', '45 Seconds', '60 Seconds']
        # A list of reps to be provided
        reps = ['8', '12', '16', '20', '24', '30']

        # This tells the order of the exercises
        exNum = [1, 2, 3]
        # Variable to indicate 0 as the start for exercises
        exStart = 0
        # And finish set for 3. To be used with the exercise while loop
        exFinish = 3

        # This prints the initial set, with the first item within the set list
        print('\nSet ' + str(sets[0]) + ':')
        # Once the above is printed, this removes the first item from the list, leaving the next item avail for the
        # following loop
        sets.pop(0)

        while exStart < exFinish:
            """The heart of the function. While 'start' is less than 'finish', it will run"""

            # Variable 'pulled' being the random item pulled from the workouts list
            pulled = choice(workouts)
            # Variable 'random_time' being the random item pulled from the time list
            random_time = choice(time)
            # Variable 'random_reps' being the random item pulled from the reps list
            random_reps = choice(reps)

            # The first item printed. Will state 'Exercise', followed by the first item of the exNum list, followed by
            # the 'pulled' item from the exercise list
            print('\n\tExercise ' + str(exNum[0]) + ': ' + pulled.title())

            # Once the number of exercise is printed, this pops that same item off, leaving the next sequential item
            exNum.pop(0)

            # If the item for pulled is a timed item, then this pulls from the 'time' list
            if pulled == 'plank' or pulled == 'side-planks (Each Side)':
                print('\tTime: ' + random_time)

            # If not, it pulls from the 'reps' list
            else:
                print('\tReps: ' + random_reps)

            # This will to into the 'workouts' list, and remove the 'pulled' item, so the same exercise isn't
            # duplicated
            workouts.remove(pulled)

            # And here, once all of the above while statement is done, it adds a 1 to the start value. Once this is
            # equal
            # to finish, or 3, it will not run again, giving only 3 exercises.
            exStart += 1
        # Adds 1 to the setStart variable, increasing each time the look runs, until it hits less than three
        setStart += 1

# And this runs the whole thing
daily_workout()

# Test note/commit