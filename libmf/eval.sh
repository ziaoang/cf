for i in 1 10 20; do
    testFile=data/test-${i}m.txt
    for d in 50 100 200 500; do
        resultFile=data/${i}m-${d}.out
        echo $i $d
        python ../rsme.py $resultFile $testFile 0 2
    done
done

