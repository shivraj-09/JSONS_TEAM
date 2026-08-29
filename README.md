# 🤖 AI Customer Support System

> ### Understand. Prioritize. Respond. Escalate.

An AI-powered customer support agent that transforms raw customer messages into **structured, actionable support decisions**.

It understands the customer's issue, detects urgency and sentiment, generates a contextual response, and determines whether the case requires **human intervention**.

<br>

<div align="center">

**🧠 Classify** &nbsp; • &nbsp;
**🚨 Prioritize** &nbsp; • &nbsp;
**💬 Respond** &nbsp; • &nbsp;
**🔀 Escalate**

</div>

---

## 🚀 What Does It Do?

Modern support teams receive thousands of messages ranging from simple product questions to urgent billing disputes and potential security incidents.

Manually processing every message creates two major problems:

- ⏳ **Slow triage** — humans must read every ticket before understanding its urgency.
- 🎭 **Inconsistent responses** — tone and response quality can vary between support agents.

**Our system automates the first layer of customer support while keeping humans in control of high-risk cases.**

### Example

**Customer message**

> "Someone hacked my account and made an unauthorized payment!"

### AI Analysis

| Signal | Result |
|---|---|
| 🏷️ Category | **Security / Fraud** |
| 🚨 Urgency | **CRITICAL** |
| 😡 Sentiment | **Angry** |
| 🔀 Escalation | **REQUIRED** |

The system then generates an appropriate customer-facing response and creates an escalation ticket for the human support team.

---

## ✨ Key Features

### 🧠 Intelligent Query Classification
Automatically identifies the type of customer issue and extracts structured support signals.

### 🚨 Urgency Detection
Ranks tickets from **Low → Medium → High → Critical**, allowing support teams to focus on the cases that matter most.

### 😡 Sentiment Analysis
Detects customer sentiment and adapts the response accordingly.

### 💬 Contextual Response Generation
Generates a customer-facing response using the original message together with its AI classification.

### 🔀 Smart Human Escalation
High-risk cases are automatically routed toward human support using explicit, deterministic rules.

### 📊 Real-Time Support Dashboard
Provides a visual overview of the support queue, including ticket statistics, classifications, urgency levels, and escalation status.

---

## 🔄 AI Agent Workflow

```text
                 CUSTOMER MESSAGE
                        │
                        ▼
              ┌───────────────────┐
              │  1. CLASSIFY      │
              │                   │
              │ Category           │
              │ Urgency            │
              │ Sentiment          │
              │ Reasoning          │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  2. RESPOND       │
              │                   │
              │ Contextual AI     │
              │ Response          │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │  3. ESCALATE      │
              │                   │
              │ Deterministic     │
              │ Rule Engine       │
              └─────────┬─────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ TICKET OBJECT│
                 └──────┬───────┘
                        │
                        ▼
                SUPPORT DASHBOARD

🧠 How the AI Works
1. Classification

The first AI stage analyzes the customer's message and produces structured information:

{
  "category": "security_fraud",
  "urgency": "critical",
  "sentiment": "angry",
  "reasoning": "The customer reports an unauthorized payment and possible account compromise."
}

The structured output allows the rest of the system to make consistent decisions without parsing free-form AI responses.

2. Response Generation

A second AI stage receives:

The original customer message
The detected category
The urgency
The sentiment

This allows the response tone to adapt to the situation.

For example:

Neutral + Low urgency
        ↓
Informative response

Angry + Critical urgency
        ↓
Empathetic + urgent response
        + human escalation

The system therefore separates understanding the problem from communicating the solution.

3. Deterministic Escalation

Escalation is intentionally handled by code rather than another LLM decision.

ESCALATION_RULES = {
    "critical": True,
    "high": True,
    "medium": False,
    "low": False
}

ANGRY_SENTIMENT_ESCALATES = True

A ticket is escalated when:

Urgency = CRITICAL
        OR
Urgency = HIGH
        OR
Sentiment = ANGRY
Why?

Escalation is a high-impact decision.

A deterministic rule is:

✅ Predictable
✅ Auditable
✅ Testable
✅ Easy to modify
✅ Independent of LLM randomness

The LLM determines what the customer is experiencing.

The rule engine determines what the system should do about it.

🎯 Why This Architecture?

Instead of asking one large LLM prompt to perform everything, the system separates the workflow into independent stages.

Design Decision	Why?
🧠 Separate classification	Makes AI decisions structured and inspectable
💬 Separate response generation	Allows response tone to explicitly depend on classification
🔀 Rule-based escalation	Prevents critical routing decisions from depending entirely on LLM judgment
📦 JSON output	Makes AI results easy for the backend and dashboard to consume
🎨 Fixed classification values	Keeps dashboard visualizations and ticket filtering consistent
🗄️ In-memory ticket log	Keeps the prototype simple while allowing future database integration

This makes the system easier to debug, evaluate, and extend.

🖥️ Support Dashboard

The project includes a live support dashboard designed to give support teams an immediate overview of their queue.

Dashboard includes
📊 Total tickets
🚨 Escalated tickets
🔴 Critical cases
✅ Handled cases
🏷️ Category distribution
📈 Urgency distribution
💬 Customer conversation
🧠 AI analysis
🔀 Escalation tickets
🕐 Live ticket history

The latest customer interaction and its AI analysis are displayed directly in the support console.

🏗️ System Architecture
┌─────────────────────┐
│    Customer Query   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Flask Backend    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Gemini API       │
│                     │
│  Classification     │
│  Response Generation│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Escalation Engine  │
│                     │
│ Deterministic Rules │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Ticket Log      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Support Dashboard │
│                     │
│ HTML / CSS / JS     │
│      Chart.js       │
└─────────────────────┘
🛠️ Tech Stack
Technology	Purpose
🐍 Python 3	Backend logic
🌶️ Flask	REST API
🧠 Gemini API	Classification & response generation
🔐 python-dotenv	Environment variable management
🌐 HTML / CSS / JavaScript	Frontend dashboard
📊 Chart.js	Dashboard visualizations
🔗 Flask-CORS	Frontend/backend communication
🔌 API Endpoints
Method	Endpoint	Description
POST	/api/analyze	Analyze a customer message and create a ticket
GET	/api/tickets	Retrieve the ticket log
GET	/api/health	Check backend health
POST /api/analyze

Example request:

{
  "message": "Someone hacked my account and made an unauthorized payment!"
}

The endpoint runs the complete pipeline:

Message
   ↓
Classification
   ↓
Response Generation
   ↓
Escalation Decision
   ↓
Ticket
⚡ Getting Started

Follow these steps to run the project locally.

1. Clone the repository
git clone https://github.com/shivraj-09/JSONS_TEAM.git
cd JSONS_TEAM
2. Set up the backend

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
3. Configure the Gemini API

Create a file named:

backend/.env

Add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

⚠️ Never commit your .env file to GitHub.

Your API key should remain private.

4. Start the backend

From the backend directory:

python app.py

The backend will run at:

http://127.0.0.1:5000

You can verify that the server is running using:

http://127.0.0.1:5000/api/health
5. Start the frontend

Open a new terminal.

Navigate to the frontend:

cd frontend

Start a local server:

python -m http.server 5500

Open the dashboard:

http://127.0.0.1:5500
6. Test the system

Try entering:

Someone hacked my account and made an unauthorized payment!

The system should automatically:

🧠 Classify the issue
        ↓
🚨 Determine urgency
        ↓
😡 Analyze sentiment
        ↓
💬 Generate a contextual response
        ↓
🔀 Determine escalation
        ↓
📊 Update the dashboard
🧪 Example
Input

"I've been charged twice this month and nobody has replied to me!"

Expected AI Analysis
Category    → Billing
Urgency     → High
Sentiment   → Angry
Escalation  → Required
Generated Response

The response-generation agent creates an empathetic response that acknowledges the billing issue and its urgency while directing the case toward appropriate human support.

📁 Project Structure
JSONS_TEAM/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── ...
│
├── README.md
└── HANDOVER.md

.env should remain local and must not be committed to the repository.

🔐 Security & Design Considerations
API Key Protection

The Gemini API key is loaded from an environment variable rather than being exposed in frontend JavaScript.

.env
 ↓
Backend
 ↓
Gemini API
Deterministic Escalation

Critical support decisions are handled by explicit backend rules rather than relying entirely on model-generated decisions.

Human-in-the-Loop

The system is designed to assist support teams, not replace them.

High-risk cases are surfaced for human intervention.

🚧 Limitations & Future Improvements

This project is currently designed as a working prototype.

Planned improvements
🗄️ Persistent ticket storage using SQLite/PostgreSQL
🔐 User authentication and role-based access
👨‍💼 Dedicated human-agent workspace
🔔 Real-time notifications for critical tickets
📚 Knowledge-base / RAG integration
📈 Advanced support analytics
🧾 Persistent conversation history
🔄 Ticket status management
☁️ Production deployment
🧪 Automated evaluation of classification accuracy

The current architecture intentionally keeps these components replaceable without changing the core AI workflow.

🧩 Key Engineering Principle

Use AI where interpretation is required. Use deterministic code where decisions must be predictable.

The LLM handles:

"What is happening?"
"What does the customer need?"
"How should we respond?"

The rule engine handles:

"Does this require human escalation?"

This separation provides a balance between AI flexibility and system reliability.

🏆 Why It Matters

Customer support shouldn't force humans to choose between speed and quality.

Our system automates the repetitive first layer of support — understanding customer needs, prioritizing urgent cases, drafting contextual responses, and routing high-risk situations to humans.

The goal isn't to replace support teams. It's to make them faster, more consistent, and better equipped to focus on the cases that actually need human judgment.

👥 Team
JSON'S TEAM

1. Shivraj Nirloti
2. Shaurya Darne

<div align="center">
🤖 AI Customer Support System

Understand. Prioritize. Respond. Escalate.

Built with ❤️ for intelligent, human-centered customer support.

</div> ```
