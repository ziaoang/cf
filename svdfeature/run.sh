#for i in 1 10 20; do
for i in 20; do

    trainFile=../pipeline/data/train-${i}m.d2v.svd
    testFile=../pipeline/data/test-${i}m.d2v.svd

    outputFolder=data-${i}m

    bufferTrainFile=${outputFolder}/train-${i}m.buffer
    bufferTestFile=${outputFolder}/test-${i}m.buffer
    confFile=${outputFolder}/conf-${i}m.txt
    
    mkdir $outputFolder

    python genConf.py $trainFile $testFile $confFile

    ../tool/svdfeature-1.2.2/tools/make_feature_buffer $trainFile $bufferTrainFile
    ../tool/svdfeature-1.2.2/tools/make_feature_buffer $testFile $bufferTestFile
    ../tool/svdfeature-1.2.2/svd_feature $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder num_round=50

    for j in $(seq 0 50); do
        ../tool/svdfeature-1.2.2/svd_feature_infer $confFile buffer_feature=$bufferTrainFile test:buffer_feature=$bufferTestFile model_out_folder=$outputFolder pred=$j name_pred=${outputFolder}/${j}.out
    done
    
    for j in $(seq 0 50); do
        python ../rsme.py $testFile ${outputFolder}/${j}.out 0 0 
    done

done

