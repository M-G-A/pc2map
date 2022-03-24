import sys, os
import numpy as np
import open3d as o3d
import cv2

def alignData(pc,R=None):
    if R is None:
        if pc.has_normals():
            N = 90
            xy = np.asarray(pc.normals)[:,0:2].T
            ang = np.arctan2(xy[0],xy[1])%(np.pi/2) # heading angles of the normals
            alpha,b = np.histogram(ang,N,range=(0,np.pi/2)) 
            alpha = (alpha.argmax()+0.5)/N*np.pi/2 # mode of histogram
            c=np.cos(alpha)
            s=np.sin(alpha)
            R=np.array([[c,-s,0],
                        [s,c,0],
                        [0,0,1]])
        else:
            from sklearn.decomposition import PCA
            xy = np.asarray(pc.points)[:,0:2]
            pca = PCA(n_components=2)
            pca.fit_transform(xy)
            R = np.eye(3);
            R[0:2,0:2] = pca.components_
    pc.rotate(R)

def pc2map(pc, map_out=None, res=5, height=1.8):
    p = np.array(pc.points)

    # introduce variables for better readability
    XY = p[:,[0,1]]
    z = p[:,2]

    #find floor
    n,bins = np.histogram(z,50)
    floor = bins[np.argmax(n)+1]
    index = (z>floor) & (z<floor+height)

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
    
    # uncomment if you don't want to align the data
    # you can also set R to a desired value
    alignData(pc,R=None)

    # create map
    pc2map(pc,map_out)
