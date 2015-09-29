import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 4:
  print "Wrong number of input parameter!"
  print "Usage: " + sys.argv[0] + " <MeshLabSceneFile.mlp> <OutputCalibrationFileName> <OutputImageListFileName>"
  exit()

# Reading input parameters
inFile = ET.parse(sys.argv[1])
outCalibName = sys.argv[2]
outImageListName = sys.argv[3]

outCalibFile = open(outCalibName, "w")
outImageListFile = open(outImageListName, "w")


imageNum = 0
allMatrices = []
allImages = []

root = inFile.getroot()

for raster in root.iter('MLRaster'):

	imageNum = imageNum + 1
	camera = raster.find('VCGCamera')

	camMatrices = []

	# Translation vector
	translationVector = camera.attrib['TranslationVector']
	camMatrices.append(translationVector)

	# Distortion
	distortion = camera.attrib['LensDistortion']
	camMatrices.append(distortion)

	# ViewPort
	size = camera.attrib['ViewportPx']
	camMatrices.append(size)

	# PixelSize
	pixsize = camera.attrib['PixelSizeMm']
	camMatrices.append(pixsize)

	# CenterPx
	centerpix = camera.attrib['CenterPx']
	camMatrices.append(centerpix)

	# Focal lenght
	focal = camera.attrib['FocalMm']
	camMatrices.append(focal)

	# Rotation matrix
	rotation = camera.attrib['RotationMatrix']
	camMatrices.append(rotation)

	allMatrices.append(camMatrices)

	image = raster.find('Plane')
	thisImage = image.attrib['fileName']
	allImages.append(thisImage)



# Now output files are written

outCalibFile.write("%d\n" % (imageNum))

for i in range(0,imageNum):
	# current image is written to the image list
	outImageListFile.write(allImages[i] + "\n")

 	currentCam = allMatrices[i]

 	# To obtain the correct value for the focal lenght
 	# we also need the pixel sizes
 	focal = float(currentCam[5])
 	pixsize = currentCam[3].split()
 	focalX = focal / float(pixsize[0])
 	focalY = focal / float(pixsize[1])

 	# Image Dimensions
 	imsize = currentCam[2].split()
 	imWidth = int(imsize[0])
 	imHeight = int(imsize[1])

 	# Pixel Center
 	pixcenter = currentCam[4].split()
 	pixCenterX = int(pixcenter[0])
 	pixcenterY = imHeight - int(pixcenter[1])

 	# Rotation
 	rotation = currentCam[6].split()
 	extrinsic = []
 	for i in range(0, len(rotation)):
 		extrinsic.append(float(rotation[i]))

 	# Position
 	position = []
 	translationVector = camMatrices[0].split()
 	for i in range(0,3):
 		position.append(float(translationVector[i]))

 	# current camera parameters
	outCalibFile.write("%.7e 0 %d 0 %.7e %d 0 0 1 %.7e %.7e %.7e %.7e %.7e %.7e %.7e %.7e %.7e %.7e %.7e %.7e %d %d\n" % 
		(focalX, pixCenterX, focalY, pixcenterY, extrinsic[0], extrinsic[1], extrinsic[2], -extrinsic[4], -extrinsic[5], -extrinsic[6], -extrinsic[8], -extrinsic[9], -extrinsic[10], -position[0], -position[1], -position[2], imWidth, imHeight))


outCalibFile.close()
outImageListFile.close()

