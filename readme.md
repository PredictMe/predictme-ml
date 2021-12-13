
build :  docker build . --tag app_test

run : docker run --rm     -v /Users/id/Documents/projects/ml_iexec/iexec_app/io/iexec_in:/iexec_in     -v /Users/id/Documents/projects/ml_iexec/iexec_app/io/iexec_out:/iexec_out     -e IEXEC_IN=/iexec_in     -e IEXEC_OUT=/iexec_out     app_test arg1 arg2 arg3

run with input_files: docker run \
    -v /Users/id/Documents/projects/ml_iexec/iexec_app/io/iexec_in:/iexec_in \
    -v /Users/id/Documents/projects/ml_iexec/iexec_app/io/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    -e IEXEC_INPUT_FILE_NAME_1=jsoninput.json \
    -e IEXEC_INPUT_FILES_NUMBER=1 \
    app_test \
    arg1 arg2 arg3