export MINIO_ROOT_USER=minioadmin
export MINIO_ROOT_PASSWORD=minioadmin

mc alias set localminio http://localhost:9002 $MINIO_ROOT_USER $MINIO_ROOT_PASSWORD
mc mb localminio/delta-aq
mc policy set public localminio/delta-aq