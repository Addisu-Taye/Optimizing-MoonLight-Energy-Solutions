**Prepared for:** MoonLight Energy Solutions  
**Prepared by:** Addisu Taye, Analyst  
**Date:** May 21, 2025  

# ☀️ Solar Irradiance Analysis Report  

---

## Table of Contents  
1. [Executive Summary](#1-executive-summary)  
2. [Introduction](#2-introduction)  
3. [MoonLight Business Objective](#3-moonlight-business-objective)  
4. [Data Cleaning and Profiling](#4-data-cleaning-and-profiling)  
   - [4.1 Benin (Malanville)](#41-benin-malanville)  
   - [4.2 Sierra Leone (Bumbuna)](#42-sierra-leone-bumbuna)  
   - [4.3 Togo (Dapaong)](#43-togo-dapaong)  
5. [Cross-Country Comparison](#5-cross-country-comparison)  
6. [Recommendations](#6-recommendations)  

---

## 1. Executive Summary  
This report evaluates solar irradiance data from three West African locations to identify the optimal site for MoonLight Energy Solutions’ solar farm investment.

### 🔍 Key Findings:
- 🌞 **Benin (Malanville)** has the highest average GHI (**235.93 W/m²**).
- 🟡 **Togo (Dapaong)** is the next best (GHI: **223.38 W/m²**).
- 💧 **Sierra Leone (Bumbuna)** has the lowest irradiance but significantly higher relative humidity (**RH: 79.87%**).

**📌 Recommendation:** Prioritize **Benin** as the pilot investment location for a solar farm.

---

## 2. Introduction  
West Africa holds untapped potential for solar energy. This analysis explores irradiance patterns across three countries to support evidence-based investment in renewable energy infrastructure.

---

## 3. MoonLight Business Objective  
MoonLight Energy Solutions aims to expand its renewable energy portfolio by deploying scalable solar infrastructure in regions with optimal sunlight exposure and moderate atmospheric variability.

---

## 4. Data Cleaning and Profiling  

### 4.1 Benin (Malanville)  

**Table 4.1: Summary Statistics for Benin**  

| Feature     | Mean    | Max     | Std     |  
|-------------|---------|---------|---------|  
| GHI (W/m²)  | 235.93  | 1233.00 | 328.13  |  
| Tamb (°C)   | 28.15   | 43.80   | 5.93    |  

**Figure 4.1:** GHI and Temperature Trends  
![Benin Trend](https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/benin_ghi_trend.png)

**Figure 4.2:** Correlation Heatmap  
![Benin Correlation](https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/benin_correlation.png)

---

### 4.2 Sierra Leone (Bumbuna)  

**Table 4.2: Summary Statistics for Sierra Leone**  

| Feature     | Mean    |  
|-------------|---------|  
| GHI (W/m²)  | 180.42  |  
| RH (%)      | 79.87   |  

**Figure 4.3:** GHI Histogram  
![Sierra GHI Histogram](https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/sierra_histogram.png)

---

### 4.3 Togo (Dapaong)  

**Table 4.3: Summary Statistics for Togo**  

| Feature     | Mean    | Max     |  
|-------------|---------|---------|  
| GHI (W/m²)  | 223.38  | 1201.00 |  

---

## 5. Cross-Country Comparison  

**Figure 5.1:** GHI Comparison Across Countries  
![GHI Comparison](https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/ghi_comparison_chart.png)

### Key Insight:
📈 **Benin’s GHI is ~30.8% higher** than Sierra Leone’s, making it a more viable site in terms of solar resource availability.

---

## 6. Recommendations  

✅ **Primary Site Recommendation:**  
- **Benin (Malanville)** — highest irradiance, consistent solar exposure.

📋 **Next Steps:**  
1. Conduct **feasibility study** for land, water, and grid access.  
2. Initiate **pilot farm installation** with real-time monitoring.  
3. Collect annual irradiance data to validate long-term performance.  
4. Assess scalability for neighboring Togo if Benin succeeds.  

---
## 📸 Streamlit App Screenshot

![Streamlit Screenshot](https://raw.githubusercontent.com/Addisu-Taye/Optimizing-MoonLight-Energy-Solutions/main/data/streamlit.png)
*For questions or deeper analysis, contact: [Addisu Taye](mailto:addtaye@gmail.com)*  
