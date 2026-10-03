#!/usr/bin/env python3
"""Download the NASA GISTEMP v4 data used in this project.

The script downloads the CSV files behind the GISTEMP v4 graphics analysed in
this repository and stores them in the data/ folder at the root of the
project. The CSVs are the official data files published at
https://data.giss.nasa.gov/gistemp/graphs_v4/ .

The download is first attempted with Python's standard library. If the local
Python was compiled against an old SSL library that cannot negotiate with the
server (this happens with the system Python on some macOS versions), the
script automatically falls back to the curl command-line tool.

Usage (from the repository root):

    python scripts/download_data.py
"""

import shutil
import subprocess
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlretrieve

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

BASE_URL = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data"

FILES = {
    "land_ocean_anomalies.csv": (
        f"{BASE_URL}/Temperature_Anomalies_over_Land_and_over_Ocean/graph.csv"
    ),
    "seasonal_cycle.csv": (
        f"{BASE_URL}/GISTEMP_Seasonal_Cycle_since_1880/graph.csv"
    ),
    "global_annual_mean.csv": (
        f"{BASE_URL}/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv"
    ),
}


def download(url, destination):
    """Download url to destination, falling back to curl if needed."""
    try:
        urlretrieve(url, destination)
    except (URLError, OSError) as error:
        if shutil.which("curl") is None:
            raise SystemExit(f"Could not download {url}: {error}")
        subprocess.run(
            ["curl", "--fail", "--silent", "--show-error", "--location",
             "-o", str(destination), url],
            check=True,
        )


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for filename, url in FILES.items():
        destination = DATA_DIR / filename
        print(f"Downloading {filename} ...", end=" ", flush=True)
        download(url, destination)
        size_kb = destination.stat().st_size / 1024
        print(f"done ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
