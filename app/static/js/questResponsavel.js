document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".tipoPaciente-button");
    const relationContainer = document.getElementById("relacaoResponsavelCampo");
    const relationSelect = document.getElementById("relacaoResponsavel");
    const relations = ["Pai", "Mãe", "Tia", "Tio", "Avó", "Avô", "Outro"];
    const relationsByType = {
        menor_idade: relations,
        curatelado: relations,
    };

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            buttons.forEach(btn => btn.classList.remove("selecao"));
            button.classList.add("selecao");

            document.querySelectorAll("input[name='tipo_responsavel']").forEach(radio => {
                radio.checked = false;
            });

            const tipo = button.getAttribute("data-role");
            const radio = document.getElementById(`check-${tipo}`);
            if (radio) {
                radio.checked = true;
            }

            relationSelect.replaceChildren();
            relationsByType[tipo].forEach((relacao, index) => {
                relationSelect.add(new Option(relacao, relacao, index === 0, index === 0));
            });
            relationContainer.classList.remove("d-none");
            relationSelect.disabled = false;
        });
    });
});