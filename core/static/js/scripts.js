document.addEventListener("DOMContentLoaded", function () {
    // Form validation
    const forms = document.querySelectorAll("form");
    forms.forEach((form) => {
        form.addEventListener("submit", function (event) {
            let valid = true;
            const inputs = form.querySelectorAll("input, textarea");
            
            inputs.forEach((input) => {
                if (input.hasAttribute("required") && input.value.trim() === "") {
                    valid = false;
                    input.classList.add("is-invalid");
                } else {
                    input.classList.remove("is-invalid");
                }
            });

            if (!valid) {
                event.preventDefault();
                alert("Please fill in all required fields.");
            }
        });
    });

    // Show pop-up notification on form submission
    const formWithPopup = document.querySelector("form");
    if (formWithPopup) {
        formWithPopup.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevents actual submission for testing
            alert("Form submitted successfully!");
            this.submit(); // Uncomment this line when ready for real submissions
        });
    }
});
