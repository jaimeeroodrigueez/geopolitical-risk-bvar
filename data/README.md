# Data

This project combines bilateral geopolitical-risk indicators with energy prices and euro-area macro-financial data.

## Expected raw files

Place the source files under `data/raw/` using the following structure:

- `gpr/GPR_DBGlobal_Bilateral.xlsx`  
- `energy/Brent_and_Gas_Prices.xlsx`  
- `hicp/HICP_CoreHICP_EnergyHICP.xlsx`  
- `ipi/IPI.xlsx`  
- `gdp/GDP.xlsx`  
- `clifs/CLIFS.xlsx`

The thesis uses bilateral GPR indices from Banco de España, Brent and European natural-gas prices from the World Bank, HICP/IPI/GDP series from Eurostat, and CLIFS from the ECB.

## Sample and variables

The quarterly skeleton covers **1997Q1–2025Q4**. The first quarter is retained to construct log differences, so the transformed estimation sample begins in **1997Q2**.

**Recipient economies:** Germany, France, Italy and Spain.   
**GPR origins:** Russia, China, Middle East (MENA) and Western Bloc.

The baseline BVAR uses `[GPR, Brent, Gas, HICP, IPI, CLIFS]`. 

GDP is retained only for the descriptive GDP-versus-IPI comparison used to motivate the baseline activity indicator. Energy prices remain in USD throughout the public pipeline; no exchange-rate series is required.
