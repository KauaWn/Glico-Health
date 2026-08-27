document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".role-button");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            // Toggle a classe "selecao" no botão clicado
            button.classList.toggle("selecao");

            // Coleta todos os papéis selecionados (botões com classe "selecao")
            const selectedRoles = [];
            document.querySelectorAll(".role-button.selecao").forEach(selectedButton => {
                selectedRoles.push(selectedButton.dataset.role);
            });
            
            console.log("Papéis selecionados:", selectedRoles);

            // Desativa todos os checkboxes
            document.querySelectorAll("input[name='papeis']").forEach(checkbox => {
                checkbox.checked = false;
            });

            // Marca apenas os checkboxes correspondentes aos botões selecionados
            selectedRoles.forEach(role => {
                const hiddenCheckbox = document.getElementById(`check-${role}`);
                if (hiddenCheckbox) {
                    hiddenCheckbox.checked = true;
                    console.log(`Checkbox '${role}' marcado com sucesso!`);
                }
            });
        });
    });
});