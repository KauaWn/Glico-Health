document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".tipoPaciente-button");

    buttons.forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();

            buttons.forEach(btn => btn.classList.remove("selecao"));
            button.classList.add("selecao");

            document.querySelectorAll("input[name='tipo_paciente']").forEach(radio => {
                radio.checked = false;
            });

            const tipo = button.getAttribute("data-role");
            const radio = document.getElementById(`check-${tipo}`);
            if (radio) {
                radio.checked = true;
            }
        });
    });
});