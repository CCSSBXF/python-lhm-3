import pygal
from die import Die

#15_7
D8_1 = Die(8)
D8_2 = Die(8)
#15_8
D6_1 = Die()
D6_2 = Die()
D6_3 = Die()

results = []
for roll in range(1000):
    #result = D8_1.roll() + D8_2.roll()
    result = D6_1.roll() + D6_2.roll() + D6_3.roll()
    results.append(result)

frequencies = []
# max_result = D8_1.num_sides + D8_2.num_sides
# for value in range(2,max_result+1):
for value in range(3,19):
    frequencies.append(results.count(value))

dog = pygal.Bar()
dog.title = 'two D8'
dog.x_labels = []
# for x in range(2,max_result+1):
for x in range(3,19):
    dog.x_labels.append(str(x))
dog.x_title = 'result'
dog.y_title = 'frequencies'

# dog.add('D8+D8',frequencies)
dog.add('three D6',frequencies)
dog.render_to_file('15_789.svg')
