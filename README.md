# pascalvoctosimple
Pascal VOC style labelling (in xml) to simple format. The simple format is used by keras-frcnn to train on your own data. 

If you are using https://github.com/yhenon/keras-frcnn for training your own data, 
then I will recommend labelImg.py (https://github.com/tzutalin/labelImg) to label your testing data.

labelImg.py will create a per training data annotation file in pascal voc format (in xml)
Keras-Frcnn does support training in pascal voc data.
However, if you would like to conver the pascal voc data annotations to the "simple" format supported, then you can use this script.

Usage
convert.py xml_path 
Arguments accepted 
xml_path : path where the annotation files are present (xml)
--image_path: Path of the images. If this is provided,path within the label will be changed to the provided option. 
--output_file: Name of the output file. If not provided, assumed to be traininfile.txt


