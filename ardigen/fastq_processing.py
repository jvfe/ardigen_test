import gzip
from io import StringIO, TextIOWrapper
from pathlib import Path

from Bio import SeqIO
from matplotlib import pyplot as plt
from pandas import DataFrame
from seaborn import barplot


def parse_fastq(fastq: Path) -> SeqIO.QualityIO.FastqPhredIterator:

    if ".gz" in fastq.suffixes:
        with TextIOWrapper(gzip.open(fastq)) as f:
            parsed_fastq = SeqIO.parse(StringIO(f.read()), "fastq")
            return parsed_fastq

    parsed_fastq = SeqIO.parse(fastq, "fastq")

    return parsed_fastq


def get_fastq_df(parsed_fastq: SeqIO.QualityIO.FastqPhredIterator) -> DataFrame:

    fastq_dict = {
        record.id: record.letter_annotations["phred_quality"] for record in parsed_fastq
    }

    fastq_df = DataFrame(fastq_dict)

    fastq_stats = fastq_df.apply(DataFrame.describe, axis=1)

    final_stats_df = fastq_stats[["mean", "std"]].copy()
    final_stats_df["read_position"] = fastq_stats.index + 1
    final_stats_df = final_stats_df.loc[:, ["read_position", "mean", "std"]].rename(
        {"mean": "mean_Phred_qual", "std": "standard_deviation_Phred_qual"}, axis=1
    )

    return final_stats_df


def generate_plot(stats_df: DataFrame):

    fig, ax = plt.subplots(figsize=(16, 10))
    p = barplot(
        stats_df,
        x="read_position",
        y="mean_Phred_qual",
        yerr=stats_df["standard_deviation_Phred_qual"],
        capsize=1,
        errcolor=".5",
        linewidth=3,
        edgecolor="1",
        facecolor=".7",
        ax=ax,
    )
    p.set_xticks(range(0, len(stats_df["read_position"]), 5))
    return fig


def process_fastq(fastq_file: str):
    path_input = Path(fastq_file)
    sample_id = path_input.stem

    parsed_fastq = parse_fastq(path_input)
    fastq_df = get_fastq_df(parsed_fastq)
    plot = generate_plot(fastq_df)

    output_dir = Path("Ardigen_FastQ_results").resolve()
    if output_dir.exists() == False:
        output_dir.mkdir()
    fastq_df.to_csv(Path(output_dir, f"{sample_id}.tsv"), index=False, sep="\t")
    plot.savefig(Path(output_dir, f"{sample_id}.pdf"))

    return fastq_df, plot
