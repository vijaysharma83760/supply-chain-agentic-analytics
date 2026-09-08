# ============================================================
# Supply Chain Agentic Analytics
# Agent / Decision Orchestrator
# ============================================================

from risk_engine import analyze_product_risk


# ============================================================
# Supply Chain Agent
# ============================================================

def supply_chain_agent(product):
    """
    Analyze product inventory risk and generate
    a business recommendation.
    """

    # --------------------------------------------------------
    # Step 1: Analyze product risk
    # --------------------------------------------------------

    result = analyze_product_risk(product)

    # --------------------------------------------------------
    # Step 2: Handle invalid product
    # --------------------------------------------------------

    if "error" in result:
        print()
        print("============================================================")
        print("SUPPLY CHAIN RISK DECISION")
        print("============================================================")
        print("Product:", product)
        print("Error:", result["error"])
        print("============================================================")
        return

    # --------------------------------------------------------
    # Step 3: Extract risk information
    # --------------------------------------------------------

    risk = result["risk_analysis"]

    stock_risk = risk["stock_risk"]
    supply_risk = risk["supply_risk"]
    shortage_risk = risk["shortage_risk"]
    overall_risk = risk["overall_risk"]

    # --------------------------------------------------------
    # Step 4: Extract inventory information
    # --------------------------------------------------------

    current_stock = result["current_stock"]
    reorder_point = result["reorder_point"]
    daily_demand = result["daily_demand"]
    lead_time = result["supplier_lead_time"]

    # --------------------------------------------------------
    # Step 5: Business Decision Logic
    # --------------------------------------------------------

    if overall_risk == "HIGH":

        if shortage_risk == "HIGH":
            recommendation = "Urgent replenishment required"

        elif supply_risk == "HIGH":
            recommendation = "Supplier lead-time risk - expedite replenishment"

        elif stock_risk == "HIGH":
            recommendation = "Stock below reorder point - initiate replenishment"

        else:
            recommendation = "High risk detected - immediate review required"

        approval_required = "YES"

    else:

        recommendation = "Inventory condition is stable"
        approval_required = "NO"

    # --------------------------------------------------------
    # Step 6: Display Business Decision
    # --------------------------------------------------------

    print()
    print("============================================================")
    print("SUPPLY CHAIN RISK DECISION")
    print("============================================================")

    print("Product:", product)
    print("Current Stock:", current_stock)
    print("Reorder Point:", reorder_point)
    print("Daily Demand:", daily_demand)
    print("Supplier Lead Time:", lead_time, "days")

    print()
    print("Stock Risk:", stock_risk)
    print("Supply Risk:", supply_risk)
    print("Shortage Risk:", shortage_risk)
    print("Overall Risk:", overall_risk)

    print()
    print("Recommendation:", recommendation)
    print("Approval Required:", approval_required)

    print("============================================================")


# ============================================================
# Test Cases
# ============================================================

if __name__ == "__main__":

    print("\nTEST 1 - Laptop")
    supply_chain_agent("Laptop")

    print("\nTEST 2 - Monitor")
    supply_chain_agent("Monitor")

    print("\nTEST 3 - Mouse")
    supply_chain_agent("Mouse")

    print("\nTEST 4 - Invalid Product")
    supply_chain_agent("ABC123")