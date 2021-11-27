from datetime import datetime 

def shampoo_dates():
    dates = []
    file = open('shampoo_sales.csv', 'r')
    for line in file:
        elements = line.split(',')
        if elements[0] != 'Date':
            lista_delle_date = datetime.strptime(elements[0],'%d-%m-%Y')
            dates.append(lista_delle_date)
    
        
    return dates
    file.close()

print("Dates:\n")
date_finali = shampoo_dates()
for line in date_finali:
    print(line.strftime('%d - %b - %Y'))
