for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        trainFile=data/train-${i}.${j}.txt
        testFile=data/test-${i}.${j}.txt
        echo $trainFile
        echo $testFile

        outputFolder=data-${i}.${j}

        bufferTrainFile=${outputFolder}/train-${i}.${j}.buffer
        bufferTestFile=${outputFolder}/test-${i}.${j}.buffer
        confFile=${outputFolder}/conf-${i}.${j}.txt
    
        mkdir $outputFolder

        python genConf.py $trainFile $testFile $confFile

        ../../tool/svdfeature-1.2.2/tools/make_feature_buffer $trainFile $bufferTrainFile
        ../../tool/svdfeature-1.2.2/tools/make_feature_buffer $testFile $bufferTestFile
    
        ../../tool/svdfeature-1.2.2/svd_feature $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder num_round=50
        ../../tool/svdfeature-1.2.2/svd_feature_infer $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder

        for k in $(seq 0 50); do
            ../../tool/svdfeature-1.2.2/svd_feature_infer $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder pred=$k name_pred=${outputFolder}/out-${i}.${j}.${k}.txt
        done
    
    done
done

