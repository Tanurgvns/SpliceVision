import streamlit as st
from Bio import SeqIO
from Bio.Seq import Seq
from io import StringIO
import pandas as pd

st.set_page_config(page_title="SpliceVision", page_icon="🧬", layout="wide")

st.title("🧬 SpliceVision")
st.subheader("Interactive DNA Sequence Analysis Platform")

st.write("""
SpliceVision is an interactive bioinformatics application for exploring DNA sequences. Upload a FASTA file to analyze nucleotide composition, identify canonical splice-site motifs, detect open reading frames (ORFs), and perform DNA transcription and protein translation.
""")

EXAMPLE_FASTA = """>Example_DNA_Sequence
ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAGGTAGCGTATGCGTAGCTAGCTAGCGTAGCTAGCTAGCTAA
"""

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "📂 Upload a FASTA file",
        type=["fasta", "fa", "txt"]
    )

with col2:
    use_example = st.button("🧬 Use Example FASTA")


def clean_sequence(seq):
    """Clean sequence text by removing spaces and converting to uppercase."""
    return str(seq).upper().replace("\n", "").replace(" ", "")


def validate_dna(seq):
    """Check whether the sequence contains only valid DNA bases."""
    return set(seq).issubset(set("ATGCN"))


def gc_content(seq):
    """Calculate GC content percentage."""
    if len(seq) == 0:
        return 0
    return round(((seq.count("G") + seq.count("C")) / len(seq)) * 100, 2)


def at_content(seq):
    """Calculate AT content percentage."""
    if len(seq) == 0:
        return 0
    return round(((seq.count("A") + seq.count("T")) / len(seq)) * 100, 2)


def detect_splice_sites(seq):
    """Detect simple canonical GT donor and AG acceptor motifs."""
    sites = []

    for i in range(len(seq) - 1):
        signal = seq[i:i + 2]

        if signal == "GT":
            sites.append({
                "Type": "Donor site",
                "Signal": "GT",
                "Position": i + 1
            })

        elif signal == "AG":
            sites.append({
                "Type": "Acceptor site",
                "Signal": "AG",
                "Position": i + 1
            })

    return pd.DataFrame(sites)


def find_orfs(seq):
    """Find open reading frames starting with ATG and ending with stop codons."""
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []

    for frame in range(3):
        i = frame

        while i < len(seq) - 2:
            codon = seq[i:i + 3]

            if codon == "ATG":
                for j in range(i + 3, len(seq) - 2, 3):
                    stop = seq[j:j + 3]

                    if stop in stop_codons:
                        orfs.append({
                            "Frame": frame + 1,
                            "Start": i + 1,
                            "End": j + 3,
                            "Length": j + 3 - i,
                            "Stop Codon": stop
                        })
                        break

            i += 3

    return pd.DataFrame(orfs)


if uploaded_file is not None or use_example:
    
    if use_example:
        fasta_text = EXAMPLE_FASTA
    else:
        fasta_text = uploaded_file.read().decode("utf-8")

    records = list(SeqIO.parse(StringIO(fasta_text), "fasta"))

    if len(records) == 0:
        st.error("No FASTA sequence found.")

    else:
        record = records[0]
        sequence = clean_sequence(record.seq)

        st.success("Sequence loaded successfully!")

        if validate_dna(sequence):

            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "📊 Overview",
                "🧬 Composition",
                "🔍 Splice Sites",
                "🧪 ORF Finder",
                "🧬 Transcription & Translation"
            ])

            with tab1:
                st.header("Sequence Information")

                col1, col2, col3 = st.columns(3)

                col1.metric("Sequence ID", record.id)
                col2.metric("Sequence Length", f"{len(sequence)} bases")
                col3.metric("Unknown Bases", sequence.count("N"))

                col4, col5 = st.columns(2)
                col4.metric("GC Content", f"{gc_content(sequence)}%")
                col5.metric("AT Content", f"{at_content(sequence)}%")

                st.subheader("Sequence Preview")
                st.text_area("First 1000 bases", sequence[:1000], height=200)

                if len(sequence) > 1000:
                    st.info("Only the first 1000 bases are shown.")

            with tab2:
                st.header("Nucleotide Composition")

                base_counts = {
                    "A": sequence.count("A"),
                    "T": sequence.count("T"),
                    "G": sequence.count("G"),
                    "C": sequence.count("C"),
                    "N": sequence.count("N")
                }

                base_df = pd.DataFrame({
                    "Base": list(base_counts.keys()),
                    "Count": list(base_counts.values())
                })

                st.dataframe(base_df, use_container_width=True)
                st.bar_chart(base_df.set_index("Base"))

            with tab3:
                st.header("Canonical Splice-Site Detection")

                st.write("""
                This section detects simple canonical splice-site motifs:
                **GT** as a donor signal and **AG** as an acceptor signal.
                """)

                splice_df = detect_splice_sites(sequence)

                if splice_df.empty:
                    st.warning("No GT donor or AG acceptor signals found.")

                else:
                    donor_count = len(splice_df[splice_df["Signal"] == "GT"])
                    acceptor_count = len(splice_df[splice_df["Signal"] == "AG"])

                    col1, col2 = st.columns(2)
                    col1.metric("GT Donor Sites", donor_count)
                    col2.metric("AG Acceptor Sites", acceptor_count)

                    st.dataframe(splice_df, use_container_width=True)

                    st.download_button(
                        label="📥 Download splice-site table as CSV",
                        data=splice_df.to_csv(index=False),
                        file_name="splice_sites.csv",
                        mime="text/csv"
                    )

                    st.info(
                        "Note: This app detects simple GT/AG motifs only. "
                        "Not every GT or AG motif is a true biological splice site."
                    )

            with tab4:
                st.header("Open Reading Frame Finder")

                st.write("""
                This section detects ORFs beginning with **ATG** and ending with
                one of the stop codons: **TAA**, **TAG**, or **TGA**.
                """)

                orf_df = find_orfs(sequence)

                if orf_df.empty:
                    st.warning("No ORFs found.")

                else:
                    st.dataframe(orf_df, use_container_width=True)

                    longest_orf = orf_df.sort_values(
                        "Length",
                        ascending=False
                    ).iloc[0]

                    st.success(
                        f"Longest ORF: Frame {longest_orf['Frame']} | "
                        f"Start {longest_orf['Start']} | "
                        f"End {longest_orf['End']} | "
                        f"Length {longest_orf['Length']} bp"
                    )

                    st.download_button(
                        label="📥 Download ORF table as CSV",
                        data=orf_df.to_csv(index=False),
                        file_name="orfs.csv",
                        mime="text/csv"
                    )

            with tab5:
                st.header("DNA Transcription and Protein Translation")

                clean_dna = sequence.replace("N", "")
                dna_seq = Seq(clean_dna)

                rna_seq = dna_seq.transcribe()
                protein_seq = dna_seq.translate(to_stop=False)

                st.subheader("RNA Sequence Preview")
                st.text_area("First 1000 RNA bases", str(rna_seq[:1000]), height=150)

                st.subheader("Protein Sequence Preview")
                st.text_area("First 1000 amino acids", str(protein_seq[:1000]), height=150)

                st.metric("Protein Length", f"{len(protein_seq)} amino acids")

        else:
            st.error("Invalid DNA sequence. Use only A, T, G, C, or N.")

else:
    st.info("Load the demo sequence or upload a FASTA file to begin.")