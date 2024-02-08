from osgeo import osr, gdal
import numpy as np
import os

def save_tiff_with_georeference(image:np.array, 
                                save_path: str, 
                                ds:gdal.Open) -> str:

    """
    Args:
        image: array of read image (shape=(-1,-1,3))
        save_path: save path for tested data
        ds: variable with geo-reference information
    """
    h,w = image.shape
    c = 1

    prj = ds.GetProjection()
    srs = osr.SpatialReference(wkt=prj)
    driver = gdal.GetDriverByName("GTiff")
    tfw = ds.GetGeoTransform() 

    outdata = driver.Create(save_path, h,w,c, gdal.GDT_Byte)
    outdata.SetGeoTransform(tfw)
    outdata.SetProjection(prj)
    outdata.GetRasterBand(1).WriteArray(image)
    outdata.FlushCache()
    outdata = None
    ds = None

def create_dir(path):
    """
    Args:
        path: path to the folder to create
    """
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        pass

def create_save_path(main_path, path):
    dir, fn = os.path.split(path)
    dir = os.path.basename(dir)
    create_dir(os.path.join(main_path,dir))
    save_path = os.path.join(main_path,dir,fn)
    return save_path