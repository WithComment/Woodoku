from __future__ import annotations

import numpy as np


def int8_array(*args, **kwargs) -> np.ndarray:
  return np.asarray(*args, dtype=np.int8, **kwargs)


def print_shape(shape: np.ndarray) -> None:
  output = []
  for row in shape:
    for cell in row:
      if cell:
        output.append(u'\u2588\u2588')
      else:
        output.append('  ')
    output.append('\n')
  print(''.join(output))

# O
O_1 = int8_array([[1]])

# O O
# O O
O_2 = int8_array([
  [1, 1], 
  [1, 1]
])

# O
# O O
L_2 = int8_array([
  [1, 0],
  [1, 1]
])

# O
# O
# O O O
L_3 = int8_array([
  [1, 0, 0],
  [1, 0, 0],
  [1, 1, 1]
])

# O O O
#   O
T_2 = int8_array([
  [1, 1, 1],
  [0, 1, 0]
])

# O O O
#   O
#   O
T_3 = int8_array([
  [1, 1, 1],
  [0, 1, 0],
  [0, 1, 0]
])

I_2 = int8_array([
  [1, 1]
]).T

I_3 = int8_array([
  [1, 1, 1]
]).T

I_4 = int8_array([
  [1, 1, 1, 1]
]).T

I_5 = int8_array([
  [1, 1, 1, 1, 1]
]).T

D_2 = np.diag([1] * 2)
D_3 = np.diag([1] * 3)
D_4 = np.diag([1] * 4)

# O O
# O
# O O
C = int8_array([
  [1, 1],
  [1, 0],
  [1, 1]
])

# O O
#   O O
Z = int8_array([
  [1, 1, 0],
  [0, 1, 1]
])

#   O O
# O O
S = int8_array([
  [0, 1, 1],
  [1, 1, 0]
])

shapes = [O_1, O_2]
rotate_2 = [I_2, I_3, I_4, I_5, D_2, D_3, D_4, Z, S]
rotate_4 = [L_2, L_3, T_2, T_3, C]

for shape in rotate_2:
  for i in range(2):
    shape = np.rot90(shape)
    shapes.append(shape)

for shape in rotate_4:
  for i in range(4):
    shape = np.rot90(shape)
    shapes.append(shape)

if __name__ == '__main__':
  for shape in shapes:
    print_shape(shape)
