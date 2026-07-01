# SpliceVision

## Interactive DNA Sequence Analysis Platform

SpliceVision is a bioinformatics web application developed in Python using Streamlit, Biopython, and Pandas. The application provides an interactive interface for basic DNA sequence analysis, enabling users to upload FASTA files or use a built-in example sequence for demonstration.

The project is intended as an educational and exploratory tool for sequence analysis and molecular biology workflows.

---

## Features

- Upload DNA sequences in FASTA format
- Built-in example FASTA sequence for demonstration
- DNA sequence validation
- Sequence length calculation
- GC and AT content analysis
- Nucleotide composition analysis
- Interactive nucleotide count visualization
- Detection of canonical splice donor (GT) and acceptor (AG) motifs
- Open Reading Frame (ORF) identification
- DNA transcription to RNA
- DNA translation into protein sequence
- Export splice-site results as CSV

---

## Technologies

- Python
- Streamlit
- Biopython
- Pandas

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Tanurgvns/SpliceVision.git
```

Navigate to the project directory:

```bash
cd SpliceVision
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Input

The application accepts DNA sequences in FASTA format.

Users may either:

- Upload their own FASTA file
- Load the built-in example FASTA sequence

---

## Output

The application provides:

- Sequence summary statistics
- GC and AT content
- Nucleotide composition table and chart
- Canonical splice-site detection
- Open Reading Frame (ORF) predictions
- RNA transcription
- Protein translation
- Downloadable CSV file containing splice-site information

---

## Repository Structure

```
SpliceVision/
│
├── app.py
├── requirements.txt
├── README.md
└── sample.fasta
```

---

## Future Development

Future versions may include:

- Reverse complement generation
- Restriction enzyme site analysis
- Sequence motif search
- Exon and intron prediction
- Alternative splice-site prediction
- Interactive genome visualization
- Downloadable PDF reports

---

## Author

**Tanushka Raghuvanshi**

GitHub: https://github.com/Tanurgvns

LinkedIn: https://www.linkedin.com/in/tanushka30/
