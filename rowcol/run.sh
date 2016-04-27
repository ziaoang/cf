#python rowcol.py 6040 3883 ../data/my/train.txt ../data/my/test.txt train.0.rc test.0.rc 0
#python rowcol.py 6040 3883 ../data/my/train.txt ../data/my/test.txt train.1.rc test.1.rc 1
../tool/liblinear-2.1/train -s 11 train.0.rc 0.model
../tool/liblinear-2.1/predict test.0.rc 0.model 0.out
../tool/liblinear-2.1/train -s 11 train.1.rc 1.model
../tool/liblinear-2.1/predict test.1.rc 1.model 1.out
