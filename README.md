# Replicating Temperature Anomalies Graphics

**STAT 159/259 — Project 1**

## Overview

This project replicates four graphics showing global surface temperature anomalies. Three of the graphics are based on figures published by NASA's Goddard Institute for Space Studies (GISS) as part of the GISTEMP v4 data product. The fourth reproduces the *New York Times* chart from the article *“It's Official: 2018 Was the Fourth-Warmest Year on Record”* (Schwartz and Popovich, February 6, 2019), which is a modified version of one of the NASA graphics.

The data are downloaded from the official NASA GISTEMP v4 data server using `scripts/download_data.py`. Each figure is reproduced in a separate Jupyter notebook, and the resulting graphics are exported in both PNG and PDF formats to `outputs/`.

## Repository Structure

```text
temperature-anomalies/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── land_ocean_anomalies.csv
│   ├── seasonal_cycle.csv
│   └── global_annual_mean.csv
├── scripts/
│   ├── download_data.py
│   ├── 01_land_ocean_anomalies.ipynb
│   ├── 02_seasonal_cycle.ipynb
│   ├── 03_global_annual_mean.ipynb
│   └── 04_nyt_chart.ipynb
├── outputs/
│   ├── graphic1_land_ocean_anomalies.png
│   ├── graphic1_land_ocean_anomalies.pdf
│   ├── graphic2_seasonal_cycle.png
│   ├── graphic2_seasonal_cycle.pdf
│   ├── graphic3_global_annual_mean.png
│   ├── graphic3_global_annual_mean.pdf
│   ├── graphic4_nyt_rising_global_temperature.png
│   └── graphic4_nyt_rising_global_temperature.pdf
└── report/
    └── report.md
```

## Data

| File | Used for | Contents |
| --- | --- | --- |
| `data/land_ocean_anomalies.csv` | Graphic 1 | Annual temperature anomalies over land and ocean, together with lowess smoothings, relative to the 1951–1980 mean |
| `data/seasonal_cycle.csv` | Graphic 2 | Monthly temperature anomalies since 1880, relative to the 1980–2015 base period |
| `data/global_annual_mean.csv` | Graphics 3 and 4 | Annual global mean temperature anomalies and 5-year lowess smoothing, relative to the 1951–1980 mean |

Data source: NASA GISS, GISTEMP v4 — <https://data.giss.nasa.gov/gistemp/graphs_v4/>

## Replicated Graphics

### Graphic 1 — Temperature Anomalies over Land and over Ocean

![Temperature anomalies over land and over ocean](outputs/graphic1_land_ocean_anomalies.png)

This figure compares annual mean land surface air temperature and sea surface water temperature anomalies relative to the 1951–1980 mean. The annual series and their 5-year lowess smoothings are reproduced from the NASA graphic.

### Graphic 2 — GISTEMP Seasonal Cycle since 1880

![GISTEMP seasonal cycle since 1880](outputs/graphic2_seasonal_cycle.png)

This figure shows monthly global surface temperature anomalies for each year since 1880. Years are grouped by color across 20-year periods, with the partial 2026 series shown separately.

### Graphic 3 — Global Mean Estimates based on Land and Ocean Data

![Global mean estimates based on land and ocean data](outputs/graphic3_global_annual_mean.png)

This figure reproduces the annual global mean surface temperature anomaly series together with the 5-year lowess smoothing.

**Documented deviation:** the official NASA graphic includes a light-grey *LSAT+SST Uncertainty* band. The values for that band are not included in the `graph.csv` file distributed with the graphic, so the band is omitted here.

### Graphic 4 — The New York Times “Rising Global Temperature”

![NYT rising global temperature](outputs/graphic4_nyt_rising_global_temperature.png)

This figure reproduces the *New York Times* chart published on February 6, 2019. It uses the NASA global annual mean series but expresses values relative to the 1880–1899 average and restricts the displayed data to 1880–2018 to match the original article.

## Reproducing the Project

From the repository root, create a virtual environment and install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Download the NASA GISTEMP data:

```bash
python scripts/download_data.py
```

Execute all four notebooks:

```bash
jupyter nbconvert --execute --inplace scripts/*.ipynb
```

Running the notebooks regenerates the figures in `outputs/` in PNG and PDF formats.

## Requirements

The project uses Python with the packages listed in `requirements.txt`, including:

- pandas
- NumPy
- Matplotlib
- JupyterLab
- nbformat
- nbconvert
- ipykernel

## Report

A fuller description of the replication, the individual figures, and the documented deviations is available in [`report/report.md`](report/report.md).

## References

- GISTEMP Team. *GISS Surface Temperature Analysis (GISTEMP), version 4*. NASA Goddard Institute for Space Studies. <https://data.giss.nasa.gov/gistemp/>
- Lenssen, N., Schmidt, G., Hansen, J., Menne, M., Pershing, A., Ruedy, R., & Schlinger, D. (2019). *Improvements in the GISTEMP uncertainty model*. Journal of Geophysical Research: Atmospheres, 124(12), 6307–6326.
- Schwartz, J., & Popovich, N. (2019, February 6). *It's Official: 2018 Was the Fourth-Warmest Year on Record*. The New York Times.
