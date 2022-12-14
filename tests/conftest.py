from Bio import SeqIO
from pytest import fixture


@fixture
def sample_fastq():
    records = SeqIO.parse("data/small_reads.fastq", "fastq")
    return records
