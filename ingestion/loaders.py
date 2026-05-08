from pathlib import Path

def load_department_docs(department: str):

    base_path = Path(r"C:\Users\sande\GitHub projects\project5.1(RAG)\docs")

    folder = base_path / department

    for path in folder.rglob("*.md"):
        text = path.read_text(encoding="utf-8")

        yield {
            "text": text,
            "metadata": {
                "department": department,
                "source": str(path)
            }
        }


