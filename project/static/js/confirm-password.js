const passwordInput = document.getElementById("id_auth-password");
const confirmPasswordInput = document.getElementById("id_confirm-password");

document.getElementById("sing-up-form").addEventListener("submit", function(event) {

    if (passwordInput.value !== confirmPasswordInput.value) {
        event.preventDefault();
        confirmPasswordInput.setCustomValidity(
            "Password confirmation does not match the password entered above."
        );
    } else {
        confirmPasswordInput.setCustomValidity("");
    }
});