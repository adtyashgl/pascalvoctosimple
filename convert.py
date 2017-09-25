import xml.etree.ElementTree
import glob 
import argparse


def convert():
    parser  = argparse.ArgumentParser()
    parser.add_argument("xml_path", help="directory where the annotation files are present")
    parser.add_argument("--image_path", help="Path of the images. If this is provided,path within the label will be changed to the provided option")
    parser.add_argument("--output_file", help="Name of the output file. If not provided, assumed to be traininfile.txt")
    parser.add_argument("--append", help="true if you want to append the results to the output file. Assumed false")
    args = parser.parse_args()
  
    outputFile = "trainingfile.txt"
    if args.output_file:
      outputFile = args.output_file 
   
    mode = "w+"
    if args.append and args.append == "true":
       mode = "a+"
        
    handle = open(outputFile,mode)
    path = args.xml_path + "/*.xml"
    print path

    for filename in glob.iglob(path):
      print filename 
      root = xml.etree.ElementTree.parse(filename).getroot()
      if args.image_path:
         image_path = args.image_path + '/' + filename 
      else:
         image_path = root.find('path').text

      for object in root.findall('object'):
        className = object.find('name').text
        xmin = object.find('bndbox').find('xmin').text
        ymin = object.find('bndbox').find('ymin').text
        xmax = object.find('bndbox').find('xmax').text
        ymax = object.find('bndbox').find('ymax').text
        textToWrite = image_path + ',' + xmin + ',' + ymin + ',' + xmax + ',' + ymax + ',' + className + '\n'
        print textToWrite
        handle.write(textToWrite) 
   
    print "Conversion available in " + outputFile
    handle.close()

if __name__ == "__main__":
   convert() 
