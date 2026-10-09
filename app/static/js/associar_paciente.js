document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("associarPacienteForm");
    if (!form) return;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const submitButton = form.querySelector("[type='submit']");
        const originalText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = "Buscando...";

        try {
            const response = await fetch(form.action, {
                method: "POST",
                body: new FormData(form),
                headers: {
                    "Accept": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                },
            });
            const resultado = await response.json();

            if (resultado.success) {
                window.location.assign(resultado.redirect);
                return;
            }

            window.showNotice(resultado.message, "danger");
        } catch {
            window.showNotice("Não foi possível procurar o paciente. Tente novamente.", "danger");
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = originalText;
        }
    });
});