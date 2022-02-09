timeseries = [['1949-04', 129], ['1949-06', 135], ['1949-07', 148], ['1949-08', 148], ['1949-09', 136], ['1949-11', 104], ['1949-12', 118], ['1950-04', 135], ['1950-05', 125], ['1950-06', 149], ['1950-07', 170], ['1950-08', 170], ['1950-09', 158], ['1950-10', 133], ['1950-11', 114], ['1950-12', 140], ['1951-02', 150], ['1951-03', 178], ['1951-04', 163], ['1951-05', 172], ['1951-06', 178], ['1951-07', 199], ['1951-08', 199], ['1951-09', 184], ['1951-10', 162], ['1951-11', 146], ['1951-12', 166]]

total_years = 1951-1949+1
filled_time_series = []
for i in range(total_years):
    filled_time_series.append([])
    for j in range (0,12):
        filled_time_series[i].append(['-1',1])

print(filled_time_series)
print()

timeseries2 = []

for i in range (1949, 1951+1):
    tmplist = []
    for item in timeseries:
        date = item[0].split('-')
        if str(i) == date[0]:
            tmplist.append(item)
    timeseries2.append(tmplist)

print(timeseries2)

for i,lista in enumerate(timeseries2):
    for element in lista:
        date = element[0].split('-')
        month = date[1]
        monthint = int(month)
        
        for j in range(12):
            if j == monthint-1:
                filled_time_series[i][j] = element

print()
print(filled_time_series)
print()
flat_time_series = [item for sublist in filled_time_series for item in sublist]
print(flat_time_series)

