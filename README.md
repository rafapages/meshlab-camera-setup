# Calibration file to Meshlab scene converter

This is a simple python script which transforms a file with camera calibration parameters (intrinsic, extrinsic and position) into a Meshlab scene an the other way around.

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

