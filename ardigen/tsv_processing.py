from functools import reduce
from pathlib import Path

from matplotlib import pyplot as plt
from numpy import log10
from pandas import DataFrame, merge, read_table
from seaborn import histplot


def get_max_in_group(df: DataFrame, index: str, max_of: str) -> DataFrame:

    df_grouped = df.copy().groupby(index, as_index=False)

    return df_grouped[max_of].max()


def filter_alignment(df: DataFrame) -> DataFrame:
    """
    First, filter hits that have the best bitscore, then minimum evalue
    (through -log10(evalue))
    Then, in decreasing order of priority, highest pident, highest length
    and less mismatches

    If there are still duplicated queries, take the first.
    """

    df = df.copy()

    df["-log10(evalue)"] = -log10(df["evalue"])

    max_ofs = ["bitscore", "-log10(evalue)", "pident", "length"]

    dfs = [get_max_in_group(df, "qseqid", max_of) for max_of in max_ofs]
    min_mismatches = df.copy().groupby("qseqid", as_index=False)["mismatch"].min()
    dfs.append(min_mismatches)

    best_hits_df = reduce(lambda df1, df2: merge(df1, df2, on="qseqid"), dfs)

    merged = best_hits_df.merge(df)
    duplicated_subset = ["qseqid"] + max_ofs
    unique = merged.drop_duplicates(subset=duplicated_subset, keep="first")

    return unique


def tabulate_lengths(filtered_alignment: DataFrame) -> DataFrame:
    value_counts = filtered_alignment["length"].value_counts()
    abundances_df = (
        value_counts.rename_axis("alignment_lengths")
        .reset_index(name="abundance")
        .sort_values("abundance", ignore_index=True)
    )

    return abundances_df


def plot_lengths(filtered_alignment: DataFrame) -> DataFrame:
    fig, ax = plt.subplots(figsize=(16, 10))

    histplot(data=filtered_alignment, x="length", binwidth=1, ax=ax)

    return fig


def process_tsv(alignment_result: str):
    path_input = Path(alignment_result).resolve()
    sample_id = path_input.stem

    df = read_table(
        path_input,
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

    filtered = filter_alignment(df)
    tabulated = tabulate_lengths(filtered)
    plot = plot_lengths(filtered)

    output_dir = Path("Ardigen_TSV_results").resolve()

    if output_dir.exists() == False:
        output_dir.mkdir()

    tabulated.to_csv(Path(output_dir, f"{sample_id}.csv"), index=False)
    plot.savefig(Path(output_dir, f"{sample_id}.pdf"))

    return tabulated, plot
