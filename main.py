import re
from collections import Counter
from pathlib import Path

def normalize_error(line: str) -> str:
    # Strip timestamp and dynamic IDs (e.g., tx_id=99102 -> tx_id=*) so recurring errors cluster cleanly
    msg = re.sub(r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+", "", line.strip())
    msg = re.sub(r"=\d+", "=*", msg)
    return msg

def generate_digest(log_path: str) -> str:
    lines = Path(log_path).read_text(encoding="utf-8").splitlines()
    errors = [normalize_error(l) for l in lines if " ERROR " in l]
    counts = Counter(errors)

    report = [
        "# Daily Log & Error Digest",
        f"- **Total Lines Scanned:** {len(lines)}",
        f"- **Total Errors Found:** {len(errors)}",
        f"- **Unique Error Signatures:** {len(counts)}\n",
        "## Top Recurring Issues",
    ]
    for idx, (sig, count) in enumerate(counts.most_common(), 1):
        report.append(f"{idx}. **[{count}x]** `{sig}`")
    return "\n".join(report)

if __name__ == "__main__":
    print(generate_digest("sample.log"))