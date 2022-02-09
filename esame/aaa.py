lista = [[[0],[0]],[[1],[1]],[[2],[2]]]
print(lista)
flat_list = [item for sublist in lista for item in sublist]
print(flat_list)