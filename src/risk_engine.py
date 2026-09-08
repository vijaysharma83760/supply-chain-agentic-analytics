import json
from inventory_tools import get_inventory


def analyze_inventory(current_stock, reorder_point, daily_demand, lead_time):

    days_of_stock = (
        current_stock / daily_demand
        if daily_demand > 0
        else float("inf")
    )

    demand_during_lead_time = daily_demand * lead_time

    stock_risk = (
        "HIGH"
        if current_stock < reorder_point
        else "LOW"
    )

    supply_risk = (
        "HIGH"
        if days_of_stock < lead_time
        else "LOW"
    )

    shortage_risk = (
        "HIGH"
        if current_stock < demand_during_lead_time
        else "LOW"
    )

    if (
        stock_risk == "HIGH"
        or supply_risk == "HIGH"
        or shortage_risk == "HIGH"
    ):
        overall_risk = "HIGH"
    else:
        overall_risk = "LOW"

    return {
        "days_of_stock": round(days_of_stock, 2),
        "demand_during_lead_time": demand_during_lead_time,
        "stock_risk": stock_risk,
        "supply_risk": supply_risk,
        "shortage_risk": shortage_risk,
        "overall_risk": overall_risk
    }


def analyze_product_risk(product):

    inventory = get_inventory(product)

    if inventory is None:
        return {
            "product": product,
            "error": "Product not found"
        }

    risk = analyze_inventory(
        current_stock=inventory["current_stock"],
        reorder_point=inventory["reorder_point"],
        daily_demand=inventory["daily_demand"],
        lead_time=inventory["supplier_lead_time"]
    )

    return {
        "product": inventory["Product"],
        "current_stock": inventory["current_stock"],
        "reorder_point": inventory["reorder_point"],
        "daily_demand": inventory["daily_demand"],
        "supplier_lead_time": inventory["supplier_lead_time"],
        "unit_cost": inventory["unit_cost"],
        "risk_analysis": risk
    }


if __name__ == "__main__":

    result = analyze_product_risk("Laptop")

    print(json.dumps(result, indent=4))