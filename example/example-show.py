import numpy as np

#imagem = np.load('../output/train/images/1_0_320.npy')
imagem = np.load('../output/train/labels/1_0_320_bushes.npy')
#imagem = np.load('../output/train/labels/1_16_176_map.npy')


import cv2
cv2.imshow('Imagem RGB', imagem[:,:,0:3])
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
import matplotlib.pyplot as plt
plt.imshow(imagem)
plt.axis('off')  # Desativa os eixos
plt.show()
'''
