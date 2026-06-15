class ObjectStoreAdapter:
    def __init__(self, bucket=None):
        self.bucket = bucket
        self._objects = {}

    def save(self, key, content):
        if not self.bucket:
            raise RuntimeError("object store bucket is not configured")
        self._objects[key] = content
        return {"backend": "object_store", "key": key, "status": "saved"}

    def read(self, key):
        return self._objects[key]
