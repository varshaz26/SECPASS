

function generatePassword() {
    const passwordField = document.getElementById('password');
    const length = 12; // Adjust length of generated password here
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()";
    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }

    passwordField.value = password;
}


function toggleView(id) {
    const input = document.getElementById(id);
    const icon = document.getElementById(`icon-${id}`);
    if (input.type === "password") {
        input.type = "text";  // Show password
        icon.classList.remove("fa-eye");  // Change icon to "open eye"
        icon.classList.add("fa-eye-slash");  // Add "closed eye" icon
    } else {
        input.type = "password";  // Hide password
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
    }
}

