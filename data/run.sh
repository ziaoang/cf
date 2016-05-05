#python split.py movielens/ml-1m/ratings.dat my/train-1m.txt my/test-1m.txt 0.9
#python split.py movielens/ml-10M100K/ratings.dat my/train-10m.txt my/test-10m.txt 0.9
#python split.py movielens/ml-20m/ratings.csv my/train-20m.txt my/test-20m.txt 0.9

python statistics.py my/train-1m.txt my/test-1m.txt
python statistics.py my/train-10m.txt my/test-10m.txt
python statistics.py my/train-20m.txt my/test-20m.txt

