#for i in 1m 10m 20m net; do
#    for j in $(seq 1 5); do
#        python feature.py ../data/my/train-${i}.${j}.txt data/model-${i}.${j}.txt
#    done
#done

for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        python scale.py data/model-${i}.${j}.txt data/model-${i}.${j}.2.txt 2
    done
done

