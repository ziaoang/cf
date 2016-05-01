../tool/svdfeature-1.2.2/tools/line_shuffle ../doc2vec/train.doc2vec train.doc2vec.shuffle
../tool/svdfeature-1.2.2/tools/make_feature_buffer train.doc2vec.shuffle train.doc2vec.shuffle.buffer
../tool/svdfeature-1.2.2/tools/make_feature_buffer ../doc2vec/test.doc2vec test.doc2vec.buffer
../tool/svdfeature-1.2.2/svd_feature base.conf num_round=50

