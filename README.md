# 🏥 Drug Interaction Detection System

An AI-powered healthcare application that helps identify potential drug-drug interactions and provides clinically relevant information through an interactive Streamlit web interface.

## 🚀 Project Overview

Drug interactions can lead to serious adverse effects when medications are taken together. This project allows users to select two drugs and instantly view:

* Interaction Severity
* Mechanism of Interaction
* Clinical Effects
* Safer Alternatives
* Clinical Management Recommendations
* Reference Sources

The system uses a structured Drug-Drug Interaction (DDI) database and provides an intuitive healthcare dashboard for quick analysis.

---

## ✨ Features

### 🔍 Drug Interaction Search

Select any two drugs and check whether an interaction exists.

### ⚠️ Severity Detection

Interactions are classified as:

* 🔴 Major
* 🟠 Moderate
* 🟢 Minor

### 🧬 Mechanism Analysis

Displays the pharmacological mechanism responsible for the interaction.

### 🩺 Clinical Effects

Shows possible patient outcomes and risks.

### ✅ Safer Alternatives

Provides alternative medication suggestions when available.

### 📋 Clinical Management

Displays recommended clinical actions and monitoring strategies.

### 📚 References

Includes source references for interaction information.

---

## 🛠️ Tech Stack

* Python
* Pandas
* Streamlit
* JSON Data Processing
* ast.literal_eval()
* pd.json_normalize()

---

## 📊 Data Processing Pipeline

Raw DDI Dataset (JSON)
↓
ast.literal_eval()
↓
pd.json_normalize()
↓
Structured DataFrame
↓
Drug Interaction Search Engine
↓
Streamlit User Interface

---

## 🧠 Key Concepts Used

### Data Processing

* JSON Parsing
* Data Normalization
* Feature Extraction

### Data Analysis

* Pandas DataFrames
* Data Cleaning
* Data Transformation

### Web Development

* Streamlit Components
* Interactive Dropdowns
* Dynamic Result Rendering

### Search Logic

The application supports bidirectional drug matching:

Drug A + Drug B

and

Drug B + Drug A

produce the same interaction result.

---

## 📂 Project Structure

Drug-Interaction-Detection-System/

├── app.py

├── drug_interactions.csv

├── requirements.txt

├── README.md

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

Add your deployed Streamlit link here:




---

## 💻 Author

Mubarak Naikwade

Computer Science Engineering Student

Interested in:

* Machine Learning
* Computer Vision
* Healthcare AI
* Data Science

---

## ⭐ Future Improvements

* Machine Learning-based severity prediction
* Drug recommendation engine
* Multi-drug interaction analysis
* User authentication
* Interaction history tracking
* Clinical risk scoring system

---

If you found this project useful, consider giving it a ⭐ on GitHub.
