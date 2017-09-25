import xml.etree.ElementTree
import glob 
import argparse


def convert():
    parser  = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path of the images")
    parser.add_argument("--output_file", help="Name of the output file. If not provided, assumed to be traininfile.txt")
    args = parser.parse_args()
  
    outputFile = "trainingfile.txt"
    if args.output_file:
      outputFile = args.output_file 
    
    handle = open(outputFile,"w+")

   
    for filename in glob.iglob('*.xml'):
      root = xml.etree.ElementTree.parse(filename).getroot()
      for object in root.findall('object'):
        textToWrite = args.image_path + '/' + filename 
        className = object.find('name').text
        xmin = object.find('bndbox').find('xmin').text
        ymin = object.find('bndbox').find('ymin').text
        xmax = object.find('bndbox').find('xmax').text
        ymax = object.find('bndbox').find('ymax').text
        textToWrite +=',' + xmin + ',' + ymin + ',' + xmax + ',' + ymax + ',' + className + '\n'
        handle.write(textToWrite) 
   
    print "Conversion available in " + outputFile
    handle.close()

if __name__ == "__main__":
   convert() 
