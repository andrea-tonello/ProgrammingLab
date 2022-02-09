timeseries = [['a',11],['b',12],['c',0],['d',14],['e',15],['f',16],['g',17],['h',18],['i',19],['j',20],['k',21],['l',22],['a',21],['b',22],['c',23],['d',24],['e',25],['f',26],['g',27],['h',28],['i',29],['j',30],['k',31],['l',0]]

tot = 1950-1949+1
results = []

for i in range(0,12):
    results.append([])

month_index = 0
for i in range(0,12):
    sum = 0
    for j in range(0,tot):
        results[i].append(timeseries[month_index + sum][1])
        sum += 12
    month_index += 1

for month in results:
        for value in month:
            if value <= 0:
                month.remove(value)

print(results)
print()

final = []
for month in results:
    if len(month) <= 1:
        final.append(0)
    else:
        res = 0
        j = 1
        while j<len(month):
            res = res + (month[j]-month[j-1])
            j += 1
        print(res)
        final.append(res / (len(month)-1))
            
        
print(final)