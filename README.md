# FloodGuard Nigeria 🌧️

## AI-Powered Flood Risk Classifier

FloodGuard Nigeria is an AI/ML project that classifies flood-impact risk across selected Nigerian Local Government Areas (LGAs).

The project combines historical flood-impact data, rainfall indicators and population data to classify an LGA as **Low, Medium or High risk**.

## Why I Built This

Flooding affects many communities across Nigeria, resulting in displacement, loss of livelihoods and other humanitarian impacts.

I wanted to explore how machine learning and publicly available data could be used to create a simple tool that helps identify areas with higher flood-impact risk.

## Data Sources

The project uses data from:

- Humanitarian Data Exchange (HDX)
- NEMA flood-impact records
- Subnational rainfall data
- LGA population data

The datasets were cleaned and joined using Nigerian administrative PCODEs.

The final modelling dataset contains **40 LGAs and 15 features**.

## Features Used

The model uses rainfall and population-related features, including:

- Average and maximum 10-day rainfall
- Average and maximum 1-month rainfall
- Average and maximum 3-month rainfall
- Rainfall anomalies
- Rainfall variability
- 90th percentile rainfall
- Extreme rainfall days
- Log-transformed population

## Machine Learning

I tested three classification models:

- Logistic Regression
- Random Forest
- Decision Tree

Logistic Regression produced the best results on the test set and was selected as the final model.

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 50.0% | 55.4% | 48.9% | 47.8% |
| Random Forest | 42.5% | 44.1% | 40.0% | 39.0% |
| Decision Tree | 32.5% | 28.3% | 30.0% | 27.5% |

Because the modelling dataset is relatively small, these results should be interpreted as a prototype evaluation rather than production-level performance.

## Application

The application was built with Streamlit.
[Open FloodGuard Nigeria](https://floodguard-nigeria-gheflzp6g4vmxwxetruppe.streamlit.app/)

A user can:

1. Select a state
2. Select an LGA
3. Run the flood-risk analysis
4. View the predicted risk level
5. View rainfall and population indicators
6. View historical flood-impact information

## Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- GitHub


## Project Files

```text
app.py
flood_risk_classifier.pkl
floodguard_lga_data.csv
model_features.json
requirements.txt
README.md

```
## Demo Video

[Watch the FloodGuard Nigeria Demo](https://drive.google.com/file/d/1CfRtEgFTeu5UN2LrWV5NnZUZhYVvMJDE/view?usp=sharing)

## Limitations

This is an AI/ML prototype developed using a relatively small dataset covering 40 LGAs.

The model uses historical data and should not be considered a replacement for official flood warnings or emergency management systems.

## Future Improvements

Future versions could include:

- More LGAs and historical flood records
- Real-time rainfall data
- Satellite imagery
- Elevation and drainage data
- Soil and land-use information
- More advanced machine learning models
- Explainable AI
- Wider geographic coverage

## Project

**FloodGuard Nigeria**  
3MTT AI/ML Capstone Project
