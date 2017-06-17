import xml.etree.ElementTree
import glob 
IMAGE_PATH='/home/ubuntu/keras-frcnn/training_13_06/images'
SIMPLE_TRAINING_FILE = 'trainingfile.txt'

f=open(SIMPLE_TRAINING_FILE,"w+")

for filename in glob.iglob('*.xml'):
  root = xml.etree.ElementTree.parse(filename).getroot()
  for object in root.findall('object'):
     textToWrite = IMAGE_PATH + '/' + filename 
     className = object.find('name').text
     xmin = object.find('bndbox').find('xmin').text
     ymin = object.find('bndbox').find('ymin').text
     xmax = object.find('bndbox').find('xmax').text
     ymax = object.find('bndbox').find('ymax').text
     textToWrite +=',' + xmin + ',' + ymin + ',' + xmax + ',' + ymax + ',' + className + '\n'
     f.write(textToWrite) 
