import sys, os
import numpy as np
import open3d as o3d
import cv2

def pc2map(pc, map_out=None, res=5, height=1.8):
    p = np.array(pc.points)

    # introduce variables for better readability
    XY = p[:,[0,1]]
    z = p[:,2]

    #find floor
    n,bins = np.histogram(z,50)
    floor = bins[np.argmax(n)+1]
    index = (z>floor) & (z<height)

    # remove Rotation
    ## TODO: use histogram of normals (if existing) 
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca.fit(XY[~index,:])
    XY = pca.transform(XY)

    # quantize and scale xy of points
    xy = XY*100.0/res
    xy = xy - np.min(xy,axis=0)
    xy = xy.astype(int)

    # create map
    mapp = np.zeros((np.max(xy,axis=0)+[1,1]).tolist()+[4])
    temp = xy[~index]
    mapp[temp[:,0],temp[:,1]] = [255,255,255,255]
    temp = xy[index]
    mapp[temp[:,0],temp[:,1]] = [0,0,0,255]

    # write map
    if map_out:
        cv2.imwrite(map_out, mapp)

    return map_out

if __name__ == "__main__":
    pc_path = sys.argv[1]
    map_out = sys.argv[2]
    #res = sys.argv[3]
    #height = sys.argv[4]

    # read pc
    pc = o3d.io.read_point_cloud(pc_path)

    # create map
    pc2map(pc,map_out)


