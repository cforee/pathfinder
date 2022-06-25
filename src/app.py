from src.map import Map

class App:
  def __init__(self):
    level = '0010'
    self.nodemap = Map('{}.csv'.format(level))
    self.run()

  def run(self):
    self.nodemap.draw()
