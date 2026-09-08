# ============================================================
# Supply Chain Agentic Analytics
# Data Loader
# ============================================================

import pandas as pd


def load_supply_chain_data():
    file_path = "data/supply_chain_data.csv"

    data = pd.read_csv(file_path)

    return data

# ============================================================
# Test Data Loader
# ============================================================

data = load_supply_chain_data()

print(data)