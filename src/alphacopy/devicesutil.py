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
        except Exception as e:
            print(f"Erro ao listar discos: {e}")
            directories = []
        return directories

    def disk_size(self, label):
        try:
            total, used, free = shutil.disk_usage(os.path.join(self.volumes_path, label))
            return total // (2 ** 30)
        except Exception as e:
            print(f"Erro ao obter tamanho do disco '{label}': {e}")
            return 0

    def list_files(self, dir):
        try:
            files = [str(item) for item in list(Path(dir).rglob("*"))]
            return files
        except Exception as e:
            print(f"Erro ao listar arquivos em '{dir}': {e}")
            return []

    def get_hash(self, filename):
        sha256_hash = hashlib.sha256()
        buffer_size = 262144  # 256 KB para maior desempenho
        try:
            with open(filename, "rb") as f:
                for byte_block in iter(lambda: f.read(buffer_size), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"Erro ao calcular hash de '{filename}': {e}")
            return None

    def compare_hash(self, file1, file2):
        hash1 = self.get_hash(file1)
        hash2 = self.get_hash(file2)
        if hash1 is None or hash2 is None:
            return False
        return hash1 == hash2

    def copy_files(self, files, dest):
        try:
            dest = self.make_dir(dest)
        except Exception as e:
            print(f"Erro ao criar diretório de destino: {e}")
            return

        if files:
            src_root = os.path.commonpath(files)
        else:
            src_root = ""

        def copy_single_file(file):
            try:
                rel_path = os.path.relpath(file, start=src_root)
                dest_path = os.path.join(dest, rel_path)
                dest_dir = os.path.dirname(dest_path)
                os.makedirs(dest_dir, exist_ok=True)
                if Path(file).is_file():
                    self.copy_file(file, dest_path)
                else:
                    Path(dest_path).mkdir(exist_ok=True)
            except Exception as e:
                print(f"Erro ao copiar '{file}': {e}")

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
        try:
            os.makedirs(new_folder, exist_ok=True)
        except Exception as e:
            print(f"Erro ao criar diretório '{new_folder}': {e}")
            raise
        return new_folder

    def copy_file(self, file, dest_path):
        try:
            shutil.copy2(file, dest_path)
            if self.compare_hash(file, dest_path):
                self.file_copied.emit()
                return True
            else:
                error_msg = "Error: " + file
                print(error_msg)
                raise Exception(error_msg)
        except Exception as e:
            print(f"Erro ao copiar arquivo '{file}' para '{dest_path}': {e}")
            raise

    def eject_disk(self, label):
        # Validação simples para evitar injeção de comandos
        if not label.isalnum():
            print("Nome de dispositivo inválido")
            raise ValueError("Nome de dispositivo inválido")
        command = "umount " + self.volumes_path + "/" + label
        try:
            return os.system(command) == 0
        except Exception as e:
            print(f"Erro ao ejetar disco '{label}': {e}")
            return False

    def used_disk(self):
        try:
            used_disk = psutil.disk_usage(self.volumes_path)
            used_bytes = used_disk.used
            natural_bytes = naturalsize(used_bytes)
            return natural_bytes
        except Exception as e:
            print(f"Erro ao obter espaço usado: {e}")
            return "N/A"

    def free_disk(self):
        try:
            free_disk = psutil.disk_usage(self.volumes_path)
            free_bytes = free_disk.free // (2 ** 30)
            info_free = f"{free_bytes} GB Free"
            return info_free
        except Exception as e:
            print(f"Erro ao obter espaço livre: {e}")
            return "N/A"
