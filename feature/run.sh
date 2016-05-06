#i=2.5
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.${i}.txt data/train-1m.${i}.d2v.svd data/test-1m.${i}.d2v.svd

#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.2.txt data/train-1m.0.2.d2v.svd data/test-1m.0.2.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.4.txt data/train-1m.0.4.d2v.svd data/test-1m.0.4.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.6.txt data/train-1m.0.6.d2v.svd data/test-1m.0.6.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.8.txt data/train-1m.0.8.d2v.svd data/test-1m.0.8.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.2.txt data/train-1m.2.d2v.svd data/test-1m.2.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.4.txt data/train-1m.4.d2v.svd data/test-1m.4.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.8.txt data/train-1m.8.d2v.svd data/test-1m.8.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.16.txt data/train-1m.16.d2v.svd data/test-1m.16.d2v.svd

#for i in $(seq 1 9); do
#    echo $i
#    python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.${i}.txt data/train-1m.0.${i}.d2v.svd data/test-1m.0.${i}.d2v.svd
#done


#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.0.5.txt data/train-1m.0.5.d2v.svd data/test-1m.0.5.d2v.svd
#python format.py ../data/my/train-10m.txt ../data/my/test-10m.txt ../doc2vec/data/model-10m.0.5.txt data/train-10m.0.5.d2v.svd data/test-10m.0.5.d2v.svd
#python format.py ../data/my/train-20m.txt ../data/my/test-20m.txt ../doc2vec/data/model-20m.0.5.txt data/train-20m.0.5.d2v.svd data/test-20m.0.5.d2v.svd

python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../doc2vec/data/model-1m.txt data/train-1m.d2v.svd data/test-1m.d2v.svd
#python format.py ../data/my/train-10m.txt ../data/my/test-10m.txt ../doc2vec/data/model-10m.txt data/train-10m.d2v.svd data/test-10m.d2v.svd
#python format.py ../data/my/train-20m.txt ../data/my/test-20m.txt ../doc2vec/data/model-20m.txt data/train-20m.d2v.svd data/test-20m.d2v.svd
#python format.py ../data/my/train-1m.txt ../data/my/test-1m.txt ../word2vec/data/model-1m.txt data/train-1m.w2v.svd data/test-1m.w2v.svd
#python format.py ../data/my/train-10m.txt ../data/my/test-10m.txt ../word2vec/data/model-10m.txt data/train-10m.w2v.svd data/test-10m.w2v.svd
#python format.py ../data/my/train-20m.txt ../data/my/test-20m.txt ../word2vec/data/model-20m.txt data/train-20m.w2v.svd data/test-20m.w2v.svd


