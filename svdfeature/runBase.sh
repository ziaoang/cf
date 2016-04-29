#python formatBase.py ../data/my/train.txt ../data/my/test.txt train.base test.base

../tool/svdfeature-1.2.2/tools/line_shuffle train.base train.base.shuffle
../tool/svdfeature-1.2.2/tools/make_feature_buffer train.base.shuffle train.base.shuffle.buffer
../tool/svdfeature-1.2.2/tools/make_feature_buffer test.base test.base.buffer

../tool/svdfeature-1.2.2/svd_feature base.conf num_round=50

for i in $(seq 0 50)
do
    ../tool/svdfeature-1.2.2/svd_feature_infer base.conf pred=$i name_pred=base/base$i.out
done


for i in $(seq 0 50)
do
    python ../rsme.py test.base base/base$i.out 0 0
done
