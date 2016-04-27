#th data.lua  -ratings ../../data/ml-1m/ratings.dat -out movieLens-1M.t7 -fileType movieLens -ratio 0.9
#th main.lua  -file movieLens-1M.t7 -conf ../conf/my.conf -save network.t7 -type V -meta 0 -gpu 0
th main.lua  -file ../my/newTrain.t7 -conf ../my/my.conf -save ../my/network.t7 -type U -meta 0 -gpu 0
#th main.lua  -file ../my/newTrain.t7 -conf ../my/my.conf -save ../my/network.t7 -type V -meta 0 -gpu 0



