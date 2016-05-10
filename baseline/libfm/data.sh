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

