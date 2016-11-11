prompt = '\nEnter the name of a city you want to visit (type \'list\' to view list, \'quit\' to quit): '

cityList = []

while True:
    city = input(prompt)

    if city == 'list':
        print('And here is your list of cities you want to visit: ')
        for city in cityList:
            print(city.title())
    elif city == 'quit':
        break
    else:
        print('Adding: ' + city.title())
        cityList.append(city)