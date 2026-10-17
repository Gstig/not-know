word = 'strinGLine, colOumn, Case, Vase, continent'

#print(word[1]) #printing letters

#print(len(word)) measuring #length

#print(word.count('!')) #counting symbols

#print(word.upper()) #uppercase

#print(word.lower()) #lowercase

#print(word.isupper()) #determine possessing capital letters

#print(word.islower()) #determine possessing lower letters

#print(word.capitalize()) #capitalize the first letter & lower the rest

#print(word.find('')) #find symbol

#print(word.split(', ')) #spliting the list

things = word.split(', ')

for el in range(len(things)):
    things[el] = things[el].capitalize()
    result = ' , '.join(things)

#print(result)

#index

word = 'Taekwondo'

#print(word[3:-2:2])


list = [6, 3, 'Unforgiven', True, 7.8]

#print(list[2:5:2])
#print(list[::-1])


stuck = 'flucTuaTion,difraction,contamination'

qwe = stuck.split(',')

for i in range(len(qwe)):
    qwe[i] = qwe[i].capitalize()
    ewq = ' - '.join(qwe)

print(ewq)

#print(stuck[1])

#print(len(stuck))

#print(stuck.count('T'))

#print(stuck.upper())

#print(stuck.lower())

#print(stuck.isupper())

#print(stuck.islower())

#print(stuck.capitalize())

#print(stuck.find('f'))

#print(stuck.split(', '))