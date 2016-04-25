../tool/liblinear-2.1/train -s 11 train.rc.addOne train.model
../tool/liblinear-2.1/predict test.rc.addOne train.model test.out
