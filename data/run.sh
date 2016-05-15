#python split.py movielens/ml-1m/ratings.dat my/train-1m my/test-1m 0.9 5
#python split.py movielens/ml-10M100K/ratings.dat my/train-10m my/test-10m 0.9 5
#python split.py movielens/ml-20m/ratings.csv my/train-20m my/test-20m 0.9 5
#for i in 1 10 20; do
#    for j in $(seq 1 5); do
#        python statistics.py my/train-${i}m.${j}.txt my/test-${i}m.${j}.txt
#    done
#done

#python split.py netflix/data/netflix.dat my/train-net my/test-net 0.9 5
#for k in $(seq 1 5); do
#    python statistics.py my/train-net.${k}.txt my/test-net.${k}.txt
#done

python split.py movielens/ml-100k/u.data my/train-100k my/test-100k 0.9 5
for k in $(seq 1 5); do
    python statistics.py my/train-100k.${k}.txt my/test-100k.${k}.txt
done
