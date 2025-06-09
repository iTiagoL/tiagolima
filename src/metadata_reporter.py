import os
from typing import List, Dict

import requests
from docx import Document


def fetch_denodo_metadata(host: str, username: str, password: str) -> List[Dict[str, str]]:
    """Fetch metadata information from Denodo.

    This function uses a simplified example of calling a Denodo REST API.
    In a real scenario, you would adjust the endpoints and authentication
    method according to your Denodo installation.
    """
    # Placeholder implementation -- replace with actual API calls
    # For demonstration, return sample metadata
    return [
        {"database": "example_db", "view": "customer", "description": "Customer data"},
        {"database": "example_db", "view": "orders", "description": "Orders data"},
    ]


def generate_word_report(metadata: List[Dict[str, str]], output_path: str) -> None:
    """Generate a Word report from metadata."""
    document = Document()
    document.add_heading("Denodo Metadata Report", level=1)

    for item in metadata:
        document.add_heading(f"{item['database']}.{item['view']}", level=2)
        document.add_paragraph(item.get("description", "No description"))

    document.save(output_path)


if __name__ == "__main__":
    host = os.getenv("DENODO_HOST", "localhost")
    user = os.getenv("DENODO_USER", "admin")
    password = os.getenv("DENODO_PASSWORD", "admin")
    output = "denodo_report.docx"

    metadata = fetch_denodo_metadata(host, user, password)
    generate_word_report(metadata, output)
    print(f"Report saved to {output}")
