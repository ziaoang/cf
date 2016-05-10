for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        python format.py ../../data/my/train-${i}.${j}.txt ../../data/my/test-${i}.${j}.txt data/train-${i}.${j}.txt data/test-${i}.${j}.txt
    done
done

