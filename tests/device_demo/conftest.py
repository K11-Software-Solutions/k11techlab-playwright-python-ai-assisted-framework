from pathlib import Path
import pytest

@pytest.fixture(scope="session")
def demo_artifacts_dir():
    dirpath = Path(__file__).parent / "artifacts"
    dirpath.mkdir(parents=True, exist_ok=True)
    return dirpath
