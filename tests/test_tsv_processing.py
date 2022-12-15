import shutil
from pathlib import Path

from pandas import DataFrame, read_table
from pandas.testing import assert_frame_equal
from pytest import mark

from ardigen import process_tsv
from ardigen.tsv_processing import filter_alignment, tabulate_lengths


def test_filter_alignment(sample_alignment):
    df = filter_alignment(sample_alignment)
    expected_lines = DataFrame(
        {
            "qseqid": ["read.1", "read.2", "read.3"],
            "length": [92, 92, 52],
        }
    )

    assert_frame_equal(df.loc[:, ["qseqid", "length"]], expected_lines)


def test_tabulate_lengths(sample_alignment):
    df = filter_alignment(sample_alignment)
    tabulated = tabulate_lengths(df)
    expected_lines = DataFrame(
        {
            "alignment_lengths": [52, 92],
            "abundance": [1, 2],
        }
    )

    assert_frame_equal(tabulated, expected_lines)

@mark.parametrize(
    "input_file, output_file",
    [
        ("data/small_alignment.b6", "Ardigen_TSV_results/small_alignment"),
        ("data/alignment.b6", "Ardigen_TSV_results/alignment"),
    ],
)
def test_process_tsv(input_file, output_file):
    tsv_file = Path(f"{output_file}.csv").resolve()
    plot_file = Path(f"{output_file}.pdf").resolve()

    if tsv_file.exists() or plot_file.exists():
        shutil.rmtree(Path("Ardigen_TSV_results/"))

    process_tsv(input_file)

    assert tsv_file.exists()
    assert plot_file.exists()
