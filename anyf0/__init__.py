import contextlib
import os

with contextlib.suppress(ImportError):
    from nvidia import cu13, cudnn
    os.environ["PATH"] += os.pathsep + os.sep.join([cu13.__path__[0], "bin"])
    os.environ["PATH"] += os.pathsep + os.sep.join([cudnn.__path__[0], "bin"])