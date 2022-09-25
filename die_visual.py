import pygal
from die import Die

die = Die()

results = []

for roll_num in range(1000):
  result = die.roll()
  results.append(result)

# print(results)

frequences = []
for value in range(1, die.num_sides + 1):
  frequency = results.count(value)
  frequences.append(frequency)
# print(frequences)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [1,2,3,4,5,6]
hist._x_title = "Result"
hist._y_title = "Requency of Result"

hist.add("D6", frequences)
hist.render_to_file("die_visual.svg")