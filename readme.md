build: docker build . --tag predictme-ml
tag: docker tag predictme-ml id997/predictme-ml:0.3.0
push: docker push id997/predictme-ml:0.3.0
hash: docker pull id997/predictme-ml:0.3.0 | grep "Digest: sha256:" | sed 's/.*sha256:/0x/'
link: registry.hub.docker.com/id997/predictme-ml:0.2.3


run with input_files: docker run \
    -v /Users/id/Documents/projects/predictme-iexec/predictme-ml/io/iexec_in:/iexec_in \
    -v /Users/id/Documents/projects/predictme-iexec/predictme-ml/io/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    id997/predictme-ml:0.3.0 \
    RLCUSDT
    