"""Central repository paths and shared empirical settings."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
SRC_DIR = PROJECT_ROOT / "src"
PAPER_DIR = PROJECT_ROOT / "paper"

RAW_GPR_DIR = RAW_DATA_DIR / "gpr"
RAW_ENERGY_DIR = RAW_DATA_DIR / "energy"
RAW_HICP_DIR = RAW_DATA_DIR / "hicp"
RAW_IPI_DIR = RAW_DATA_DIR / "ipi"
RAW_GDP_DIR = RAW_DATA_DIR / "gdp"
RAW_CLIFS_DIR = RAW_DATA_DIR / "clifs"

RAW_FILES = {
    "gpr": RAW_GPR_DIR / "GPR_DBGlobal_Bilateral.xlsx",
    "energy": RAW_ENERGY_DIR / "Brent_and_Gas_Prices.xlsx",
    "hicp": RAW_HICP_DIR / "HICP_CoreHICP_EnergyHICP.xlsx",
    "ipi": RAW_IPI_DIR / "IPI.xlsx",
    "gdp": RAW_GDP_DIR / "GDP.xlsx",
    "clifs": RAW_CLIFS_DIR / "CLIFS.xlsx",
}

IMPORT_DECISIONS_PATH = PROCESSED_DATA_DIR / "01_import_decisions.xlsx"
SKELETON_PATH = PROCESSED_DATA_DIR / "02_master_quarterly_skeleton.xlsx"
CLEAN_QUARTERLY_PANEL_PATH = PROCESSED_DATA_DIR / "03_clean_quarterly_panel.xlsx"
BVAR_READY_PANEL_PATH = PROCESSED_DATA_DIR / "03_bvar_ready_panel.xlsx"

COVID_OUTPUT_DIR = OUTPUT_DIR / "04_covid_volatility"
COVID_THETA_PATH = COVID_OUTPUT_DIR / "PRODUCTION_covid_theta_mle.csv"
COVID_SCALE_PATHS_PATH = COVID_OUTPUT_DIR / "PRODUCTION_covid_scale_paths.csv"

TARGET_COUNTRIES = ["Germany", "France", "Italy", "Spain"]
GPR_ORIGINS = ["Russia", "China", "Middle East", "Western Bloc"]
START_QUARTER = "1997Q1"
ESTIMATION_START_QUARTER = "1997Q2"
END_QUARTER = "2025Q4"


def ensure_output_directories() -> None:
    """Create standard generated-data and output directories when absent."""
    for path in (PROCESSED_DATA_DIR, OUTPUT_DIR):
        path.mkdir(parents=True, exist_ok=True)
