#!/usr/bin/python

from osgeo import gdal
import numpy as np
import os

def tiff_to_bmp(archivo_tiff,output,image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp']):
    os.makedirs(output, exist_ok = True);
    
    ds = gdal.Open(archivo_tiff)

    # Obtener el número de bandas (capas)
    num_bandas = ds.RasterCount

    import imageio

    # Iterar sobre cada banda
    for i in range(1, num_bandas + 1):
        # Leer la banda actual
        banda = ds.GetRasterBand(i)
        # Convertir la banda en una matriz numpy
        matriz_banda = banda.ReadAsArray()
        
        MIN=np.min(matriz_banda)
        MAX=np.max(matriz_banda)
        
        matriz_banda_normalizada = (matriz_banda - MIN) / (MAX - MIN) * 255
        
        matriz_banda_enteros = matriz_banda_normalizada.astype(np.uint8)
        
        imageio.imwrite(os.path.join(output,image_names[i-1]),matriz_banda_enteros)

    ds = None


archivo_tiff = '../input/0-raw/bgrne_23.tiff';
output='../input/1-preprocessed/train/images/1';

tiff_to_bmp(archivo_tiff,output);

