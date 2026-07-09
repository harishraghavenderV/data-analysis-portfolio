import subprocess
import os

notebooks = [
    "project1_sales_analysis/analysis.ipynb",
    "project2_healthcare_analysis/analysis.ipynb",
    "project3_sports_analytics/analysis.ipynb",
    "project4_financial_analysis/analysis.ipynb",
    "project5_ecommerce_analysis/analysis.ipynb",
    "portfolio_summary.ipynb"
]

# Set environment variable to make sure plots show up correctly and matplotlib works headlessly
os.environ["MPLBACKEND"] = "Agg"

for nb in notebooks:
    print(f"Executing notebook: {nb}...")
    try:
        result = subprocess.run([
            ".venv/Scripts/python", "-m", "nbconvert", 
            "--to", "notebook", 
            "--execute", 
            "--inplace", 
            "--ExecutePreprocessor.timeout=600",
            nb
        ], capture_output=True, text=True, check=True)
        print(f"Successfully executed {nb}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {nb}:")
        print(e.stdout)
        print(e.stderr)
        raise e

print("All notebooks executed successfully and visualizations generated!")
