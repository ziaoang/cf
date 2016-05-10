for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        rawTrainFile=../../data/my/train-${i}.${j}.txt
        rawTestFile=../../data/my/test-${i}.${j}.txt
        trainFile=data/train-${i}.${j}.txt
        testFile=data/test-${i}.${j}.txt
        python format_libmf.py $rawTrainFile $rawTestFile $trainFile $testFile
    done    
done
