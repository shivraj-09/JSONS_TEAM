import os
import json
import uuid
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

SYSTEM_PROMPT = """
You are an AI Customer Support Agent.

Analyze the customer's message and:

1. Classify the issue.
2. Determine urgency.
3. Detect sentiment.
4. Decide whether human escalation is required.
5. Explain the escalation decision.
6. Generate a helpful professional response.

Categories:
- Order
- Payment
- Refund
- Account
- Technical Issue
- Delivery
- Product
- Security/Fraud
- General Inquiry
- Other

Urgency:
- LOW
- MEDIUM
- HIGH
- CRITICAL

Escalate when:
- There is suspected fraud, unauthorized access, or a security issue.
- There is a serious financial issue.
- The issue is critical or time-sensitive.
- The customer repeatedly tried to resolve the issue.
- The customer explicitly requests human support for a serious issue.

Return ONLY valid JSON:

{
  "category": "...",
  "urgency": "LOW/MEDIUM/HIGH/CRITICAL",
  "sentiment": "Positive/Neutral/Frustrated/Angry",
  "needs_escalation": true,
  "escalation_reason": "...",
  "response": "..."
}
"""


def customer_support_agent(customer_query):

    prompt = SYSTEM_PROMPT + f"""

CUSTOMER QUERY:
{customer_query}

Analyze the query and return ONLY the required JSON.
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "temperature": 0.2,
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()
    text = data["choices"][0]["message"]["content"]

    cleaned = text.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned)


def apply_escalation_guardrails(query, result):

    query_lower = query.lower()

    critical_keywords = [
        "hacked",
        "hack",
        "unauthorized",
        "fraud",
        "stolen",
        "account compromised",
        "identity theft",
    ]

    financial_keywords = [
        "charged twice",
        "duplicate charge",
        "money deducted",
        "payment deducted",
        "wrong charge",
        "refund",
    ]

    if any(keyword in query_lower for keyword in critical_keywords):

        result["needs_escalation"] = True
        result["urgency"] = "CRITICAL"

        if not result.get("escalation_reason"):
            result["escalation_reason"] = (
                "Security or fraud-related issue requires human intervention."
            )

    elif any(keyword in query_lower for keyword in financial_keywords):

        if result["urgency"] in ["HIGH", "CRITICAL"]:
            result["needs_escalation"] = True

    return result


def create_escalation_ticket(query, result):

    ticket_id = "TKT-" + str(uuid.uuid4())[:8].upper()

    return {
        "ticket_id": ticket_id,
        "created_at": datetime.now().isoformat(),
        "priority": result["urgency"],
        "category": result["category"],
        "customer_query": query,
        "sentiment": result["sentiment"],
        "reason": result["escalation_reason"],
        "status": "OPEN",
        "assigned_to": "Human Support Team",
    }


def process_customer_query(customer_query):

    result = customer_support_agent(customer_query)

    result = apply_escalation_guardrails(
        customer_query,
        result
    )

    ticket = None

    if result["needs_escalation"]:
        ticket = create_escalation_ticket(
            customer_query,
            result
        )

    return {
        "query": customer_query,
        "analysis": result,
        "ticket": ticket,
    }