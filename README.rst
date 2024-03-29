####################
The CIFAR-10 dataset
####################

`<https://www.cs.toronto.edu/~kriz/cifar.html>`_

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with
6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with
10000 images. The test batch contains exactly 1000 randomly-selected images
from each class. The training batches contain the remaining images in random
order, but some training batches may contain more images from one class than
another. Between them, the training batches contain exactly 5000 images from
each class.

The classes are completely mutually exclusive. There is no overlap between
automobiles and trucks. "Automobile" includes sedans, SUVs, things of that
sort. "Truck" includes only big trucks. Neither includes pickup trucks.

********
Download
********

If you're going to use this dataset, please cite the tech report at the bottom
of this page.

+-----------------------------+--------+-----------------------------+
| Version                     | Size   | md5sum                      |
+-----------------------------+--------+-----------------------------+
| `CIFAR-10 python            | 163 MB | c58f3                       |
| version                     |        | 0108f718f92721af3b95e74349a |
| <cifar-10-python.tar.gz>`__ |        |                             |
+-----------------------------+--------+-----------------------------+
| `CIFAR-10 Matlab            | 175 MB | 70270                       |
| version                     |        | af85842c9e89bb428ec9976c926 |
| <cifar-10-matlab.tar.gz>`__ |        |                             |
+-----------------------------+--------+-----------------------------+
| `CIFAR-10 binary version    | 162 MB | c32a1                       |
| (suitable for C             |        | d4ab5d03f1284b67883e8d87530 |
| programs)                   |        |                             |
| <cifar-10-binary.tar.gz>`__ |        |                             |
+-----------------------------+--------+-----------------------------+

****************
Baseline results
****************

You can find some baseline replicable results on this dataset `on the project
page for cuda-convnet <http://code.google.com/p/cuda-convnet/>`__. These
results were obtained with a convolutional neural network. Briefly, they are
18% test error without data augmentation and 11% with. Additionally, `Jasper
Snoek <http://www.cs.toronto.edu/~jasper/>`__ has a `new paper
<http://hips.seas.harvard.edu/content/practical-bayesian-optimization-machine-learning-algorithms>`__
in which he used Bayesian hyperparameter optimization to find nice settings of
the weight decay and other hyperparameters, which allowed him to obtain a test
error rate of 15% (without data augmentation) using the architecture of the net
that got 18%.

*************
Other results
*************

`Rodrigo Benenson <http://rodrigob.github.com/>`__ has been kind enough to
collect results on CIFAR-10/100 and other datasets on his website; `click here
<http://rodrigob.github.com/are_we_there_yet/build/classification_datasets_results.html>`__
to view.

**************
Dataset layout
**************

Python / Matlab versions
========================

I will describe the layout of the Python version of the dataset. The layout of
the Matlab version is identical.

The archive contains the files data_batch_1, data_batch_2, ..., data_batch_5,
as well as test_batch. Each of these files is a Python "pickled" object
produced with `cPickle
<http://www.python.org/doc/2.5/lib/module-cPickle.html>`__.  Here is a python2
routine which will open such a file and return a dictionary:

.. code:: code

   def unpickle(file):
       import cPickle
       with open(file, 'rb') as fo:
           dict = cPickle.load(fo)
       return dict

And a python3 version:

.. code:: code

   def unpickle(file):
       import pickle
       with open(file, 'rb') as fo:
           dict = pickle.load(fo, encoding='bytes')
       return dict

Loaded in this way, each of the batch files contains a dictionary with
the following elements:

-  **data** -- a 10000x3072 `numpy <http://numpy.scipy.org/>`__ array of
   uint8s. Each row of the array stores a 32x32 colour image. The first 1024
   entries contain the red channel values, the next 1024 the green, and the
   final 1024 the blue. The image is stored in row-major order, so that the
   first 32 entries of the array are the red channel values of the first row of
   the image.
-  **labels** -- a list of 10000 numbers in the range 0-9. The number at index
   *i* indicates the label of the *i*\ th image in the array **data**.

The dataset contains another file, called batches.meta. It too contains a
Python dictionary object. It has the following entries:

-  **label_names** -- a 10-element list which gives meaningful names to the
   numeric labels in the **labels** array described above. For example,
   label_names[0] == "airplane", label_names[1] == "automobile", etc.

Binary version
==============

The binary version contains the files data_batch_1.bin, data_batch_2.bin, ...,
data_batch_5.bin, as well as test_batch.bin. Each of these files is formatted
as follows:

.. code:: code

   <1 x label><3072 x pixel>
   ...
   <1 x label><3072 x pixel>

In other words, the first byte is the label of the first image, which is a
number in the range 0-9. The next 3072 bytes are the values of the pixels of
the image. The first 1024 bytes are the red channel values, the next 1024 the
green, and the final 1024 the blue. The values are stored in row-major order,
so the first 32 bytes are the red channel values of the first row of the image.

Each file contains 10000 such 3073-byte "rows" of images, although there is
**nothing delimiting the rows**. Therefore each file should be exactly 30730000
bytes long.

There is another file, called batches.meta.txt. This is an ASCII file that maps
numeric labels in the range 0-9 to meaningful class names.  It is merely a list
of the 10 class names, one per row. The class name on row *i* corresponds to
numeric label *i*.

*********
Reference
*********

This tech report (Chapter 3) describes the dataset and the methodology followed
when collecting it in much greater detail. Please cite it if you intend to use
this dataset.

-  `Learning Multiple Layers of Features from Tiny Images
   <learning-features-2009-TR.pdf>`__, Alex Krizhevsky, 2009.
