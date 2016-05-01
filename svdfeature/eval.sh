for i in $(seq 0 50)
do
    ../tool/svdfeature-1.2.2/svd_feature_infer base.conf pred=$i name_pred=data/$i.out
done

for i in $(seq 0 50)
do
    python ../rsme.py ../doc2vec/train.doc2vec data/$i.out 0 0
done
