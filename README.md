# OptiForge

## Autonomous IT Operations & Self-Healing Platform

OptiForge is an AI-driven IT operations and self-healing platform designed to monitor system health, detect anomalies, make adaptive recovery decisions, execute corrective actions, and verify system recovery automatically.

---

## 🚀 Key Features

- Real-time system monitoring
- CPU and memory monitoring
- Response-time monitoring
- Error-rate monitoring
- Service availability monitoring
- Automatic anomaly detection
- Adaptive agent selection
- Workload-aware decision making
- Intelligent recovery actions
- Self-healing simulation
- Recovery verification
- FastAPI backend
- Interactive web dashboard
- Automated test suite

---

## 🧠 System Workflow

```text
             System Metrics
                   │
                   ▼
             ┌─────────────┐
             │  Monitoring │
             └──────┬──────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Anomaly Detection │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │  Decision Engine  │
          └─────────┬─────────┘
                    │
                    ▼
            ┌───────────────┐
            │Agent Selection│
            └───────┬───────┘
                    │
                    ▼
            ┌───────────────┐
            │Recovery Action│
            └───────┬───────┘
                    │
                    ▼
          ┌─────────────────────┐
          │Recovery Verification│
          └──────────┬──────────┘
                     │
                     ▼
              Updated Status
📁 Project Structure
optiforge-2026/
│
├── api/
│   ├── app.py
│   └── routes.py
│
├── core/
│   ├── __init__.py
│   ├── agent.py
│   ├── swarm.py
│   ├── heuristics.py
│   ├── decision_engine.py
│   ├── simulation.py
│   ├── monitoring.py
│   ├── anomaly_detection.py
│   ├── recovery.py
│   └── self_healing.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_core.py
│   ├── test_monitoring.py
│   ├── test_recovery.py
│   ├── test_self_healing.py
│   └── test_api.py
│
├── .gitignore
└── README.md
⚙️ Core Components
1. Agent System

OptiForge uses multiple agents with different:

Workloads
CPU capacity
Memory capacity
Reliability
Communication quality
Capabilities
Availability status

Agents are evaluated based on their current state before an action is assigned.

2. Swarm Management

The swarm manages multiple agents and provides:

Available-agent detection
Capability-based agent filtering
Agent status handling
Failed-agent exclusion

Example:

Agent A → available
Agent B → failed
Agent C → available

Required capability → restart_service

Selected capable agent → Agent A
3. Heuristic Scoring

Each available agent receives a score based on factors such as:

Current workload
CPU capacity
Memory capacity
Reliability
Communication quality
Availability

The decision engine uses these scores to select a suitable agent for a requested action.

4. Monitoring

The monitoring component collects system health metrics including:

CPU usage
Memory usage
Response time
Error rate
Service availability
5. Anomaly Detection

OptiForge analyzes monitoring data and identifies abnormal conditions such as:

High CPU usage
High memory usage
Slow response time
High error rate
Service failure

Example:

CPU Usage = 95%
      ↓
Anomaly Detected
      ↓
high_cpu
6. Decision Engine

After detecting an anomaly, the decision engine determines:

Required action
Suitable agent
Agent score

Example:

Detected Issue : high_cpu
Selected Agent : A
Action         : reduce_load
Decision Score : 0.688
7. Self-Healing

OptiForge automatically performs simulated recovery actions according to the detected issue.

Examples:

High CPU
    ↓
reduce_load
High Memory
    ↓
free_memory
Service Failure
    ↓
restart_service
8. Recovery Verification

After performing a recovery action, OptiForge verifies whether the recovery was successful.

Anomaly
   ↓
Recovery Action
   ↓
Recovery Successful
   ↓
Recovery Verified
🌐 FastAPI Backend

OptiForge provides a FastAPI backend for communication between the dashboard and the core system.

Start the Backend

Activate the virtual environment:

.\.venv\Scripts\Activate.ps1

Then run:

python -m uvicorn api.app:app --reload

The backend runs at:

http://127.0.0.1:8000
🔍 API Health Check

Open:

http://127.0.0.1:8000/health

Expected response:

{
  "status": "online",
  "service": "OptiForge"
}
🖥️ Frontend Dashboard

OptiForge includes a web-based dashboard for visualizing system health and recovery decisions.

Start the Frontend

Open another terminal and run:

python -m http.server 5500 --directory frontend

Then open:

http://127.0.0.1:5500

The dashboard displays:

API status
CPU usage
Memory usage
Response time
Error rate
System status
Detected anomaly
Selected agent
Recovery action
Decision score
Recovery verification
🧪 Example High CPU Scenario

Input:

{
  "cpu_usage": 0.95,
  "memory_usage": 0.50,
  "response_time": 0.5,
  "error_rate": 0.02,
  "service_available": true
}

OptiForge detects:

Anomaly: high_cpu
Severity: medium

The decision engine selects an appropriate agent:

Agent: A
Action: reduce_load
Score: 0.688

The recovery system executes the simulated recovery:

Recovery successful
Recovery verified

The dashboard displays:

System Status
RECOVERED
🛠️ Technologies Used
Technology	Purpose
Python	Core application logic
FastAPI	Backend API
psutil	System monitoring
Pytest	Automated testing
HTML	Dashboard structure
CSS	Dashboard styling
JavaScript	Frontend and API interaction
Git	Version control
GitHub	Source-code hosting
🧪 Testing

The project includes an automated test suite covering:

Agent functionality
Swarm management
Heuristic scoring
Decision engine
System monitoring
Anomaly detection
Recovery
Self-healing
API endpoints
Frontend/API integration

Run the complete test suite:

python -m pytest

Current test result:

22 passed
🔄 Self-Healing Workflow

A typical OptiForge operation follows this sequence:

1. Monitor system
       ↓
2. Detect abnormal condition
       ↓
3. Identify required recovery action
       ↓
4. Find capable agents
       ↓
5. Calculate agent scores
       ↓
6. Select suitable agent
       ↓
7. Execute recovery action
       ↓
8. Verify recovery
       ↓
9. Update system status
📊 Demonstrated Scenarios
Normal System
System operating normally
No active anomalies detected
High CPU
high_cpu
    ↓
reduce_load
    ↓
Recovery verified
High Memory
high_memory
    ↓
Recovery action
    ↓
Recovery verified
Service Failure
service_failure
    ↓
restart_service
    ↓
Recovery verified
🎯 Project Objective

The objective of OptiForge is to demonstrate an autonomous IT operations workflow in which system problems can be detected, analyzed, assigned to suitable agents, automatically remediated, and verified with minimal manual intervention.

The platform combines monitoring, anomaly detection, adaptive decision making, agent-based coordination, recovery, and a visual dashboard into a single system.

👥 Development Structure

The project was developed as a modular multi-member implementation.

Member 1
Core Agent & Decision System
        ↓
Member 2
Monitoring & Self-Healing
        ↓
Member 3
FastAPI Backend
        ↓
Member 4
Frontend Dashboard
        ↓
Integrated OptiForge Platform
📌 Project Status

Implementation Complete

The following components have been integrated successfully:

Agent decision system
Swarm management
Heuristic scoring
Decision engine
System monitoring
Anomaly detection
Recovery system
Self-healing system
FastAPI backend
Interactive frontend dashboard
Automated test suite
🚀 Final Result

OptiForge provides an end-to-end autonomous IT operations workflow:

MONITOR
   ↓
DETECT
   ↓
DECIDE
   ↓
ACT
   ↓
RECOVER
   ↓
VERIFY

OptiForge — Autonomous IT Operations & Self-Healing Platform