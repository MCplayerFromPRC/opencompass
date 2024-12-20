import os
import sys
from pathlib import Path

sys.path.insert(0, os.getcwd())
sys.path.insert(0, Path(__file__).parent.as_posix())

from opencompass.cli.customized_main import \
    main  # noqa: E402 # pylint: disable=C0413

if __name__ == '__main__':
    main()
