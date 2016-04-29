#python formatMf.py ../data/my/train.txt ../data/my/test.txt train.mf test.mf
#../tool/svdfeature-1.2.2/tools/line_shuffle train.mf train.mf.shuffle
#../tool/svdfeature-1.2.2/tools/make_feature_buffer train.mf.shuffle train.mf.shuffle.buffer
#../tool/svdfeature-1.2.2/tools/make_feature_buffer test.mf test.mf.buffer

../tool/svdfeature-1.2.2/svd_feature mf.conf num_round=10
../tool/svdfeature-1.2.2/svd_feature_infer mf.conf pred=10


