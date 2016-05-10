for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        trainFile=data/train-${i}.${j}.libfm
        testFile=data/test-${i}.${j}.libfm
        outFile=data/out-${i}.${j}
        ../../tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.als -method als -regular '0,0,10' -init_stdev 0.1
    done
done

#../../tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.sgd -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1
#../../tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.als -method als -regular '0,0,10' -init_stdev 0.1
#../../tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.mcmc -method mcmc -init_stdev 0.1

