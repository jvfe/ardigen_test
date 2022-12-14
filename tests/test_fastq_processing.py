import shutil
from pathlib import Path

from pandas import DataFrame
from pandas.testing import assert_frame_equal
from pytest import mark

from ardigen import process_fastq
from ardigen.fastq_processing import get_fastq_df, parse_fastq


# Can process both compressed and uncompressed files
@mark.parametrize(
    "input_file, output_record_one",
    [("data/small_reads.fastq.gz", "read.1"), ("data/small_reads.fastq", "read.1")],
)
def test_read_gzipped_fastq(input_file, output_record_one):

    results = parse_fastq(Path(input_file))

    record_ids = [record.id for record in results]

    assert record_ids[0] == output_record_one


# Can generate the statistics
def test_get_fastq_df(sample_fastq):
    df = get_fastq_df(sample_fastq)
    expected_lines = DataFrame(
        {
            "read_position": [1, 2, 3],
            "mean_Phred_qual": [32.6667, 33.6667, 33.6667],
            "standard_deviation_Phred_qual": [
                1.5275252316519465,
                0.5773502691896258,
                0.5773502691896258,
            ],
        }
    )

    assert_frame_equal(df.iloc[[0, 1, 2]], expected_lines)


@mark.parametrize(
    "input_file, output_file",
    [
        ("data/small_reads.fastq", "Ardigen_FastQ_results/small_reads"),
        ("data/reads.fastq", "Ardigen_FastQ_results/reads"),
    ],
)
def test_process_fastq(input_file, output_file):
    tsv_file = Path(f"{output_file}.tsv").resolve()
    plot_file = Path(f"{output_file}.pdf").resolve()

    if tsv_file.exists() or plot_file.exists():
        shutil.rmtree(Path("Ardigen_FastQ_results/"))

    process_fastq(input_file)

    assert tsv_file.exists()
    assert plot_file.exists()
