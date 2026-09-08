# ============================================================
# Supply Chain Agentic Analytics
# Inventory Tools
# ============================================================

from data_loader import load_supply_chain_data


def get_inventory(product):
    data = load_supply_chain_data()

    result = data[data["Product"].str.lower() == product.lower()]

    if result.empty:
        return None

    return result.iloc[0].to_dict()


# ============================================================
# Test Inventory Tool
# ============================================================

laptop = get_inventory("Laptop")

print(laptop)