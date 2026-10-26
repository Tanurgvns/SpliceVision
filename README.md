# 🧬 SpliceVision

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://splicevision-bioinfo.streamlit.app/)

**Interactive DNA sequence analysis platform**

SpliceVision is a bioinformatics web app built in Python with Streamlit, Biopython and Pandas. Upload a FASTA file, or use the built-in example, to explore nucleotide composition, canonical splice-site motifs, open reading frames, transcription and translation.

It is designed as an educational and exploratory tool for sequence analysis and molecular biology workflows.

## Features

- **Sequence input:** upload a FASTA file or load the built-in example sequence
- **Validation:** checks that the sequence contains only A, T, G, C or N
- **Overview:** sequence ID, length, unknown bases, GC and AT content, and a sequence preview
- **Composition:** nucleotide count table and interactive bar chart
- **Splice-site detection:** canonical GT donor and AG acceptor motifs, with CSV export
- **ORF finder:** ATG-to-stop open reading frames in three forward frames, with the longest ORF highlighted and CSV export
- **Transcription and translation:** DNA to RNA, and DNA to protein

## Try it

Use the app online, with nothing to install: **[Open SpliceVision](https://splicevision-bioinfo.streamlit.app/)**

Or run it on your own computer:

```bash
git clone https://github.com/Tanurgvns/SpliceVision.git
cd SpliceVision
pip install -r requirements.txt
streamlit run app.py
```

## Input and output

**Input:** a DNA sequence in FASTA format, either uploaded or the built-in example (`sample.fasta`).

**Output:**
- Sequence summary statistics, GC and AT content
- Nucleotide composition table and chart
- Canonical splice-site table (downloadable CSV)
- ORF predictions (downloadable CSV)
- RNA transcript and protein translation

> **Note:** SpliceVision detects simple GT/AG motifs only. Not every GT or AG is a true biological splice site; real splice-site prediction also depends on the surrounding sequence context.

## Tech stack

Python · Streamlit · Biopython · Pandas

## Repository structure

```
SpliceVision/
├── app.py            # Streamlit application
├── requirements.txt  # Python dependencies
├── sample.fasta      # Example DNA sequence
└── README.md
```

## Future development

- Reverse complement and six-frame ORF search
- Restriction enzyme site analysis
- Sequence motif search
- Exon and intron prediction
- Alternative splice-site prediction
- Downloadable PDF reports

## Related project

**[DNA Viewer](https://github.com/Tanurgvns/dna-viewer)**: an interactive double-helix visualizer for FASTA files, with GC content plots, six-frame translation and motif search. [Try it live](https://dna-viewer-tanurgvns.streamlit.app/).

## Author

**Tanushka Raghuvanshi**

- GitHub: [Tanurgvns](https://github.com/Tanurgvns)
- LinkedIn: [tanushka30](https://www.linkedin.com/in/tanushka30/)
