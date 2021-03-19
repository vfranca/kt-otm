from kt_otm import cli
from click.testing import CliRunner


def test_exibe_strikes_fora_do_dinheiro():
    runner = CliRunner()
    res = runner.invoke(cli.cli, ["25.00"])
    assert res.output == "26.25\n23.75\n"
    assert res.exit_code == 0
