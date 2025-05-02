import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
import filecmp
from .utils import *
from alphacopy.devicesutil import DevicesUtil
from pathlib import Path

devices = DevicesUtil("test_user")


def test_copy_file(random_file):
    src = random_file
    dst = 'output_file'
    devices.copy_file(src, dst)

    assert os.path.exists(dst)
    assert filecmp.cmp(src, dst)

    os.remove(dst)


def test_compare_hash(random_file):

    src = random_file
    dst = 'output_file'
    devices.copy_file(src, dst)

    # Check if the hash is the same
    assert devices.compare_hash(src, dst) is True

    # Change the dst contents and see if the hash is different
    write_random_data_to_file(dst, 1000)
    assert devices.compare_hash(src, dst) is False

    # Clean up
    os.remove(dst)


def test_list_disks(tmpdir):

    # Make a temporary volumes path
    volumes_path = tmpdir / "test_user"
    devices.volumes_path = volumes_path
    os.mkdir(volumes_path)

    # Make sure it exists
    assert os.path.exists(volumes_path)

    test_disks = ["test_disk_1", "test_disk_2"]

    for test_disk in test_disks:
        test_disk_path = volumes_path / test_disk
        os.mkdir(test_disk_path)

    disks = devices.list_disks()

    assert len(disks) == len(test_disks)

    for disk in disks:
        assert disk in test_disks

    shutil.rmtree(volumes_path)


def test_copy_files_parallel(random_tree, tmpdir):
    """
    Testa a cópia paralela de múltiplos arquivos e diretórios,
    garantindo que todos os arquivos sejam copiados corretamente e com integridade.
    """
    src_root = random_tree
    dst_root = tmpdir / "backup_dest"

    devices = DevicesUtil("test_user")
    files = [str(item) for item in Path(src_root).rglob("*") if Path(item).is_file()]

    # Executa a cópia paralela
    devices.copy_files(files, dst_root)

    # Verifica se todos os arquivos foram copiados e se os hashes batem
    for file in files:
        # Monta o caminho relativo esperado no destino
        rel_path = os.path.relpath(file, start=str(src_root))
        # O método copy_files cria uma subpasta com timestamp
        backup_folders = list(Path(dst_root).glob("*"))
        assert backup_folders, "Nenhuma pasta de backup criada"
        backup_folder = backup_folders[0]
        dst_file = backup_folder / rel_path
        assert dst_file.exists(), f"Arquivo não copiado: {dst_file}"
        assert devices.compare_hash(file, dst_file), f"Hash diferente para o arquivo: {file}"
