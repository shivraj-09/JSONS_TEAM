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
              │   1. CLASSIFY     │
              │                   │
              │   Category        │
              │   Urgency         │
              │   Sentiment       │
              │   Reasoning       │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │   2. RESPOND      │
              │                   │
              │   Contextual AI   │
              │   Response        │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │   3. ESCALATE     │
              │                   │
              │   Deterministic   │
              │   Rule Engine     │
              └─────────┬─────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │ TICKET OBJECT│
                 └──────┬───────┘
                        │
                        ▼
                SUPPORT DASHBOARD

## 🧠 How the AI Works

### 1. Classification

The first AI stage analyzes the customer's message and extracts three key signals:

- **Category** — billing, technical, account, product, complaint, security/fraud, or general
- **Urgency** — low, medium, high, or critical
- **Sentiment** — positive, neutral, negative, or angry

The model also provides a short reasoning for the urgency classification.

### 2. Contextual Response Generation

A second Gemini call generates the customer-facing response.

Instead of generating a generic reply, the model receives the original query **along with the classification results**, allowing it to adapt its response based on:

- Customer sentiment
- Urgency level
- Type of issue
- Required support context

For example, a critical security complaint receives a more empathetic and action-oriented response than a routine product question.

### 3. Deterministic Escalation

Escalation is intentionally handled by **Python rules rather than another LLM decision**.

A ticket is escalated when:

```text
Urgency = HIGH or CRITICAL
OR
Sentiment = ANGRY
```

This makes the most important routing decision:

- predictable
- auditable
- testable
- independent of model wording

The AI understands the ticket.  
**The rule engine decides what happens next.**

---

## 🎯 Why This Approach?

Instead of using one large prompt to classify, respond, and escalate everything at once, the system separates the workflow into specialized stages.

| Approach | Advantage |
|---|---|
| **LLM Classification** | Understands intent, urgency, and sentiment from natural language |
| **Separate Response Generation** | Produces responses specifically informed by the classification |
| **Deterministic Rules** | Makes escalation predictable and auditable |
| **Structured JSON Output** | Allows the dashboard and backend to reliably consume AI results |

This hybrid architecture combines the flexibility of an LLM with the reliability of traditional application logic.

> **AI handles understanding. Code handles decisions that must be predictable.**

---

## 🖥️ Support Dashboard

The project includes a live support dashboard that gives support teams an immediate overview of incoming cases.

### 📊 Dashboard Insights

- **Total Tickets** — number of analyzed customer queries
- **Escalated Tickets** — cases requiring human attention
- **Critical Cases** — highest-priority customer issues
- **Handled Tickets** — cases processed by the AI pipeline
- **Category Distribution** — visual breakdown of support issues
- **Urgency Distribution** — low → critical ticket distribution
- **Live Ticket History** — reverse-chronological view of analyzed cases
- **AI Analysis Panel** — classification, sentiment, urgency, and escalation reasoning
- **Generated Response** — contextual response produced for the customer

The dashboard transforms raw AI output into an interface that a support team can actually use.

---

## 🏗️ System Architecture

```text
┌──────────────────────┐
│    Customer Query    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Gemini Classifier   │
│                      │
│ Category             │
│ Urgency              │
│ Sentiment            │
│ Reasoning            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Response Generator   │
│       Gemini         │
│                      │
│ Contextual Reply     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Escalation Engine   │
│   Deterministic      │
│       Rules          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Ticket Object    │
│                      │
│ Query + Analysis +   │
│ Response + Escalation│
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Flask REST API   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Support Dashboard  │
│   HTML/CSS/JS        │
│      + Chart.js      │
└──────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3** | Core backend logic |
| **Flask** | REST API and server |
| **Google Gemini API** | Classification & response generation |
| **google-generativeai** | Gemini Python SDK |
| **HTML / CSS / JavaScript** | Frontend dashboard |
| **Chart.js** | Support analytics and visualizations |
| **python-dotenv** | Secure environment variable loading |

---

## 🔌 API Endpoints

### `POST /api/analyze`

Analyzes a new customer support message.

**Input:**
```json
{
  "query": "Someone hacked my account and made an unauthorized payment!"
}
```

**Returns:**
- AI classification
- urgency
- sentiment
- generated response
- escalation decision
- escalation reason
- updated ticket log

### `GET /api/tickets`

Returns the current ticket history.

Used by the dashboard to restore the support queue after a page refresh.

### `GET /api/health`

Basic backend health check.

Useful for verifying that the Flask server is running correctly.

---

## ⚡ Getting Started

### Prerequisites

Make sure you have:

- Python 3.x
- Git
- A Google Gemini API key

### 1. Clone the Repository

```bash
git clone https://github.com/shivraj-09/JSONS_TEAM.git
cd JSONS_TEAM
```

### 2. Create and Activate the Virtual Environment

**Windows:**

```bash
cd backend
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create a `.env` file inside the `backend` directory:

```env
GEMINI_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file to GitHub. Your API key should remain private.

### 5. Start the Backend

From the `backend` directory:

```bash
python app.py
```

The Flask API will start at:

```text
http://127.0.0.1:5000
```

### 6. Start the Frontend

Open a **new terminal** and run:

```bash
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

### 7. Test the System

Try submitting:

```text
Someone hacked my account and made an unauthorized payment!
```

The system will:

```text
🧠 Classify the issue
      ↓
🚨 Determine urgency
      ↓
😡 Analyze sentiment
      ↓
💬 Generate a contextual response
      ↓
🔀 Determine human escalation
      ↓
📊 Update the dashboard
```

---

## 🧪 Example

### Customer Input

> "Someone hacked my account and made an unauthorized payment!"

### AI Analysis

```text
Category      → Security / Fraud
Urgency       → CRITICAL
Sentiment     → Angry
Escalation    → REQUIRED
```

### Generated Response

The system generates an empathetic, action-oriented response that acknowledges the security incident, requests relevant information, and prioritizes the case for human review.

### Why Escalate?

```text
Urgency = CRITICAL
        ↓
Human escalation required
```

This demonstrates how the AI and deterministic rule engine work together.

---

## 📁 Project Structure

```text
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
│   └── script.js
│
├── HANDOVER.md
├── README.md
└── ...
```

> `.env` is used locally for the Gemini API key and should **not** be committed to the repository.

---

## 🔐 Security & Design Considerations

### 🔑 API Key Protection

The Gemini API key is stored in an environment variable and accessed only by the backend.

The frontend never receives the API key.

### 🧩 Deterministic Escalation

Critical routing decisions are handled by explicit application logic instead of relying entirely on LLM judgment.

### 📦 Structured AI Output

Classification uses predefined categories and urgency/sentiment values, making downstream processing more reliable.

### ⚠️ Prototype Scope

This is a hackathon/prototype implementation. Production deployment would require additional security, authentication, persistence, monitoring, and access controls.

---

## 🚧 Limitations & Future Improvements

The current system intentionally keeps the implementation lightweight so the complete workflow can be demonstrated end-to-end.

Future improvements could include:

- 🗄️ **Persistent storage** using SQLite or PostgreSQL
- 🔐 **Authentication & role-based access**
- 👨‍💻 **Human-agent workspace** for escalated tickets
- 🔔 **Real-time notifications** for critical cases
- 📚 **Knowledge-base integration** for grounded responses
- 🧠 **Conversation memory** across multiple customer messages
- 📈 **Advanced support analytics**
- 🔄 **Ticket status management** — Open / In Progress / Resolved
- 🌐 **Production deployment**
- 🛡️ **Rate limiting, logging, and monitoring**

---

## 🏆 Why It Matters

Customer support shouldn't force teams to choose between **speed and quality**.

Our system automates the repetitive first layer of support — understanding what customers need, identifying urgent situations, generating contextual responses, and routing high-risk cases to humans.

**The goal isn't to replace support teams.**

It's to make them **faster, more consistent, and better equipped to focus human attention where it matters most.**

> **Let AI handle the first pass. Let humans handle the moments that matter.**

---

## 👥 Team

### JSON'S TEAM

**Shivraj Nirloti**  
**Shaurya Darne**

Built as an AI-powered customer support automation prototype.

---

## ⭐ Project Vision

> **Understand every customer. Prioritize what matters. Respond intelligently. Escalate responsibly.**

**AI Customer Support System — turning an overwhelming support queue into an intelligent, prioritized workflow.**
