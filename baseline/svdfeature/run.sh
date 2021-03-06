bufferTrainFile=data/train.buffer
bufferTestFile=data/test.buffer
confFile=../../data/my/conf.txt
model_out_folder=tmp

num_round=100
num_factor=2000
learning_rate=0.005
wd_item=0.032
wd_user=0.032

../../tool/svdfeature-1.2.2/svd_feature $confFile\
                        buffer_feature=$bufferTrainFile\
                        model_out_folder=$model_out_folder\
                        num_round=$num_round\
                        num_factor=$num_factor\
                        learning_rate=$learning_rate\
                        wd_item=$wd_item\
                        wd_user=$wd_user

../../tool/svdfeature-1.2.2/svd_feature_infer $confFile\
                        test:buffer_feature=$bufferTrainFile\
                        model_out_folder=$model_out_folder

../../tool/svdfeature-1.2.2/svd_feature_infer $confFile\
                        test:buffer_feature=$bufferTestFile\
                        model_out_folder=$model_out_folder


