# 🤖 AI Customer Support System

> Understand. Prioritize. Respond. Escalate.

Short 2–3 line description

[Key badges / tech stack]

## 🚀 What does it do?

Problem + solution
Example ticket → AI analysis

## ✨ Key Features

- 🧠 Query Classification
- 🚨 Urgency Detection
- 💬 Contextual Response Generation
- 🔀 Smart Human Escalation
- 📊 Real-time Support Dashboard

## 🔄 AI Agent Workflow

Customer Query
      ↓
Classification
      ↓
Response Generation
      ↓
Escalation Engine
      ↓
Ticket + Dashboard

## 🧠 How the AI Works

### 1. Classification
...
### 2. Response Generation
...
### 3. Deterministic Escalation
...

## 🎯 Why This Approach?

Explain why LLM + rules instead of one giant prompt.

## 🖥️ Dashboard

Explain what the UI shows:
- Total tickets
- Escalated tickets
- Critical cases
- Category distribution
- Urgency distribution
- Live ticket history

## 🏗️ Architecture

Backend → Gemini → Rule Engine → API → Dashboard

## 🛠️ Tech Stack

Python
Flask
Gemini API
HTML/CSS/JS
Chart.js

## 🔌 API Endpoints

POST /api/analyze
GET /api/tickets
GET /api/health

## ⚡ Getting Started

Installation instructions

## 🧪 Example

Input:
"Someone hacked my account..."

Output:
Category → Security/Fraud
Urgency → Critical
Sentiment → Angry
Escalation → Required

## 📁 Project Structure

...
    
## 🔐 Security & Design Considerations

.env
deterministic escalation
no API key in frontend

## 🚧 Limitations & Future Improvements

SQLite/PostgreSQL
authentication
persistent ticket storage
human-agent workflow
etc.

## 🏆 Why It Matters

## 🏆 Why It Matters

Customer support shouldn't force humans to choose between speed and quality.

Our system handles the repetitive first layer of support automatically — understanding what customers need, prioritizing urgent cases, drafting contextual responses, and routing high-risk situations to humans.

**The goal isn't to replace support teams. It's to make them faster, more consistent, and better equipped to focus on the cases that actually need human judgment.**

## 👥 Team

JSON'S TEAM
1.SHIVRAJ NIRLOTI
2.SHAURYA DARNE

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shivraj-09/JSONS_TEAM.git
cd JSONS_TEAM

### 2. Setup the backend

cd backend

python -m venv venv

windows - venv\Scripts\activate
mac - source venv/bin/activate

pip install -r requirements.txt

3. Configure the Gemini API

Create a .env file inside the backend folder:

GEMINI_API_KEY=your_api_key_here

4. Start the backend

From the backend directory:

python app.py

The API will run at:

http://127.0.0.1:5000
5. Start the frontend

Open a new terminal:

cd frontend
python -m http.server 5500

Then open:

http://127.0.0.1:5500
6. Test the system

Try a query such as:

Someone hacked my account and made an unauthorized payment!

The system will automatically:

🧠 Classify the issue
🚨 Determine urgency
😡 Analyze sentiment
💬 Generate a contextual response
🔀 Decide whether human escalation is required
📊 Update the support dashboard
