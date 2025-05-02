import os
import shutil
import psutil
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from humanize import naturalsize
from pathlib import Path
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

class DevicesUtil(QObject):
    file_copied = pyqtSignal()
    volumes_path = ''

    def __init__(self, user = os.environ.get('USER')):
        super(QObject, self).__init__()
        self.volumes_path = '/media/' + user

    def list_disks(self):
        directories = []
        try:
            directories = os.listdir(self.volumes_path)
        except FileNotFoundError:
            pass
        return directories

    def disk_size(self, label):
        total, used, free = shutil.disk_usage(self.volumes_path + '/' + label)
        return total // (2 ** 30)

    def list_files(self, dir):
        files = [str(item) for item in list(Path(dir).rglob("*"))]
        return files

    def get_hash(self, filename):
        sha256_hash = hashlib.sha256()
        buffer_size = 262144  # 256 KB para maior desempenho
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(buffer_size), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def compare_hash(self, file1, file2):
        return self.get_hash(file1) == self.get_hash(file2)

    def verify_copy(self, src, dst):
        """
        Verifica se dois arquivos são idênticos usando SHA-256.
        Retorna True se forem idênticos, False caso contrário.
        Não emite sinais nem altera o estado da interface.
        """
        return self.compare_hash(src, dst)

    def copy_files(self, files, dest):
        try:
            dest = self.make_dir(dest)
        except Exception as e:
            raise e
            return

        # Get the common root of all files (the source root)
        if files:
            src_root = os.path.commonpath(files)
        else:
            src_root = ""

        def copy_single_file(file):
            # Compute the relative path from the source root
            rel_path = os.path.relpath(file, start=src_root)
            dest_path = os.path.join(dest, rel_path)
            dest_dir = os.path.dirname(dest_path)
            os.makedirs(dest_dir, exist_ok=True)
            if Path(file).is_file():
                self.copy_file(file, dest_path)
            else:
                Path(dest_path).mkdir(exist_ok=True)

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(copy_single_file, file) for file in files]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Erro ao copiar arquivo: {e}")

    def make_dir(self, base_path):
        now = datetime.now()
        dt_string = now.strftime('%Y_%m_%d_%H-%M-%S')
        new_folder = os.path.join(base_path, dt_string)
        os.makedirs(new_folder, exist_ok=True)
        return new_folder

    def copy_file(self, file, dest_path):
        shutil.copy2(file, dest_path)
        if self.compare_hash(file, dest_path):
            self.file_copied.emit()
            return True
        else:
            error_msg = "Error: " + file
            raise Exception(error_msg)

    def eject_disk(self, label):
        command = "umount " + self.volumes_path + "/" + label
        return os.system(command) == 0

    def used_disk(self):
        used_disk = psutil.disk_usage(self.volumes_path)
        used_space = str(used_disk[1])
        used_bytes = str(used_space[:6])
        natural_bytes = (naturalsize(used_bytes))
        return natural_bytes

    def free_disk(self):
        free_disk = psutil.disk_usage(self.volumes_path)
        free_space = str(free_disk[2])
        free_bytes: str = free_space[:3]
        info_free = (free_bytes + ' GB Free')
        return info_free
