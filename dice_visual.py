import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
  result = die_1.roll() + die_2.roll()
  results.append(result)

frequences = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
  frequency = results.count(value)
  frequences.append(frequency)
# print(frequences)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist._x_title = "Result"
hist._y_title = "Requency of Result"

hist.add("D6 + D6", frequences)
hist.render_to_file("dice_visual.svg")