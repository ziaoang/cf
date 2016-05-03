for i in 1 10 20; do
    echo $i
    rawTrainFile=../data/my/train-${i}m.txt
    rawTestFile=../data/my/test-${i}m.txt
    trainFile=data/train-${i}m.txt
    testFile=data/test-${i}m.txt
    
    python format_libmf.py $rawTrainFile $rawTestFile $trainFile $testFile

    for d in 50 100 200 500; do
        modelFile=data/${i}m-${d}.model
        resultFile=data/${i}m-${d}.out
        ../tool/libmf-2.01/mf-train -k ${d} -t 1000 $trainFile $modelFile
        ../tool/libmf-2.01/mf-predict $testFile $modelFile $resultFile
    done
done

