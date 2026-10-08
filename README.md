# Geopolitical Risk, Energy Prices and Macro-Financial Transmission in the Euro Area

Reproducible research repository for the MSc thesis **“Heterogeneity in Geopolitical Risk Shocks, Energy Prices and Macro-Financial Transmission in the Euro Area.”**

## Research question

Does the geographical origin of geopolitical risk affect its transmission through energy prices and macro-financial variables across euro-area economies?

The empirical design estimates **16 Bayesian VAR systems**: four recipient economies (Germany, France, Italy and Spain) × four GPR origins (Russia, China, MENA and Western).

## Empirical design

The baseline recursive ordering is:

`[GPR, Brent, Gas, HICP, IPI, CLIFS]`

The BVAR uses two lags, a Minnesota prior and recursive Cholesky identification. Structural impulse responses are summarised using posterior medians and 68% credible intervals. The quarterly data skeleton covers **1997Q1–2025Q4** and the transformed estimation sample starts in **1997Q2**.

Transformations are `log(1+GPR)`, first log differences of Brent, Gas, HICP and IPI, and CLIFS in levels. COVID-era volatility is handled with a truncated-volatility specification estimated before the production BVAR stage; the estimated volatility parameters are then frozen and reused downstream.

## Main findings

- Gas responses are negative on impact in all 16 baseline median responses; 9 are credibly different from zero at the 68% level.
- Brent responses are heterogeneous across shock origins.
- HICP responses are frequently positive, especially for several Russia- and China-origin shocks.
- IPI responses are mixed across economies and horizons.
- CLIFS responses are predominantly negative at one- and two-year horizons.
- An exact 256-assignment permutation test finds an unusually high concentration of detectable responses for Russian-origin shocks in the baseline: **23/40, p = 0.0273**. This concentration does not survive the levels specification.

The permutation test concerns the concentration of detectable responses across origins; it does not invalidate responses associated with other origins.

## Repository structure

```text
.
├── README.md
├── LICENSE.md
├── requirements.txt
├── notebooks/
│   ├── 01_data_inspection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_transformations_stationarity.ipynb
│   ├── 04_covid_volatility.ipynb
│   ├── 05_bvar_main_results.ipynb
│   ├── 06_robustness.ipynb
│   └── 07_model_validation.ipynb
├── src/
│   ├── __init__.py
│   └── paths.py
├── data/
│   ├── README.md
│   ├── raw/
│   └── processed/
├── outputs/
└── paper/
```

## Execution order

1. **Data inspection** — inspects the raw source files, records import decisions and creates the quarterly skeleton.
2. **Data cleaning** — cleans and harmonises the raw series, seasonally adjusts monthly HICP and constructs the clean quarterly panel.
3. **Transformations & stationarity** — applies the final transformations, reports dynamic diagnostics and exports the BVAR-ready panel.
4. **COVID volatility** — estimates the truncated COVID-volatility parameters used by the production models.
5. **BVAR main results** — estimates the 16 baseline systems, structural IRFs, synthesis tables and exact permutation test.
6. **Robustness** — evaluates reduced systems, alternative recursive orderings/sample windows, covariance-prior sensitivity and levels specifications.
7. **Model validation** — uses synthetic data to test known-truth recovery, covariance-prior scale sensitivity and Monte Carlo interval coverage.

There is **no classical VAR empirical specification** in the public analysis. The classical residual bootstrap appearing in notebook 07 is used only as a numerical validation benchmark on synthetic data.

## Reproducibility

Clone the repository, place the expected source files under `data/raw/` as described in [`data/README.md`](data/README.md), and install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the notebooks in numerical order from the repository root or from `notebooks/`. Paths are repository-relative; no personal Google Drive path is required.

Notebook 02 uses `rpy2` to call **RJDemetra/JDemetra+** for the final HICP seasonal adjustment. A working R installation and the R package `RJDemetra` are therefore required for that step.

Generated processed data and outputs are intentionally excluded from version control. They are reconstructed by running the pipeline.

## Validation status

The seven public notebooks have been executed without saved execution errors in the final research workflow. The rebuilt production notebooks reproduce the defended thesis results, including the 16 baseline BVARs and the robustness summaries.

The synthetic validation in notebook 07 obtains 90% interval coverage of **92% at impact and 90% at one year for the BVAR**, compared with **89% and 85%** for the classical residual-bootstrap benchmark.

## Thesis

The final MSc thesis is included under `paper/` when distributed with the repository.

## Author

Jaime Rodríguez  
MSc in Economics with Data Science — Universidad de Alicante
