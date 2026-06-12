# 🧼 BytePolish

[![Streamlit App](https://streamlit.io)](https://data-clean-visualise.streamlit.app/)
[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

An interactive data cleaning and type-safe analytics pipeline built with **Streamlit**, **Pandas**, and **Plotly**. This application features persistent session-state management, automated column-schema filtering, and memory-optimized UI downsampling to handle your data preparation workflows seamlessly.

👉 **[Access the Live Application Here](https://data-clean-visualise.streamlit.app/)**
---

## 🚀 Features

### 🛠️ Data Cleaning Core
* **Drop Duplicates:** Instantly remove identical rows from your dataset in one click.
* **Filter Missing Values:** Identify and purge `None`, `NaN`, or null values across your dataset.
* **Delete Columns:** Drop unnecessary or redundant columns to minimize memory footprint.
* **Convert Data Types:** Cast columns into type-safe formats (e.g., Categorical, DateTime, Numeric) with runtime validation.

### 📊 Interactive Visualizations (Powered by Plotly)
* **Scatter Plots:** Uncover relationships, correlations, and outliers between continuous variables.
* **Bar Charts:** Aggregate and compare categorical distributions.
* **Histograms:** Inspect data frequency, distribution curves, and skewness.

### ⚙️ Pipeline & State Management
* **State Persistence:** Built-on Streamlit Session State to keep your cleaning steps saved across user interactions.
* **Memory-Optimized Downsampling:** Smart UI rendering for large datasets to prevent browser lag.
* **Instant Refresh:** A dedicated reset/refresh mechanism to reload the pipeline or start fresh.
* **Cleaned Data Export:** Download your processed, type-safe dataset as a production-ready CSV instantly.

---

## 🛠️ Tech Stack

* **Frontend Framework:** [Streamlit](https://streamlit.io) (Data-centric UI rendering)
* **Data Processing:** [Pandas](https://pydata.org) (High-performance dataframe manipulation)
* **Data Visualization:** [Plotly Express](https://plotly.com) (Interactive, responsive charting)

---


## 💡 Usage Workflow

1. **Upload:** Drop your messy CSV or Excel file into the sidebar uploader.
2. **Clean:** Drop duplicates, strip nulls, and explicitly cast your column data types.
3. **Analyze:** Switch to the visualization tab to generate interactive scatter, bar, or histogram plots.
4. **Export:** Click the download button to grab your fully polished, structured data.
