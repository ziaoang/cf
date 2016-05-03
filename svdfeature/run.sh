trainFile=../Autoencoders_cf/my/train.txt
testFile=../Autoencoders_cf/my/test.txt
../tool/svdfeature-1.2.2/tools/line_shuffle $trainFile train.doc2vec.shuffle
../tool/svdfeature-1.2.2/tools/make_feature_buffer train.doc2vec.shuffle train.doc2vec.shuffle.buffer
../tool/svdfeature-1.2.2/tools/make_feature_buffer $testFile test.doc2vec.buffer
../tool/svdfeature-1.2.2/svd_feature base.conf num_round=50

eval
for i in $(seq 0 50)
do
    ../tool/svdfeature-1.2.2/svd_feature_infer base.conf pred=$i name_pred=data/$i.out
done

for i in $(seq 0 50)
do
    python ../rsme.py $testFile data/$i.out 0 0 
done


