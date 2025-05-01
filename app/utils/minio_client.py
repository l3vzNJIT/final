from minio import Minio
from minio.error import S3Error
import os

minio_client = Minio(
    endpoint=os.getenv("MINIO_ENDPOINT", "minio:9000"),
    access_key=os.getenv("MINIO_ROOT_USER", "minioadmin"),
    secret_key=os.getenv("MINIO_ROOT_PASSWORD", "minioadmin"),
    secure=False
)

bucket_name = "myapp-bucket"

def ensure_bucket_exists():
    try:
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
    except Exception as e:
        raise RuntimeError(f"Warning: could not verify or create bucket: {e}")
