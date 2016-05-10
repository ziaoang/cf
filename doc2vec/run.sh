for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        python feature.py ../data/my/train-${i}.${j}.txt data/model-${i}.${j}.txt
    done
done


