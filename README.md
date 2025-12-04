# 🚀 Ndeleh Fishbone Algorithm (NFBA v2)  
### AI-Assisted Root-Cause Diagnostics for Industrial Torque Systems  
**Created by:** Ndeleh  

---

## 📌 Overview  
The **Ndeleh Fishbone Algorithm (NFBA v2)** is a modern, AI-assisted diagnostic engine designed to help industrial and automotive manufacturing teams quickly identify *root causes* of torque anomalies, jams, operator variance, and cycle-time issues.

NFBA v2 blends:

- 📊 **Graph-based cause–effect modeling**  
- 🤖 **AI pattern extraction via the Fishbone v2 engine**  
- 🔧 **Industrial domain rules (GM-style torque station logic)**  
- ⚡ **FastAPI for real-time diagnostics**  
- 🧪 **7/7 passing unit tests for reliability**  

This system does **not replace workers**.  
It **supports** operators, engineers, and team leaders with clear, consistent diagnostics.

---

## 🧠 What NFBA v2 Does  
Given torque readings and event indicators, NFBA v2 produces:

- A structured diagnosis  
- Determined root cause  
- Recommendations  
- Confidence score  
- A fishbone-style “spine” of contributing nodes  
- Weight mappings for all factors

### Example Output
```json
{
  "status": "ok",
  "torque_value": 25,
  "diagnosis": [],
  "root_cause": "No abnormal torque condition detected",
  "recommendation": "No action required",
  "confidence": 0.99,
  "spine": ["torque", "machine", "operator", "environment"],
  "weights": {"tool_wear": 0.9, "material_issue": 0.7}
}

ndeleh_fba/
│
├── src/ndeleh_fba/
│   ├── api/                     # FastAPI server + endpoints
│   ├── industrial/              # Torque diagnostic logic
│   ├── fishbone_v2.py           # NFBA v2 reasoning engine
│   ├── graph.py                 # Core graph data model
│   └── ...
│
├── tests/                       # Pytest unit tests (7 passing)
├── dist/                        # Build artifacts for PyPI
└── pyproject.toml               # Project metadata

🛠️ Installation
Install from TestPyPI
pip install -i https://test.pypi.org/simple/ ndeleh_fba


Or install locally:

pip install .

⚡ Running the FastAPI Server

Start the API:

PYTHONPATH=src uvicorn ndeleh_fba.api.server:app --reload


Open documentation:

👉 http://127.0.0.1:8000/docs

You can test torque diagnostics right from Swagger UI.

🔧 Example API Request

POST → /diagnose/torque

{
  "torque_value": 18,
  "target_min": 22,
  "target_max": 30,
  "is_red_flag": false,
  "jam_detected": false,
  "cycle_time": 3.2,
  "retries": 0,
  "manual_check_used": false
}

🧪 Running the Full Test Suite
pytest -q


Expected result:

7 passed, 0 failed

🎯 Purpose and Philosophy

NFBA v2 was created to help protect manufacturing jobs by giving teams:

Faster diagnostics

Insight into operator/machine/environment relationships

Early detection of torque and assembly issues

Support for decision-making

A consistent method for reporting issues

This is not about replacing humans.
It’s about supporting the people who run the plant every day.

📦 Publishing

This package is already live on TestPyPI and ready for production deployment.

🧑‍💻 Author

Ndeleh
GitHub: https://github.com/NDELEH



