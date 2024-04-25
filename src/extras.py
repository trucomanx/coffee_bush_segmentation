import os
import cv2
import numpy as np


def generate(   input_images_dir,
                input_labels_dir,
                dname,
                image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
                label_names=['label.bmp','map.bmp'],
                separate=True):
    
    image_dir=os.path.join(input_images_dir,dname);
    label_dir=os.path.join(input_labels_dir,dname);
    
    ## Loading images
    image_list=[];
    for img_name in image_names:
        img_path=os.path.join(image_dir,img_name);
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise TypeError("Problem loading file: "+img_path);
        image_list.append(img);
    
    ## Loading output labels
    out_label_list=[];
    if separate:
        for lbl_name in label_names:
            lbl_path=os.path.join(label_dir,lbl_name);
            img = cv2.imread(lbl_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                raise TypeError("Problem loading file: "+img_path);
            out_label_list.append([img]);
    else:
        label_list=[];
        for lbl_name in label_names:
            lbl_path=os.path.join(label_dir,lbl_name);
            img = cv2.imread(lbl_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                raise TypeError("Problem loading file: "+img_path);
            label_list.append(img);
        out_label_list.append(label_list)
    
    
    #image_list,out_label_list
