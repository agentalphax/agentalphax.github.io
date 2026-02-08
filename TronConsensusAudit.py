import os
import re

# Agent Alpha - Blockchain Consensus Auditor Tool
def audit_consensus_logic(directory):
    vulnerabilities = {
        "Integer Overflow": r"(\w+)\s*\+=\s*(\w+)",
        "Floating Point Usage": r"(float|double)",
        "Missing Boundary Check": r"if\s*\((.*)\)\s*\{",
    }
    
    print(f"[!] Starting Audit in: {directory}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                    for name, pattern in vulnerabilities.items():
                        if re.search(pattern, content):
                            print(f"[FOUND] {name} risk in {file}")

if __name__ == "__main__":
    audit_consensus_logic("./")
