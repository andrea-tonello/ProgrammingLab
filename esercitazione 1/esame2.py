# custom exception
class ExamException(Exception):
  pass

# class used to calculate list moving avarage
class MovingAverage():
  def __init__(self, window_length = None, *args):
    _DEFAULT_WINDOW_LENGTH = 2

    if len(args) > 0:
      print(f"Attenzione, presenza di parametri superflui -> {args}")

    # existence check
    if(window_length == None):
      raise ExamException(f"!! Nessun paramtero passato, prendo come default window_length = {_DEFAULT_WINDOW_LENGTH}")

    # type check
    if not isinstance(window_length, int):
        raise ExamException("window_length deve essere int")
          
    # value validity check
    if(window_length <= 0):
      raise ExamException(f"!! ATTENZIONE! window_length dev'essere > 0. Prendo come default window_length = {_DEFAULT_WINDOW_LENGTH}")
    
    # check passed
    self.window_length = window_length

  def compute(self, numbers = None, *args):
    if len(args) > 0:
      print(f"Attenzione, presenza di parametri superflui -> {args}")

    # existence check
    if numbers == None:
      raise ExamException(f"!! Nessun paramtero passato(richiesta una lista di numeri), non posso calcolare la media mobile")
    
    # type check
    if not isinstance(numbers, list):
      raise ExamException(f"!! Richiesta lista, ricevuto {type(numbers)}. Non posso calcolare la media mobile")

    if not all(type(n) == int or float for n in numbers):
      raise ExamException('Ricontrollare il tipo di dati della lista')
      
    # length check
    if len(numbers) < self.window_length:
      raise ExamException(f"!! Lunghezza della lista passata pari a {len(numbers)}. La lunghezza della finestra di quest'istanza è {self.window_length}. Non posso calcolare la media mobile")

    # items type check
    for index, item in enumerate(numbers):
      try:
        item = float(item)
        numbers[index] = item
      except:
        raise ExamException(f"!! Non tutti gli elementi della lista sono numerici. Non posso calcolare la media mobile.")

    # check passed
    mean = [sum(numbers[i:i + self.window_length]) / self.window_length for i in range(0, len(numbers) - self.window_length + 1)]

    return mean


moving_avg = MovingAverage(2)

result = moving_avg.compute([2,'a',8,16,32])

print(result)