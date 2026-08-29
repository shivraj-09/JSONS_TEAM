const API_URL = "http://127.0.0.1:8000/support";

const input = document.getElementById("queryInput");
const button = document.getElementById("sendButton");
const messages = document.getElementById("chatMessages");

input.addEventListener("keydown", function (event) {

    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendQuery();
    }

});


async function sendQuery() {

    const query = input.value.trim();

    if (!query) {
        return;
    }

    addMessage(query, "user");

    input.value = "";

    button.disabled = true;
    button.querySelector("span").textContent = "Analyzing...";

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: query
            })

        });


        if (!response.ok) {
            throw new Error("Backend request failed");
        }


        const data = await response.json();

        displayResult(data);


    } catch (error) {

        console.error(error);

        addMessage(
            "Sorry, I couldn't connect to the AI support system. Please make sure the backend is running.",
            "ai"
        );

    } finally {

        button.disabled = false;
        button.querySelector("span").textContent = "Analyze & Send";

    }
}


function addMessage(text, type) {

    const wrapper = document.createElement("div");

    wrapper.className =
        type === "user"
            ? "message user-message"
            : "message ai-message";


    const avatar = document.createElement("div");

    avatar.className = "avatar";
    avatar.textContent = type === "user" ? "👤" : "✦";


    const bubble = document.createElement("div");

    bubble.className = "bubble";


    const label = document.createElement("span");

    label.className = "message-label";
    label.textContent =
        type === "user"
            ? "Customer"
            : "SupportAI";


    const paragraph = document.createElement("p");

    paragraph.textContent = text;


    bubble.appendChild(label);
    bubble.appendChild(paragraph);


    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);


    messages.appendChild(wrapper);

    messages.scrollTop = messages.scrollHeight;
}


function displayResult(data) {

    const analysis = data.analysis;
    const ticket = data.ticket;


    // Add AI response to chat
    addMessage(
        analysis.response,
        "ai"
    );


    // Hide empty state
    document
        .getElementById("emptyState")
        .classList.add("hidden");

    document
        .getElementById("analysisContent")
        .classList.remove("hidden");


    // Basic analysis
    document.getElementById("category").textContent =
        analysis.category;

    document.getElementById("urgency").textContent =
        analysis.urgency;

    document.getElementById("sentiment").textContent =
        analysis.sentiment;


    // Decision
    const decision =
        document.getElementById("decision");

    const decisionBox =
        document.getElementById("decisionBox");


    if (analysis.needs_escalation) {

        decision.textContent =
            "Human Escalation Required";

        decisionBox.style.background =
            "#1c0808";

        decisionBox.style.borderColor =
            "#7f1d1d";

        document.querySelector(".decision-icon").textContent =
            "🚨";

    } else {

        decision.textContent =
            "Auto-resolved";

        decisionBox.style.background =
            "#052e16";

        decisionBox.style.borderColor =
            "#166534";

        document.querySelector(".decision-icon").textContent =
            "✓";
    }


    // Reason
    document.getElementById("reason").textContent =
        analysis.escalation_reason ||
        "No escalation required. The AI determined that the issue can be handled automatically.";


    // Ticket
    const ticketBox =
        document.getElementById("ticketBox");


    if (ticket) {

        ticketBox.classList.remove("hidden");

        document.getElementById("ticketId").textContent =
            ticket.ticket_id;

        document.getElementById("ticketPriority").textContent =
            ticket.priority;

        document.getElementById("ticketTeam").textContent =
            ticket.assigned_to;

    } else {

        ticketBox.classList.add("hidden");

    }

}