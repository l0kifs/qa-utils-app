document.getElementById("submit-button").addEventListener("click", async () => {
    const effort = document.getElementById("effort").value;
    const clarity = document.getElementById("clarity").value;
    const risks = document.getElementById("risks").value;
    const experience = document.getElementById("experience").value;
    const communication = document.getElementById("communication").value;
    const riskLevel = document.getElementById("risk-level").value;

    const response = await fetch("/api/estimate_task", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            criteria: {
                effort: Number(effort),
                clarity: Number(clarity),
                risks: Number(risks),
                experience: Number(experience),
                communication: Number(communication)
            },
            risk_level: Number(riskLevel),
        }),
    });

    const resultDiv = document.getElementById("result");
    if (response.ok) {
        const data = await response.json();
        resultDiv.innerHTML = `<h2>Results</h2>
                               <p>Complexity: ${data.complexity}</p>
                               <p>Estimated Time: ${data.estimated_time} hours</p>`;
    } else {
        const error = await response.json();
        resultDiv.innerHTML = `<p style="color: red;">Error: ${error.detail}</p>`;
    }
});