import numpy as np

image = np.random.randint(0,256, (5,5))
bright = image + 30
bright = np.clip(bright, 0, 255)
avg_bright = np.mean(bright)
print("original Image:\n", image)
print("Brightened image: \n", bright)
print("Avg brightness: \n", avg_bright)
