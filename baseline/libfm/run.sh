./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test train.libfm -out train.sgd -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1
./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test train.libfm -out train.als -method als -regular '0,0,10' -init_stdev 0.1
./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test train.libfm -out train.mcmc -method mcmc -init_stdev 0.1
./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test test.libfm -out test.sgd -method sgd -learn_rate 0.01 -regular '0,0,0.01' -init_stdev 0.1
./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test test.libfm -out test.als -method als -regular '0,0,10' -init_stdev 0.1
./tool/libfm-1.42.src/bin/libFM -task r -train train.libfm -test test.libfm -out test.mcmc -method mcmc -init_stdev 0.1
