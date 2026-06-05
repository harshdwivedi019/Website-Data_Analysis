import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
folder = "output"
for file in os.listdir(folder):
    if file.endswith(".png"):
        img = mpimg.imread(os.path.join(folder, file))
        plt.figure(figsize=(10,5))
        plt.imshow(img)
        plt.axis("off")
        plt.title(file)
        plt.show()
