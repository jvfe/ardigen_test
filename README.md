# Ardigen Recruitment Tasks

## Install the repository

```bash
make install
```

## Run the unit tests

```bash
# Ensure you have pytest installed
pip install pytest

make test
```

## Usage

```py
from ardigen import (
    fizzbuzz,
    nth_to_mth_fib,
    process_fastq,
    process_tsv
)


fizzbuzz_results = fizzbuzz(
"""
7
16
"""
)
print(fizzbuzz_results)

fibonacci_results = nth_to_mth_fib(
"""
20
25
"""
)
print(fibonacci_results)

data_fastq, plot_fastq = process_fastq("data/reads.fastq")
# Check the folder labeled 'Ardigen_FastQ_results'
# in your working directory to see the outputs

data_tsv, plot_tsv = process_tsv("data/alignment.b6")
# Check the folder labeled 'Ardigen_TSV_results'
# in your working directory to see the outputs
```
