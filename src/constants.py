APP_TITLE = 'Pathfinder'

NODE_PIXEL_SIZE = 67
COLORS = {
  'white': '#FFFFFF',
  'gray': '#747E7E',
  'bluegray': '#3F7C85',
  'red': '#FF5F5D',
  'path': '#72F2EB'
}
NODE_TYPES = {
  '0': {
    'type': 'empty',
    'color': COLORS['white'],
    'walkable': True
  },
  '1': {
    'type': 'wall',
    'color': COLORS['gray'],
    'walkable': False
  },
  's': {
    'type': 'start',
    'color': COLORS['bluegray'],
    'walkable': True
  },
  'e': {
    'type': 'end',
    'color': COLORS['red'],
    'walkable': True
  }
}