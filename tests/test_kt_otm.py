from kt_otm import __version__
from kt_otm import kt_otm


def test_version():
    assert __version__ == "0.2.0"


def test_calcula_call_otm():
    assert kt_otm.call(26.00) == 27.3


def test_calcula_put_otm():
    assert kt_otm.put(26.00) == 24.7
