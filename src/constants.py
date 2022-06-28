APP_TITLE = 'Pathfinder'

NODE_PIXEL_SIZE = 67
NODE_TYPES = {
  '0': {
    'type': 'empty',
    'color': 'white',
    'walkable': True
  },
  '1': {
    'type': 'wall',
    'color': 'gray',
    'walkable': False
  },
  's': {
    'type': 'origin',
    'color': 'blue',
    'walkable': True
  },
  'e': {
    'type': 'target',
    'color': 'green',
    'walkable': True
  }
}