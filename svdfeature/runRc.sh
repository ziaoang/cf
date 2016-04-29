python formatRc.py ../data/my/train.txt ../data/my/test.txt train.rc test.rc
../tool/svdfeature-1.2.2/tools/line_shuffle train.rc train.rc.shuffle
../tool/svdfeature-1.2.2/tools/make_feature_buffer train.rc.shuffle train.rc.shuffle.buffer
../tool/svdfeature-1.2.2/tools/make_feature_buffer test.rc test.rc.buffer

../tool/svdfeature-1.2.2/svd_feature rc.conf num_round=10
../tool/svdfeature-1.2.2/svd_feature_infer rc.conf pred=10


