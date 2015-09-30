# Calibration file to Meshlab scene converter

This is a simple python script which transforms a file with camera calibration parameters (intrinsic, rotation and position) into a Meshlab scene an the other way around.

## calib2meshlab

Parameters:

1. 3D mesh file name
2. File with calibration parameteres as in the sample file provided
3. File with the list of images names used for texturing
4. Name of the output Meshlab scene file

## meshlab2calib

Parameters:

1. Meshlab scene input file
2. Output camera calibration file
3. Output image list

## Calibration file format

The calibration file presents the following format:
- first line is just the number of cameras in the scene
- Every other line includes the calibration parameters of each camera following:

```
[ Intrinsic parameters (row1 row2 row3) ] [ Rotation matrix (row1 row2 row3) ] [ Camera position ] [ Image dimensions ]
```

