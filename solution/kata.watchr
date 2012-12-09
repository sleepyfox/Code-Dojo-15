# This automatically runs the vows tests
watch('.*\.coffee') {|match| system "mocha --compilers coffee:coffee-script -R spec test-*.coffee"}
