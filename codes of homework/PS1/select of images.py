import numpy as np
from PIL import Image
im = Image.open('character.jpg')
im = np.array(im)
print(im.shape)


