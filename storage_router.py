from pathlib import Path


class FilesystemAdapter:
    def __init__(self, base_path="./data"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save(self, key, content):
        target = self.base_path / key
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        return {"backend": "filesystem", "key": key, "status": "saved"}

    def read(self, key):
        return (self.base_path / key).read_text()
