function toggleAboutMe() {
    var aboutMeSection = document.getElementById("about-me");
    aboutMeSection.style.display = aboutMeSection.style.display === "none" ? "block" : "none";
}


document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("contact-form");

    form.addEventListener("submit", function (event) {
        var subject = document.getElementById("subject").value;
        var fname = document.getElementById("fname").value;
        var lname = document.getElementById("lname").value;
        var email = document.getElementById("email").value;
        var phone = document.getElementById("phone").value;
        var message = document.getElementById("message").value;

        var errorMessages = [];

        if (subject.trim() === "") {
            errorMessages.push("Subject is required.");
        }

        if (fname.trim() === "") {
            errorMessages.push("First Name is required.");
        }

        if (lname.trim() === "") {
            errorMessages.push("Last Name is required.");
        }

        if (email.trim() === "") {
            errorMessages.push("Email is required.");
        }

        if (phone.trim() === "") {
            errorMessages.push("Phone Number is required.");
        }

        if (message.trim() === "") {
            errorMessages.push("Message is required.");
        }

        if (errorMessages.length > 0) {
            event.preventDefault();
            var errorContainer = document.getElementById("error-messages");
            errorContainer.innerHTML = "";
            errorMessages.forEach(function (message) {
                var errorElement = document.createElement("div");
                errorElement.className = "alert alert-danger";
                errorElement.textContent = message;
                errorContainer.appendChild(errorElement);
            });
        }
    });
});
