# PredictMe Docker Image
run with args:
` docker run \
    -v /Users/id/Documents/projects/predictme-iexec/predictme-ml/io/iexec_in:/iexec_in \
    -v /Users/id/Documents/projects/predictme-iexec/predictme-ml/io/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    id997/predictme-ml:0.3.0 \
    RLCUSDT
`