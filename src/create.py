#!/usr/bin/python

import os
import extras

    
input_dir='../input/1-preprocessed'
output_dir='../output'


input_images_dir=os.path.join(input_dir,'images')
input_labels_dir=os.path.join(input_dir,'labels')

for dname in os.listdir(input_images_dir):
    extras.generate(output_dir,
                    input_images_dir,
                    input_labels_dir,
                    dname,
                    separate=True,
                    height=224,
                    width=224,
                    step=16);
    
