import csv
from scipy.stats import binom
n = 36
p = 0.528
rv = []
dist = {}

for i in range(n+1):
    rv.append(i)
dist = [binom.pmf(r, n, p) for r in rv]


with open('Binom.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No. of dot balls","-","Probability of dot balls in an inning as per binomial distribution"])
    for i in range(n + 1):
        writer.writerow([str(rv[i]),"-", str(f'{dist[i]:.4f}')])
        
