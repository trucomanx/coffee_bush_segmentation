import os
import cv2
import numpy as np

def iterar_roi_idx(H, W, h, w, s):
    for i in range(0, H - h + 1, s):
        for j in range(0, W - w + 1, s):
            yield i, j # matriz[i:i+h, j:j+w]

def get_block_method_roi(image_list,i,j,height,width):
    img_list=[];
    for image in image_list:
        img_list.append(image[i:i+height,j:j+width]);
    img_block = np.stack(img_list, axis=-1);
    return img_block;

def generate_from_image(output_dir,
                        dname,
                        image_list,
                        out_label_list,
                        height,
                        width,
                        step,
                        images_dname='images',
                        labels_dname='labels'
                        ):
    H, W = image_list[0].shape;
    
    ## Create directories
    os.makedirs(os.path.join(output_dir,images_dname),exist_ok=True);
    os.makedirs(os.path.join(output_dir,labels_dname),exist_ok=True);
    
    frel_img_list=[];
    frel_lbl_list = [[] for _ in range(len(out_label_list))]
    for i, j in iterar_roi_idx(H, W, height, width, step):
        
        commom_name='_'+str(i)+'_'+str(j);
        
        ## Generate img_block
        img_block = get_block_method_roi(image_list,i,j,height,width);
        
        frel_img=os.path.join(images_dname,dname+commom_name+'.npy');
        np.save(os.path.join(output_dir,frel_img),img_block);
        frel_img_list.append(frel_img);
        
        for n in range(len(out_label_list)):
            ## Generate label_block
            lbl_block = get_block_method_roi(out_label_list[n],i,j,height,width);
            
            frel_lbl=os.path.join(labels_dname,dname+commom_name+'_lbl'+str(n)+'.npy');
            np.save(os.path.join(output_dir,frel_lbl),lbl_block);
            frel_lbl_list[n].append(frel_lbl);
    
    return frel_img_list,frel_lbl_list;
    
def generate(   output_dir,
                input_images_dir,
                input_labels_dir,
                dname,
                image_names=['Red.bmp','Green.bmp','Blue.bmp','Nir.bmp','RedEdge.bmp'],
                label_names=['label.bmp','map.bmp'],
                separate=True,
                height=224, # height
                width=224,  # width
                step=16     # step
                ):
    
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
    
    generate_from_image(output_dir,dname,image_list,out_label_list,height,width,step);
