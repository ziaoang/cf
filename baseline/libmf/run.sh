for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        trainFile=data/train-${i}.${j}.txt
        testFile=data/test-${i}.${j}.txt
        modelFile=data/${i}.${j}.model
        resultFile=data/${i}.${j}.out
        ../../tool/libmf-2.01/mf-train -k 100 -t 1000 $trainFile $modelFile
        ../../tool/libmf-2.01/mf-predict $testFile $modelFile $resultFile
    done    
done

