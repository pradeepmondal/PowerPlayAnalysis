import csv

with open('./PowerPlay.csv') as pp:
    crd = csv.reader(pp, delimiter=',')
    line_c = 0 #to track the row number
    ball = 0 # to track each ball in over
    j = 0
    db = 0
    tdb = 0
    db_l =[] #values of no. of dot balls in each innings
    for i in crd:
        ball = 0 #start from first over first ball
        if(line_c==0):
            line_c=line_c+1
            continue
        db = 0 #setting no. of dot balls to 0 for the new inning
        j = 5 #start from first ball of the innings
        while(j<len(i)):
            if(i[j]=='0'):
                tdb = tdb + 1
                db = db+1
            ball = ball + 1
            if(ball==11):
                j=j+3
                ball = 0
                continue
            j=j+1
        if(line_c!=0):
            db_l.append(db) #appending no. of dot balls in the previous inning to the list
        line_c=line_c+1
        if(line_c==1599):
            break

u_db_l = set(db_l)
dict_f = {}
for i in range(0,31):
    if(i in u_db_l):
        dict_f[i]=db_l.count(i)
    else:
        dict_f[i]=0

print(dict_f)

with open('Result.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["No. of dot balls","-","No. of innings"])
    for i in range(0,31):
        writer.writerow([i,"-",dict_f[i]])

    writer.writerow(["Total no. of dot balls in all the innings","-",tdb])
    
