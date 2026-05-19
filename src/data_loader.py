from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain_community.document_loaders import Docx2txtLoader, JSONLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader

def load_all_documents(data_dir:str)->List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structure
    Supported: PDF, TXT, CSV till now. To be added - Excel, Word, JSON
    """

    # Use project root data folder
    data_path=Path(data_dir).resolve()
    print(f"[DEBUG] Data Path: {data_path}")
    documents = []

    # ---------------- PDF Files ---------------
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF Files: {[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} PDF docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[Error] Failed to load PDF {pdf_file}: {e}")
    
    

    # ---------------- TXT Files ----------------
    txt_files = list(data_path.glob("**/*.txt"))
    print(f"[DEBUG] Found {len(txt_files)} TXT files")

    for txt_file in txt_files:
        try:
            loader = TextLoader(str(txt_file), encoding="utf-8")
            loaded = loader.load()
            documents.extend(loaded)
            print(f"[INFO] Loaded TXT: {txt_file}")
        except Exception as e:
            print(f"[ERROR] Failed TXT {txt_file}: {e}")
            
    # ---------------- CSV Files ----------------
    csv_files = list(data_path.glob("**/*.csv"))
    print(f"[DEBUG] Found {len(csv_files)} CSV files")

    for csv_file in csv_files:
        try:
            loader = CSVLoader(str(csv_file))
            loaded = loader.load()
            documents.extend(loaded)
            print(f"[INFO] Loaded CSV: {csv_file}")
        except Exception as e:
            print(f"[ERROR] Failed CSV {csv_file}: {e}")

    return documents

    