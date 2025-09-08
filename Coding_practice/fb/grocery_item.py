# python(3) - a list of tuple was give for a grocery store items for a date, return the item with highest avg price.
# first element is the list is the header of - date, item, price.
# [(date, item, price),
# (xxx, fruits, 3.0),
# (xxx, milk, 3.0),
# (xxx, fruits, 3.0),
# ....
# ]

def highest_avg_price(l):
    avg_price = {}
    for d,i,p in l:
        if i in avg_price:
            avg_price[i] = (avg_price[i][0]+p , 1+ avg_price[i][1])
        else:
            avg_price[i] = (p,1)
    print(avg_price)
    return sorted(avg_price.items(), key=lambda x: -(x[1][0]/x[1][1]))[0][0]

print(highest_avg_price([('xxx', 'fruits', 3.0),('xxx', 'milk', 4.0),('xxx', 'fruits', 5.0)]))