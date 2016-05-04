#python feature.py ../data/my/train-1m.txt data/model-1m.txt
#python feature.py ../data/my/train-10m.txt data/model-10m.txt
#python feature.py ../data/my/train-20m.txt data/model-20m.txt


for i in $(seq 1 9); do
    python scale.py data/model-1m.txt data/model-1m.0.${i}.txt 0.${i}
    python scale.py data/model-10m.txt data/model-10m.0.${i}.txt 0.${i}
    python scale.py data/model-20m.txt data/model-20m.0.${i}.txt 0.${i}
done
