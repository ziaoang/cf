#for i in 1 10 20; do
#    for j in $(seq 1 5); do
#        python rsme.py baseline/libmf/data/test-${i}m.${j}.txt baseline/libmf/data/${i}m.${j}.out 2 0
#    done
#done

for i in 1 10 20; do
    for j in $(seq 1 5); do
        python mae.py baseline/libmf/data/test-${i}m.${j}.txt baseline/libmf/data/${i}m.${j}.out 2 0
    done
done
