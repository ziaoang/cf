#../tool/libmf-2.01/mf-train -k 700 -t 1000 ../data/my/train.txt 1.model
../tool/libmf-2.01/mf-train -k 100 -t 1000 ../data/my/train.txt 1.model
../tool/libmf-2.01/mf-predict ../data/my/test.txt 1.model 1.out
