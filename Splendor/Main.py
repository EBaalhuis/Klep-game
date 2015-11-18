import Card
import itertools

colors= ["white", "green", "black", "blue", "red"]

# Generate list of cards from txt file
cardList = []
f = open("cards.txt")
cardLines = f.readlines()
for line in cardLines:
    newCard = Card.Card(line.split(","))
    cardList.append(newCard)

# Create table of color-to-color total costs
color_to_color = [[0 for x in range(5)] for x in range(5)]
for col_from in colors:
    for col_to in colors:
        color_to_color[colors.index(col_from)][colors.index(col_to)] = sum(int(c.costs[col_from]) for c in cardList if (c.gem == col_to))

white_red_rel = color_to_color[colors.index("white")][colors.index("red")] + color_to_color[colors.index("red")][colors.index("white")]
#print(white_red_rel)

for pair in itertools.combinations(colors, 2):
    score = color_to_color[colors.index(pair[0])][colors.index(pair[1])] + color_to_color[colors.index(pair[1])][colors.index(pair[0])]
    print("Score for " + pair[0] + " and " + pair[1] + " is " + str(score))