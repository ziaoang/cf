#for i in 1 10 20; do
#    for j in $(seq 1 5); do
#        rawTrainFile=../../data/my/train-${i}m.${j}.txt
#        rawTestFile=../../data/my/test-${i}m.${j}.txt
#        trainFile=data/train-${i}m.${j}.txt
#        testFile=data/test-${i}m.${j}.txt
#        
#        python format_libmf.py $rawTrainFile $rawTestFile $trainFile $testFile
#        
#        modelFile=data/${i}m.${j}.model
#        resultFile=data/${i}m.${j}.out
#        ../../tool/libmf-2.01/mf-train -k 100 -t 1000 $trainFile $modelFile
#        ../../tool/libmf-2.01/mf-predict $testFile $modelFile $resultFile
#    done    
#done

for k in $(seq 1 5); do
    rawTrainFile=../../data/my/train-net.${k}.txt
    rawTestFile=../../data/my/test-net.${k}.txt
    trainFile=data/train-net.${k}.txt
    testFile=data/test-net.${k}.txt
        
    python format_libmf.py $rawTrainFile $rawTestFile $trainFile $testFile
        
    modelFile=data/net.${k}.model
    resultFile=data/net.${k}.out
    ../../tool/libmf-2.01/mf-train -k 100 -t 1000 $trainFile $modelFile
    ../../tool/libmf-2.01/mf-predict $testFile $modelFile $resultFile
done

