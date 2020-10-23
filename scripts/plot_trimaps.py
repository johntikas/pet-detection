from PIL import Image
import matplotlib.pyplot as plt

image = Image.open('data/annotations/trimaps/miniature_pinscher_14.png')
plt.imshow(image)
plt.show()

