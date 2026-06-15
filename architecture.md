import os

from app.filesystem_adapter import FilesystemAdapter
from app.object_store_adapter import ObjectStoreAdapter
from app.storage_router import HybridStorageRouter


DEFAULT_BACKEND = "filesystem"


def get_storage_backend():
    backend = os.getenv("STORAGE_BACKEND", DEFAULT_BACKEND)

    if backend == "filesystem":
        return FilesystemAdapter(os.getenv("STORAGE_PATH", "./data"))
    if backend == "object_store":
        return ObjectStoreAdapter(bucket=os.getenv("STORAGE_BUCKET"))
    if backend == "hybrid":
        return HybridStorageRouter()

    raise ValueError(f"Unsupported storage backend: {backend}")
