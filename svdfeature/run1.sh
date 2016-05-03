#python format_bias.py ../data/my/train-1m.txt ../data/my/test-1m.txt data/train-1m.txt data/test-1m.txt
#python format_bias.py ../data/my/train-10m.txt ../data/my/test-10m.txt data/train-10m.txt data/test-10m.txt
#python format_bias.py ../data/my/train-20m.txt ../data/my/test-20m.txt data/train-20m.txt data/test-20m.txt

python genConf.py data/train-1m.txt data/test-1m.txt data/conf-1m.txt
python genConf.py data/train-10m.txt data/test-10m.txt data/conf-10m.txt
python genConf.py data/train-20m.txt data/test-20m.txt data/conf-20m.txt

