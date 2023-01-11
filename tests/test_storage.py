from pgbackup import storage
import tempfile


def test_storing_file_locally():
    """Write  content from one filelike to another"""

    infile=tempfile.TemporaryFile()