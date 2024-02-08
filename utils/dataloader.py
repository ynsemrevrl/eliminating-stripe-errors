from osgeo import osr, gdal

import numpy as np
import tifffile
import os

class DataLoader():
    
    def __init__(
            self, 
            images_dir,
            ):
        self.idxs = os.listdir(images_dir)
        self.images = [os.path.join(images_dir, image_idx) for image_idx in self.idxs]

    def __getitem__(self, idx):
        
        # read data
        image = (np.expand_dims(tifffile.imread(self.images[idx]),axis=0) - 127.5) / 127.5
        ds = gdal.Open(self.images[idx])
        fn = os.path.basename(self.images[idx])
        return image, ds, fn
        
    def __len__(self):
        return len(self.idxs)