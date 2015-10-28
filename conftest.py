import multiprocessing
import pytest
from FTP import server


@pytest.fixture(scope="session")
def run_ftp():
    p = multiprocessing.Process(target=server.main)
    p.start()
