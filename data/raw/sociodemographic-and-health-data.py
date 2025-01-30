import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/regularized-linear-regression-project-tutorial/main/demographic_health_data.csv"

df = pd.read_csv(url)

df.to_csv('sociodemographic_and_health_data.csv', index=False)
print("Dataset saved as 'sociodemographic_and_health_data.csv'")