# 🚚 FastBox Logistics Simulator

A Python-based delivery simulation I built as part of the FastBox logistics network assignment. The idea was pretty straightforward — simulate a real day of deliveries, but do it in a way that's clean, scalable, and actually handles the messy edge cases you'd encounter in the real world.

Under the hood, the system assigns packages to the nearest available delivery agent using Euclidean distance, tracks how far each agent travels, and wraps everything up in a structured JSON report at the end.

---

## What It Does

At its core, this simulator answers one question: *"Given a set of packages, warehouses, and delivery agents — who delivers what, and how efficiently?"*

Here's what's happening behind the scenes:

- Reads and parses JSON input files describing agents, warehouses, and packages
- For each package, finds the nearest delivery agent and assigns it to them
- Simulates the delivery route: **Agent → Warehouse → Destination**
- Tracks total travel distance per agent
- Computes efficiency metrics and identifies the best-performing agent
- Writes a clean summary report to `report.json`

---

## Project Structure

```
FASTBOX-LOGISTICS/
│
├── test_cases/
│   ├── test_case_1.json
│   ├── test_case_2.json
│   └── test_case_3.json
│
├── data.json
├── main.py
├── report.json
└── README.md
```

The `test_cases/` folder holds several datasets I used to stress-test different scenarios. `data.json` is the default input, and `report.json` is where the output lands after each run.

---

## How to Run

```bash
python main.py
```

You'll be prompted to enter the name of a JSON input file:

```
data.json
```

or a test case:

```
test_cases/test_case_1.json
```

That's it. The simulation runs and writes the results to `report.json`.

---

## The Math Behind It

**Distance** is calculated using the standard Euclidean formula:

```
distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

This gets applied twice per delivery — once from the agent to the warehouse, and again from the warehouse to the destination.

**Efficiency** is calculated as:

```
efficiency = total_distance / packages_delivered
```

A lower number means the agent is doing more with less distance — which is what you want.

---

## Sample Output

After a run, `report.json` looks something like this:

```json
{
    "A1": {
        "packages_delivered": 2,
        "total_distance": 64.14,
        "efficiency": 32.07
    },
    "A2": {
        "packages_delivered": 2,
        "total_distance": 75.57,
        "efficiency": 37.79
    },
    "A3": {
        "packages_delivered": 1,
        "total_distance": 18.25,
        "efficiency": 18.25
    },
    "best_agent": "A3"
}
```

In this case, A3 wins — fewer deliveries, but an impressively short route.

---

## Assumptions I Made

The assignment left a few things open-ended, so here's how I filled the gaps:

- Agents don't move between deliveries — their position stays fixed at their starting coordinates
- Every package is assigned independently to the nearest agent at the time
- If two agents are equally close, the first one encountered in the list gets the job
- Agents who end up with zero deliveries get an efficiency score of `0`
- The sample output in the assignment was treated as illustrative — my values are calculated strictly from the Euclidean math

---

## Test Coverage

The `test_cases/` folder covers a range of scenarios I wanted to make sure the system handled gracefully:

- Multiple warehouses and agents spread across different coordinates
- Uneven package distributions (some agents getting much more than others)
- Zero-delivery agents (agents that exist but get nothing assigned)
- Large coordinate values that could expose floating point issues
- Edge cases where distance ties need to be broken

---


## What I Learned

Honestly, this project was a good exercise in thinking through a system end-to-end. The logistics logic itself isn't complicated, but getting the assignment algorithm right, handling the edge cases cleanly, and keeping the codebase readable — that took more thought than I expected.

Key takeaways: JSON parsing, distance-based sorting, simulation design, dictionary management, and being deliberate about edge case handling from the start rather than patching them in later.

---

## Author

**Agnel Vincent**  
Python Developer | Django + React Enthusiast