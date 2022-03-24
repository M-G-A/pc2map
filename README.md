# pc2map
Create a 2D map from a point cloud. The produced occupancy-map can be used by many navigation systems.

run command:

`python pc2map.py path2pointcloud path2outputMap`


### Installation of dependencies

`pip install numpy open3d opencv-python`

if your pointcloud doesn't have normals and you want to align the data anyways, you also need

`pip install scikit-learn`

