for i in 1 10 20; do
    for j in $(seq 1 5); do
        rawTrainFile=../../data/my/train-${i}m.${j}.txt
        rawTestFile=../../data/my/test-${i}m.${j}.txt
        trainFile=data/train-${i}m.${j}.txt
        testFile=data/test-${i}m.${j}.txt
        
        python format_libmf.py $rawTrainFile $rawTestFile $trainFile $testFile
        
        modelFile=data/${i}m.${j}.model
        resultFile=data/${i}m.${j}.out
        ../../tool/libmf-2.01/mf-train -k 100 -t 1000 $trainFile $modelFile
        ../../tool/libmf-2.01/mf-predict $testFile $modelFile $resultFile
    done    
done

