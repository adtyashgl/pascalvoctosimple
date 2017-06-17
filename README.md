# pascalvoctosimple
Pascal VOC style labelling (in xml) to simple format. The simple format is used by keras-frcnn to train on your own data. 

If you are using https://github.com/yhenon/keras-frcnn for training your own data, 
then I will recommend labelImg.py (https://github.com/tzutalin/labelImg) to label your testing data.

labelImg.py will create a per training data annotation file in pascal voc format (in xml)
Keras-Frcnn does support training in pascal voc data.
However, if you would like to conver the pascal voc data annotations to the "simple" format supported, then you can use this script.


Change the following in convert.py
1) IMAGE_PATH : path where all the images are available
2) SIMPLE_TRAINING_FILE: name of the simple training file

Copy the convert to the directory where all the xmls are present

Usage
convert.py

TODO: accept command line parameters
