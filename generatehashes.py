import hashlib
import os
from glob import glob
from typing import Callable


def GetFileSize(path: str) -> str:
    return os.path.getsize(path)


def GetFileMd5(path: str) -> str:
    return GetFileHash(path, hashlib.md5)


def GetFileSha256(path: str) -> str:
    return GetFileHash(path, hashlib.sha256)


def GetFileHash(path: str, hashFunc: Callable) -> str:
    hashStr: str = ""
    if os.path.isfile(path):
        hashObj: hashlib._Hash = hashFunc()
        with open(path, "rb") as rfile:
            for chunk in iter(lambda: rfile.read(4096), b""):
                hashObj.update(chunk)
        hashStr = hashObj.hexdigest()
    return hashStr


g_writeFileCount: int = 0

def WriteFile(path: str, data: bytes) -> None:
    if len(data) > 0:
        with open(path, 'wb') as f:
            written: int = f.write(data)
            assert(written == len(data))
        global g_writeFileCount
        g_writeFileCount += 1
        print(f"Created file ({g_writeFileCount}) '{path}'")


def GetAbsFileDir(file: str) -> str:
    dir: str
    dir = os.path.dirname(file)
    dir = os.path.abspath(dir)
    return dir


def GetFileName(file: str) -> str:
    path, name = os.path.split(file)
    return name


def GenerateHashes() -> None:
    thisDir: str = GetAbsFileDir(__file__)
    toolsDir: str = os.path.join(thisDir, "Tools")
    files = list[str]()
    files.extend(glob(os.path.join(toolsDir, "**", "*.exe"), recursive=True))
    files.extend(glob(os.path.join(toolsDir, "**", "*.dll"), recursive=True))
    files.extend(glob(os.path.join(toolsDir, "**", "*.zip"), recursive=True))
    files.extend(glob(os.path.join(toolsDir, "**", "*.7z"), recursive=True))

    file: str
    for file in files:
        newDir: str = os.path.join(GetAbsFileDir(file), "hashes")
        newFile: str = os.path.join(newDir, GetFileName(file))
        os.makedirs(newDir, exist_ok=True)

        md5: str = GetFileMd5(file)
        sha256: str = GetFileSha256(file)
        size: str = GetFileSize(file)

        WriteFile(newFile + ".md5", str.encode(md5))
        WriteFile(newFile + ".sha256", str.encode(sha256))
        WriteFile(newFile + ".size", str.encode(str(size)))


if __name__ == "__main__":
    GenerateHashes()
