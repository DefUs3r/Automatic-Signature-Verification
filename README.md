Automatic Signature Stability Analysis And Verification Using Local Features
============================================================================

This repository contains the Python implementation of [Automatic Signature Stability Analysis And Verification Using Local Features](https://ieeexplore.ieee.org/document/6981088/) by Muhammad Imran Malik, Marcus Liwicki, Andreas Dengel, Seiichi Uchida, Volkmar Frinken published in 2014 at 14th International Conference on Frontiers in Handwriting Recognition:
```
@inproceedings{inproceedings,
author = {Malik, Muhammad Imran and Liwicki, Marcus and Dengel, Andreas and Uchida, Seiichi and Frinken, Volkmar},
year = {2014},
month = {09},
pages = {621-626},
title = {Automatic Signature Stability Analysis and Verification Using Local Features},
volume = {2014},
journal = {Proceedings of International Conference on Frontiers in Handwriting Recognition, ICFHR},
doi = {10.1109/ICFHR.2014.109}
}
```
In addition to this we performed some experiments on using custom hand-crafted features of images to train simple classifiers to recognise a Genuine or Forged Signature in a database.

Also additionally we have implemented a Keras-Tensorflow implementation of [SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification]() by Sounak Dey, Anjan Dutta, J. Ignacio Toledo, Suman K.Ghosh, Josep Llados, Umapada Pal published in Pattern Recognition Letters

```
@article{article,
author = {Dey, Sounak and Dutta, Anjan and Toledo, J. and Ghosh, Suman and Lladós, Josep and Pal, Umapada},
year = {2017},
month = {07},
pages = {},
title = {SigNet: Convolutional Siamese Network for Writer Independent Offline Signature Verification}
}
```
- Note : The paper linked here is from IEEEExplore. Make sure you have a valid subscription.

Dependencies
------------

The following libraries are needed:

:heavy_check_mark: OpenCV 

In pip3, you can install with: `pip3 install opencv-contrib-python==3.4.2.16`

:heavy_check_mark: Tensorflow-GPU and Keras

In pip3 you can use : `pip3 install tensorflow-gpu keras`

:rotating_light: (Proceed with caution) Ensure that you have a CUDA enabled GPU (the more, the merrier :stuck_out_tongue_winking_eye:) 

Please check dependencies and proceed.

:heavy_check_mark: Python 3.6

:heavy_check_mark: Python packages (newer packages will likely work, though these are the exact versions that we used):
```
      Pillow==6.2.1
      numpy==1.17.3
      scipy==1.3.2
      scikit-image==0.15.0
      scikit-learn==0.21.3
      ImageHash==4.0.0
 ```     
:heavy_check_mark: 
 
 Setting up a virtual environment like `virtualenv`  will help keep your Python environment safe. We recommend installing all dependencies using this.
 
Codes
-----

`Kernel Based Classifier.ipynb` : Contains experiments using PHash, aspect ratio, (convex hull area/ bounding box area), (contour area /bounding box area) as features and lineraly stacking them and sending them to standard Classifiers like SVMs, Decision Trees etc.

`CNN_BHSig260.ipynb`            : Contains experiments on using a vanilla CNN for learning to classify genuine and forged signatures end-to-end

`Siamese_BHSig260.ipynb`        : The Implementation of SigNet, a revolutionary siamese architecture using CNNs to learn to differentiate between genuine and forged signatures on BHSig260 dataset.

`Siamese_CEDAR.ipynb`           : The Implementation of SigNet, a revolutionary siamese architecture using CNNs to learn to differentiate between genuine and forged signatures on CEDAR dataset.

We have included visualisations of what the models are learning by plotting Activations. Feel free to enlighten us beyond out intuitions :smiley:

Running
-------

:heavy_check_mark: Please install the BHSig260 and CEDAR dataset from the following links:
`BHSig260`  : [link](https://goo.gl/9QfByd)

`CEDAR`     : [link](http://cedar.buffalo.edu/NIJ/data/signatures)

Download both datasets manually or using `wget` and extract from compressed version.
Run the scripts `CEDAR_Modif.py` & `modifyBHSig260.py` to prepare datasets in the correct format.

GPU Usage and Recommended Compute
---------------------------------

For training the deep learning models, we have used 4 Nvidia GeForce GTX 1080 Ti GPU with 10 GiB memory with Intel Xeon E5-2640 v4 processors having 40 cores giving 128 GB of 2400MT/s DDR4 ECC RAM. It is recommended to use around this level of compute capability, though the CNN architecture has been tested on an Intel i7-6700HQ CPU @2.60Ghz and Nvidia GeForce GTX 960M giving 640 CUDA cores.

Some results from the Siamese Network Implementation
----------------------------------------------------
:heavy_check_mark: On a bengali signature:
![Bengali](https://github.com/DefUs3r/Automatic-Signature-Stability-Analysis/blob/master/Results/beng.png)

:heavy_check_mark: On a hindi signature:
![Hindi](https://github.com/DefUs3r/Automatic-Signature-Stability-Analysis/blob/master/Results/hin.png)

:heavy_check_mark: On an English Signature:
![English](https://github.com/DefUs3r/Automatic-Signature-Stability-Analysis/blob/master/Results/eng.png)

Adding Issues
-------------

We welcome people to try our code and suggest improvements. The way to grow is to `share and learn` :smiley:
