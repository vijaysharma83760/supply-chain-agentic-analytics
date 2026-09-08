# Supply Chain Agentic Analytics

A Python-based supply chain risk analytics and decision workflow that analyzes inventory conditions, identifies stock and supply risks, and generates business recommendations with human approval checkpoints.

## Project Overview

Supply chain teams need to identify inventory risks before they become stockouts or operational disruptions.

This project demonstrates a practical **data + AI/agentic decision workflow** for inventory risk management.

The system takes supply chain data as input, analyzes multiple risk factors, determines an overall risk level, and produces an actionable business recommendation.

### Business Workflow

```text
Supply Chain Data
       ↓
Inventory Data Loader
       ↓
Inventory Tools
       ↓
Risk Analysis Engine
       ↓
Stock Risk
Supply Risk
Shortage Risk
       ↓
Overall Risk
       ↓
Business Recommendation
       ↓
Human Approval
```

## Business Problem

The system answers questions such as:

* Is current inventory below the reorder point?
* Will existing stock last through the supplier lead time?
* Is there a potential shortage before replenishment arrives?
* What is the overall inventory risk?
* Should replenishment be initiated?
* Is human approval required?

## Risk Logic

The project evaluates three major risk dimensions.

### 1. Stock Risk

Compares current inventory with the reorder point.

```text
Current Stock < Reorder Point
        → HIGH RISK
```

### 2. Supply Risk

Calculates how many days the current inventory can support demand.

```text
Days of Stock = Current Stock / Daily Demand
```

If days of stock are lower than supplier lead time:

```text
Days of Stock < Supplier Lead Time
        → HIGH RISK
```

### 3. Shortage Risk

Calculates expected demand during supplier lead time.

```text
Demand During Lead Time =
Daily Demand × Supplier Lead Time
```

If current inventory cannot cover this demand:

```text
Current Stock < Demand During Lead Time
        → HIGH RISK
```

If any major risk is HIGH:

```text
Overall Risk = HIGH
```

## Example Decision

For the Laptop:

```text
Current Stock: 75
Reorder Point: 100
Daily Demand: 20
Supplier Lead Time: 7 days

Stock Risk: HIGH
Supply Risk: HIGH
Shortage Risk: HIGH
Overall Risk: HIGH

Recommendation:
Urgent replenishment required

Approval Required:
YES
```

For a stable product such as a Monitor:

```text
Current Stock: 150
Reorder Point: 80
Daily Demand: 15
Supplier Lead Time: 5 days

Overall Risk: LOW

Recommendation:
Inventory condition is stable

Approval Required:
NO
```

## Project Architecture

```text
supply-chain-agentic-analytics/
│
├── data/
│   └── supply_chain_data.csv
│
├── docs/
│
├── screenshots/
│   └── risk_decision_demo.png
│
├── src/
│   ├── agent.py
│   ├── data_loader.py
│   ├── inventory_tools.py
│   └── risk_engine.py
│
├── requirements.txt
└── README.md
```

## Components

### `data_loader.py`

Loads and prepares the supply chain CSV data for analysis.

### `inventory_tools.py`

Provides inventory lookup functionality used by the decision workflow.

### `risk_engine.py`

Calculates:

* Days of stock
* Demand during lead time
* Stock risk
* Supply risk
* Shortage risk
* Overall risk

### `agent.py`

Acts as the decision layer.

It:

1. Receives a product
2. Retrieves inventory information
3. Runs risk analysis
4. Determines the overall risk
5. Generates a business recommendation
6. Determines whether human approval is required

## Technology Stack

* Python
* Pandas
* CSV
* Inventory Analytics
* Business Rules
* Risk Analysis
* Decision Workflows
* Agentic AI concepts

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/vijaysharma83760/supply-chain-agentic-analytics.git
```

### 2. Navigate to the project

```bash
cd supply-chain-agentic-analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the agent

```bash
python src/agent.py
```

The program evaluates multiple products and displays the resulting risk decisions.

## Sample Output

```text
============================================================
SUPPLY CHAIN RISK DECISION
============================================================
Product: Laptop
Current Stock: 75
Reorder Point: 100
Daily Demand: 20
Supplier Lead Time: 7 days

Stock Risk: HIGH
Supply Risk: HIGH
Shortage Risk: HIGH
Overall Risk: HIGH

Recommendation: Urgent replenishment required
Approval Required: YES
============================================================
```

## Project Screenshot

The project includes a demonstration of the decision workflow:

`screenshots/risk_decision_demo.png`

## Why This Project Matters

This project demonstrates how traditional supply chain analytics can be converted into a **decision-oriented workflow**.

Instead of only reporting inventory metrics, the system moves from:

```text
Data
 ↓
Analysis
 ↓
Risk Detection
 ↓
Decision
 ↓
Recommendation
 ↓
Human Approval
```

This approach can be extended toward more advanced agentic systems where AI agents interact with data sources, analytical tools, business rules, and human approval workflows.

## Future Enhancements

Planned improvements include:

* SQL-based supply chain data access
* Power BI dashboard integration
* LLM-based reasoning layer
* Multi-agent supply chain workflow
* Supplier performance analysis
* Automated purchase-order recommendations
* Real-time inventory monitoring
* Exception alerts
* Human-in-the-loop approval workflow
* Cloud deployment

## Author

**Vijay Sharma**

Interested in opportunities involving:

**Data Analytics | Supply Chain Analytics | Python | SQL | Power BI | AI / Agentic AI**

---

## License

This project is created for learning, portfolio development, and demonstration purposes.
