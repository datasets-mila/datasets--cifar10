#!/bin/bash

python scripts/preprocess_torchvision.py
# Delete raw files
rm cifar-10-python.tar.gz md5sums

