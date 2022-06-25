import csv

class Map:
  def __init__(self, filename):
    self.filepath = './nodemaps/{}'.format(filename)
    with open(self.filepath) as f:
      reader = csv.reader(f)
      self.nodes = list(reader)
      self.tokens = {
        '0': ' . ',
        '1': ' # '
      }

  def draw(self):
    for y, row in enumerate(self.nodes):
      for x, col in enumerate(row):
        print(self.get_token_at(x, y), end='')
      print()

  def get_token_at(self, x, y):
    return self.tokens[self.nodes[x][y]]

