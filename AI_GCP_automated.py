import re
from diagrams import Diagram
from diagrams.gcp.storage import Storage
from diagrams.gcp.analytics import BigQuery, Composer
from diagrams.gcp.database import SQL
from diagrams.gcp.devtools import Build
from diagrams.gcp.operations import Monitoring

# Map keywords to diagrams node classes
SERVICE_MAP = {
    "gcs": Storage,
    "google cloud storage": Storage,
    "bigquery": BigQuery,
    "bq": BigQuery,
    "composer": Composer,
    "airflow": Composer,
    "sql": SQL,
    "build": Build,
    "monitoring": Monitoring
}

def extract_services(prompt):
    found = {}
    for k, cls in SERVICE_MAP.items():
        if k in prompt:
            found[k] = cls
    return found

def extract_relations(prompt, found_nodes):
    edges = []
    # Detect common relationships
    rel_patterns = [
        r'(\w+)\s+(loaded into|sent to|written to|imported into|uploaded to)\s+(\w+)',
        r'(\w+)\s+(orchestrated using|controlled by|triggered by|handled by)\s+(\w+)'
    ]
    for phrase in rel_patterns:
        for match in re.finditer(phrase, prompt):
            a, _, b = match.groups()
            node_a = next((n for k, n in found_nodes.items() if a in k), None)
            node_b = next((n for k, n in found_nodes.items() if b in k), None)
            if node_a and node_b:
                edges.append((node_a, node_b))
    return edges

def generate_diagram_from_prompt(prompt):
    prompt = prompt.lower()
    found_classes = extract_services(prompt)
    nodes = {}

    with Diagram("Auto GCP Architecture", show=True):
        # Instantiate nodes inside context
        for k, cls in found_classes.items():
            nodes[k] = cls(k.title())
        # Draw edges dynamically
        edges = extract_relations(prompt, nodes)
        for src, dst in edges:
            src >> dst
        # Optionally show isolated nodes
        if not edges:
            for n in nodes.values():
                pass  # diagram will show single nodes

if __name__ == "__main__":
    user_prompt = input("Enter your architecture prompt:\n")
    generate_diagram_from_prompt(user_prompt)
