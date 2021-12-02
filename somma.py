class CSVFile():
  def _init_(self, nome):
    if(isinstance(nome, str)):
      self.nome = nome
    else:
      raise Exception("Pino è bello")

  def get_data(self):
    file = open(self.nome, 'r')
    righe = []
    for riga in file:
      dati_riga = riga.split(',')
      righe.append(dati_riga)
    file.close()

    return righe

try:
  csv_file = CSVFile(2)
except Exception as e:
  print(e)