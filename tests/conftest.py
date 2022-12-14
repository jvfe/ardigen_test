from pathlib import Path

from Bio import SeqIO
from pandas import read_table
from pytest import fixture


@fixture
def sample_fastq():
    records = SeqIO.parse(Path("data/small_reads.fastq"), "fastq")
    return records


@fixture
def sample_alignment():
    return read_table(
        Path("data/small_alignment.b6"),
        names=[
            "qseqid",
            "sseqid",
            "pident",
            "length",
            "mismatch",
            "gapopen",
            "qstart",
            "qend",
            "sstart",
            "send",
            "evalue",
            "bitscore",
        ],
    )
