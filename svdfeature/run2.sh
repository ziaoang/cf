for i in 1 10 20; do

    trainFile=data/train-${i}m.txt
    testFile=data/test-${i}m.txt
    bufferTrainFile=data/train-${i}m.buffer
    bufferTestFile=data/test-${i}m.buffer
    confFile=data/conf-${i}m.txt
    outputFolder=tmp${i}m

    ../tool/svdfeature-1.2.2/tools/make_feature_buffer $trainFile $bufferTrainFile
    ../tool/svdfeature-1.2.2/tools/make_feature_buffer $testFile $bufferTestFile
    mkdir $outputFolder
    ../tool/svdfeature-1.2.2/svd_feature $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder num_round=50

    for j in $(seq 0 50); do
        ../tool/svdfeature-1.2.2/svd_feature_infer $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder pred=$j name_pred=${outputFolder}/${j}.out
    done
    
    for j in $(seq 0 50); do
        python ../rsme.py $testFile ${outputFolder}/${j}.out 0 0 
    done

done

