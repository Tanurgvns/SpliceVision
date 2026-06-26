# 🧬 SpliceVision

## Interactive Gene Splicing Analyzer

**SpliceVision** is an interactive bioinformatics web application built with **Python**, **Streamlit**, **Biopython**, and **Pandas**. The application enables users to upload DNA sequences in FASTA format and perform basic sequence analysis and splice-site detection through an easy-to-use web interface.

---

## Features

* 📂 Upload DNA sequences in FASTA format
* ✅ Validate DNA sequences
* 📏 Calculate sequence length
* 🧬 Calculate GC content
* 📊 Calculate AT content
* 📈 Display nucleotide composition
* 📉 Interactive nucleotide count visualization
* 🔍 Detect canonical splice donor (GT) sites
* 🔍 Detect canonical splice acceptor (AG) sites
* 📥 Download detected splice-site information as CSV

---

## Technologies Used

* Python
* Streamlit
* Biopython
* Pandas
* Git & GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Tanurgvns/SpliceVision.git
```

Move into the project directory:

```bash
cd SpliceVision
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Project Structure

```
SpliceVision/
│
├── app.py
├── requirements.txt
├── README.md
└── sample.fasta
```

---

## Future Improvements

* Exon and intron prediction
* RNA splicing simulation
* mRNA generation
* Protein translation
* Gene structure visualization
* Mutation impact analysis
* Interactive genome browser
* Downloadable PDF analysis reports

---

## Author

**Tanushka Raghuvanshi**

GitHub: https://github.com/Tanurgvns
