#for i in 100k 1m 10m 20m net; do
#    for j in $(seq 1 5); do
#        python rsme.py baseline/libmf/data/test-${i}.${j}.txt baseline/libmf/data/${i}.${j}.out 2 0
#        python mae.py baseline/libmf/data/test-${i}.${j}.txt baseline/libmf/data/${i}.${j}.out 2 0
#        python rsme.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.sgd 0 0
#        python mae.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.sgd 0 0
#        python rsme.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.als 0 0
#        python mae.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.als 0 0
#        python rsme.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.mcmc 0 0
#        python mae.py baseline/libfm/data/test-${i}.${j}.libfm baseline/libfm/data/out-${i}.${j}.mcmc 0 0
#    done
#done


#for i in 1m 10m 20m net; do
for i in 10m; do
    #for j in $(seq 1 5); do
    for j in 1; do
        echo $i $j
        for k in $(seq 0 50); do
            python rsme.py feature/data/test-${i}.${j}.2.txt svdfeature/data-${i}.${j}/out-${i}.${j}.${k}.txt 0 0
            #python mae.py feature/data/test-${i}.${j}.2.txt svdfeature/data-${i}.${j}/out-${i}.${j}.${k}.txt 0 0
        done
    done
done
