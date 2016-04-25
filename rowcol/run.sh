../tool/liblinear-2.1/train -s 11 train.rc 1.model
../tool/liblinear-2.1/predict test.rc 1.model 1.out
../tool/liblinear-2.1/train -s 11 train.rc2 2.model
../tool/liblinear-2.1/predict test.rc2 2.model 2.out
