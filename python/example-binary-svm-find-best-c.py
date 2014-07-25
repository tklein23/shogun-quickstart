#!/usr/bin/env python2.7
#
# This software is distributed under BSD 3-clause license (see LICENSE file).
#
# Copyright (C) 2014 Thoralf Klein
#

from modshogun import RealFeatures, BinaryLabels
from modshogun import LibLinear, L2R_L2LOSS_SVC_DUAL

from numpy import random, mean

X_train = RealFeatures(random.randn(30, 100))
Y_train = BinaryLabels(random.randn(X_train.get_num_vectors()))

results = []

for C1_pow in range(-3, 1):
    for C2_pow in range(-3, 1):

        svm = LibLinear()
        svm.set_bias_enabled(False)
        svm.set_liblinear_solver_type(L2R_L2LOSS_SVC_DUAL)
        svm.set_C(10**C1_pow, 10**C2_pow)

        svm.set_features(X_train)
        svm.set_labels(Y_train)
        svm.train()

        Y_pred = svm.apply_binary(X_train)
        accuracy = mean(Y_train.get_labels() == Y_pred.get_labels())

        print 10**C1_pow, 10**C2_pow, accuracy
        results.append({"accuracy":accuracy, "svm":svm})

results.sort(key=lambda x:x["accuracy"], reverse=True)

best_svm = results[0]["svm"]
print "best machine weights:", best_svm.get_w()
print "  argmin: ", best_svm.get_w().argmin()
print "  argmax: ", best_svm.get_w().argmax()
