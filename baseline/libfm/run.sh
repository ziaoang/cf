# ml-1m
for i in $(seq 1 5); do
    python format.py ../../data/movielens/ml-1m/ratings.dat ../../data/my/train-1m.${i}.txt ../../data/my/test-1m.${i}.txt data/train-1m.${i}.libfm data/test-1m.${i}.libfm
done

# ml-10m
for i in $(seq 1 5); do
    python format.py ../../data/movielens/ml-10M100K/ratings.dat ../../data/my/train-10m.${i}.txt ../../data/my/test-10m.${i}.txt data/train-10m.${i}.libfm data/test-10m.${i}.libfm
done

# ml-20m
for i in $(seq 1 5); do
    python format.py ../../data/movielens/ml-20m/ratings.csv ../../data/my/train-20m.${i}.txt ../../data/my/test-20m.${i}.txt data/train-20m.${i}.libfm data/test-20m.${i}.libfm
done

# netflix
for i in $(seq 1 5); do
    python format.py ../../data/netflix/data/netflix.dat ../../data/my/train-net.${i}.txt ../../data/my/test-net.${i}.txt data/train-net.${i}.libfm data/test-net.${i}.libfm
done


#trainFile=data/train-1m.1.libfm
#testFile=data/test-1m.1.libfm
#outFile=data/out-1m.1
#./tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.sgd -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1
#../../tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.als -method als -regular '0,0,10' -init_stdev 0.1
#./tool/libfm-1.42.src/bin/libFM -task r -train $trainFile -test $testFile -out ${outFile}.mcmc -method mcmc -init_stdev 0.1
