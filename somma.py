
def predict(data):
     
    values_per_month = []
    l = len(data)
    print(l)

    for i in range(0, l-1):
        one_month = data[i+1] - data[i]
        values_per_month.append(one_month)
    
    somma = sum(values_per_month)
    lung = len(values_per_month)
    avg_vpm = somma / lung
    print(avg_vpm)

    pred_result = data[-1] + avg_vpm
        
    return pred_result

lista = [475.3, 581.3, 646.9]

incr_model = predict(lista)
print(incr_model)