import os
import shutil
import pytest

from zipfile import ZipFile
from utils import TMP_PATH, RESOURCES_PATH


@pytest.fixture(autouse=True, scope='session')
def make_zip_and_tmp():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    file_dir = os.listdir(RESOURCES_PATH)
    with ZipFile('tmp/test.zip', mode='w') as zf:
        for file in file_dir:
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file, arcname=file)

    yield

    shutil.rmtree(TMP_PATH)
