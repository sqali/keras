try:
    # When using torch and tensorflow, torch needs to be imported first,
    # otherwise it will segfault upon import. This should force the torch
    # import to happen first for all tests.
    import torch  # noqa: F401
except ImportError:
    pass

import pytest

from keras.backend import backend


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "requires_trainable_backend: mark test for trainable backend only",
    )


def pytest_collection_modifyitems(config, items):
    requires_trainable_backend = pytest.mark.skipif(
        backend() == "numpy",
        reason="Trainer not implemented for NumPy backend.",
    )
    for item in items:
        if "requires_trainable_backend" in item.keywords:
            item.add_marker(requires_trainable_backend)
