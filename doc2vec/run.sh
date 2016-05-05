#python feature.py ../data/my/train-1m.txt data/model-1m.txt
#python feature.py ../data/my/train-10m.txt data/model-10m.txt
#python feature.py ../data/my/train-20m.txt data/model-20m.txt


python scale.py data/model-1m.txt data/model-1m.2.5.txt 2.5
#for i in $(seq 2 9); do
    #python scale.py data/model-1m.txt data/model-1m.${i}.txt ${i}
    #python scale.py data/model-10m.txt data/model-10m.${i}.txt ${i}
    #python scale.py data/model-20m.txt data/model-20m.${i}.txt ${i}
#done
