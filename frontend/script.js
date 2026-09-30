const API_URL = "http://127.0.0.1:8000";

async function analyzeSystem(metrics) {
    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(metrics)
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        const data = await response.json();

        updateDashboard(data, metrics);

    } catch (error) {
        console.error(error);

        document.getElementById("systemStatus").textContent = "OFFLINE";
        document.getElementById("systemStatus").className =
            "badge critical";

        addEvent("Unable to connect to OptiForge API.");
    }
}


function updateDashboard(data, metrics) {

    // Metrics
    document.getElementById("cpuValue").textContent =
        `${Math.round(metrics.cpu_usage * 100)}%`;

    document.getElementById("memoryValue").textContent =
        `${Math.round(metrics.memory_usage * 100)}%`;

    document.getElementById("responseValue").textContent =
        `${metrics.response_time.toFixed(2)} s`;

    document.getElementById("errorValue").textContent =
        `${Math.round(metrics.error_rate * 100)}%`;

    document.getElementById("cpuBar").style.width =
        `${metrics.cpu_usage * 100}%`;

    document.getElementById("memoryBar").style.width =
        `${metrics.memory_usage * 100}%`;


    // System status
    const status = document.getElementById("systemStatus");
    const statusTitle = document.getElementById("statusTitle");
    const statusMessage = document.getElementById("statusMessage");
    const statusIcon = document.getElementById("statusIcon");

    status.textContent = data.status.toUpperCase();

    if (data.status === "healthy") {

        status.className = "badge healthy";

        statusTitle.textContent =
            "System operating normally";

        statusMessage.textContent =
            "No active anomalies detected.";

        statusIcon.textContent = "✓";

    } else if (data.status === "recovered") {

        status.className = "badge healthy";

        statusTitle.textContent =
            "Issue detected and recovered";

        statusMessage.textContent =
            "OptiForge automatically handled the detected anomaly.";

        statusIcon.textContent = "✓";

    } else {

        status.className = "badge critical";

        statusTitle.textContent =
            "Recovery failed";

        statusMessage.textContent =
            "The system requires further investigation.";

        statusIcon.textContent = "!";
    }


    // Detection
    const anomalies = data.detection?.anomalies || [];

    document.getElementById("issue").textContent =
        anomalies.length > 0
            ? anomalies.join(", ")
            : "None";


    // Decision
    if (data.decision) {

        document.getElementById("agent").textContent =
            data.decision.agent;

        document.getElementById("action").textContent =
            data.decision.action;

        document.getElementById("score").textContent =
            Number(data.decision.score).toFixed(3);

    } else {

        document.getElementById("agent").textContent =
            "None";

        document.getElementById("action").textContent =
            "No action";

        document.getElementById("score").textContent =
            "--";
    }


    // Recovery
    const recovery = data.recovery;

    if (recovery) {

        document.getElementById("recoveryIcon").textContent =
            recovery.verified ? "✓" : "!";

        document.getElementById("recoveryTitle").textContent =
            recovery.verified
                ? "Recovery verified"
                : "Recovery failed";

        document.getElementById("recoveryMessage").textContent =
            recovery.message;

    } else {

        document.getElementById("recoveryIcon").textContent =
            "✓";

        document.getElementById("recoveryTitle").textContent =
            "No recovery required";

        document.getElementById("recoveryMessage").textContent =
            "The system is operating normally.";
    }


    // Event log
    if (anomalies.length > 0) {

        addEvent(
            `Detected: ${anomalies.join(", ")}`
        );

        if (data.decision) {

            addEvent(
                `Agent ${data.decision.agent} selected → ${data.decision.action}`
            );
        }

        if (recovery) {

            addEvent(
                recovery.verified
                    ? "✓ Recovery successfully verified."
                    : "⚠ Recovery verification failed."
            );
        }

    } else {

        addEvent("System checked — no anomalies detected.");
    }
}


function simulate(type) {

    let metrics;

    switch (type) {

        case "cpu":

            metrics = {
                cpu_usage: 0.95,
                memory_usage: 0.50,
                response_time: 0.5,
                error_rate: 0.02,
                service_available: true
            };

            break;


        case "memory":

            metrics = {
                cpu_usage: 0.40,
                memory_usage: 0.95,
                response_time: 0.5,
                error_rate: 0.02,
                service_available: true
            };

            break;


        case "failure":

            metrics = {
                cpu_usage: 0.40,
                memory_usage: 0.50,
                response_time: 0.5,
                error_rate: 0.02,
                service_available: false
            };

            break;


        default:

            metrics = {
                cpu_usage: 0.25,
                memory_usage: 0.50,
                response_time: 0.1,
                error_rate: 0.00,
                service_available: true
            };
    }

    analyzeSystem(metrics);
}


function addEvent(message) {

    const log = document.getElementById("eventLog");

    const event = document.createElement("div");

    event.className = "event";

    event.innerHTML = `
        <span>●</span>
        <span>${message}</span>
    `;

    log.prepend(event);
}


// Initial dashboard state

simulate("healthy");