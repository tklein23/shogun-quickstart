#!/usr/bin/env python2.7
#
# This software is distributed under BSD 3-clause license (see LICENSE file).
#
# Copyright (C) 2014 Thoralf Klein
#

from modshogun import RealFeatures, BinaryLabels, LibLinear
from numpy import random, mean

X_train = RealFeatures(random.randn(30, 100))
Y_train = BinaryLabels(random.randn(X_train.get_num_vectors()))

svm = LibLinear(1.0, X_train, Y_train)
svm.train()

Y_pred = svm.apply_binary(X_train)
Y_train.get_labels() == Y_pred.get_labels()

print "accuracy:", mean(Y_train.get_labels() == Y_pred.get_labels())
