for i in 1 10 20; do
    for j in $(seq 1 5); do
        python feature.py ../data/my/train-${i}m.${j}.txt data/model-${i}m.${j}.txt
    done
done


