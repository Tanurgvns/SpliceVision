import streamlit as st
from Bio import SeqIO
from io import StringIO
import pandas as pd

st.set_page_config(page_title="SpliceVision", page_icon="🧬", layout="wide")

st.title("🧬 SpliceVision")
st.subheader("Interactive Gene Splicing Analyzer")

st.write("""
Welcome to **SpliceVision**!

This app analyzes DNA FASTA files and detects basic splice-site signals.
""")

uploaded_file = st.file_uploader("📂 Upload a FASTA file", type=["fasta", "fa", "txt"])


def clean_sequence(seq):
    return str(seq).upper().replace("\n", "").replace(" ", "")


def validate_dna(seq):
    valid_bases = set("ATGCN")
    return set(seq).issubset(valid_bases)


def gc_content(seq):
    if len(seq) == 0:
        return 0
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)


def detect_splice_sites(seq):
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

    return sites


if uploaded_file is not None:
    fasta_text = uploaded_file.read().decode("utf-8")
    records = list(SeqIO.parse(StringIO(fasta_text), "fasta"))

    if len(records) == 0:
        st.error("No FASTA sequence found.")
    else:
        record = records[0]
        sequence = clean_sequence(record.seq)

        st.success("FASTA file uploaded successfully!")

        st.header("1. Sequence Information")

        st.write(f"**Sequence ID:** {record.id}")
        st.write(f"**Sequence Length:** {len(sequence)} bases")

        if validate_dna(sequence):
            st.success("Valid DNA sequence")

            gc = gc_content(sequence)
            at = round(100 - gc, 2)

            base_counts = {
                "A": sequence.count("A"),
                "T": sequence.count("T"),
                "G": sequence.count("G"),
                "C": sequence.count("C"),
                "N": sequence.count("N")
            }

            col1, col2, col3 = st.columns(3)
            col1.metric("GC Content", f"{gc}%")
            col2.metric("AT Content", f"{at}%")
            col3.metric("Unknown Bases", base_counts["N"])

            st.header("2. Nucleotide Composition")

            base_df = pd.DataFrame({
                "Base": list(base_counts.keys()),
                "Count": list(base_counts.values())
            })

            st.dataframe(base_df, use_container_width=True)
            st.bar_chart(base_df.set_index("Base"))

            st.header("3. Sequence Preview")

            st.text_area("DNA Sequence", sequence[:1000], height=200)

            if len(sequence) > 1000:
                st.info("Only the first 1000 bases are shown.")

            st.header("4. Basic Splice-Site Detection")

            splice_sites = detect_splice_sites(sequence)

            if len(splice_sites) == 0:
                st.warning("No GT donor or AG acceptor signals found.")
            else:
                splice_df = pd.DataFrame(splice_sites)

                donor_count = len(splice_df[splice_df["Signal"] == "GT"])
                acceptor_count = len(splice_df[splice_df["Signal"] == "AG"])

                col1, col2 = st.columns(2)
                col1.metric("GT Donor Sites", donor_count)
                col2.metric("AG Acceptor Sites", acceptor_count)

                st.subheader("Detected Splice-Site Signals")
                st.dataframe(splice_df, use_container_width=True)

                csv = splice_df.to_csv(index=False)

                st.download_button(
                    label="Download splice-site table as CSV",
                    data=csv,
                    file_name="splice_sites.csv",
                    mime="text/csv"
                )

                st.info(
                    "Note: This detects simple GT/AG motifs. "
                    "Not every GT or AG is a true biological splice site."
                )

        else:
            st.error("Invalid DNA sequence. Use only A, T, G, C, or N.")

else:
    st.info("Please upload a FASTA file to begin.")