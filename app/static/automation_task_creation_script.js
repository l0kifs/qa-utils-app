function toggleTestFields() {
    const taskTypeSelect = document.getElementById("task_type");
    const testFields = document.getElementById("testFields");
    const testKey = document.getElementById("test_key");
    const testSuite = document.getElementById("test_suite");
    
    const selectedOption = taskTypeSelect.options[taskTypeSelect.selectedIndex];
    const optgroup = selectedOption.closest("optgroup");
    const isTestRelated = optgroup && (optgroup.id === "test_group");

    if (isTestRelated) {
        testFields.style.display = "block";
        testKey.setAttribute("required", "required");
        testSuite.setAttribute("required", "required");
    } else {
        testFields.style.display = "none";
        testKey.removeAttribute("required");
        testSuite.removeAttribute("required");
    }
}


document.getElementById("submit_button").addEventListener("click", async function () {
    const loginForm = document.getElementById("loginForm");
    const taskForm = document.getElementById("taskForm");
    
    if (!loginForm.checkValidity()) {
        loginForm.reportValidity();
        return;
    }
    if (!taskForm.checkValidity()) {
        taskForm.reportValidity();
        return;
    }

    const loginData = new FormData(loginForm);
    const taskData = new FormData(taskForm);
    const combinedData = new FormData();
    for (let [key, value] of loginData.entries()) {
        combinedData.append(key, value);
    }
    for (let [key, value] of taskData.entries()) {
        combinedData.append(key, value);
    }
    const jsonData = Object.fromEntries(combinedData.entries());
    const resultText = document.getElementById("result");

    try {
        const response = await fetch('/api/create_automation_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jsonData),
        });

        const result = await response.json();

        resultText.style.color = response.ok ? "green" : "red";
        resultText.style.display = "block";
        resultText.textContent = result.detail;
    } catch (error) {
        resultText.style.color = "red";
        resultText.style.display = "block";
        resultText.textContent = error;
    }
});


// Handle form submission via AJAX
// document.getElementById("taskForm").addEventListener("submit", async function (event) {
//     event.preventDefault(); // Prevent the default form submission

//     const formData = new FormData(event.target);
//     const jsonData = Object.fromEntries(formData.entries());
//     const resultText = document.getElementById("result");

//     console.log(jsonData);

//     try {
//         const response = await fetch('/api/create_automation_task', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(jsonData),
//         });

//         const result = await response.json();

//         resultText.style.color = response.ok ? "green" : "red";
//         resultText.style.display = "block";
//         resultText.textContent = result.detail;
//     } catch (error) {
//         resultText.style.color = "red";
//         resultText.style.display = "block";
//         resultText.textContent = error;
//     }
// });
