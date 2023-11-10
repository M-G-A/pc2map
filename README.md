# pc2map
Create a 2D map from a point cloud. The produced occupancy-map can be used by many navigation systems.

run command:

`python pc2map.py path2pointcloud path2outputMap`


### Installation of dependencies

`pip install numpy open3d opencv-python`

if your pointcloud doesn't have normals and you want to align the data anyways, you also need

`pip install scikit-learn`

# Paper
If you use this code please cite following [Paper](https://ieeexplore.ieee.org/document/10260595)
```
@INPROCEEDINGS{10260595,
  author={Adam, Michael G. and Piccolrovazzi, Martin and Dalloul, Ahmed and Werner, Christian and Steinbach, Eckehard},
  booktitle={2023 IEEE 19th International Conference on Automation Science and Engineering (CASE)}, 
  title={Continuous and Autonomous Digital Twinning of Large-Scale Dynamic Indoor Environments}, 
  year={2023},
  volume={},
  number={},
  pages={1-6},
  doi={10.1109/CASE56687.2023.10260595}}



# Acknowledgement
This work is funded by Germany’s Federal Ministry of Education and Research within the project KIMaps (grant ID #01IS20031C).
