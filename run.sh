for i in 1m 10m 20m net; do
    for j in $(seq 1 5); do
        python mae.py baseline/libmf/data/test-${i}.${j}.txt baseline/libmf/data/${i}.${j}.out 2 0
    done
done

