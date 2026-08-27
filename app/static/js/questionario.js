const buttons = document.querySelectorAll(".role-button");
const multipleSelection = true;

buttons.forEach(button => {
    button.addEventListener("click", () => {
        // Múltipla ou única seleção visual
        if (!multipleSelection) {
            buttons.forEach(otherButton => otherButton.classList.remove("selecao"));
            button.classList.add("selecao");
        } else {
            button.classList.toggle("selecao");
        }

        const selectedRoles = [];
        document.querySelectorAll(".role-button.selecao").forEach(selectedButton => {
            selectedRoles.push(selectedButton.dataset.role); // Puxa 'paciente', 'cuidador', 'responsavel'
        });
        
        console.log("Papéis selecionados no clique:", selectedRoles);

        document.querySelectorAll("input[name='papeis']").forEach(checkbox => {
            checkbox.checked = false;
        });

        // 2. Marca apenas os correspondentes aos botões que estão ativos (.selecao)
        selectedRoles.forEach(role => {
            const hiddenCheckbox = document.getElementById(`check-${role}`); // Procura 'check-paciente', etc.
            if (hiddenCheckbox) {
                hiddenCheckbox.checked = true;
                console.log(`Checkbox do Flask '${role}' marcado com sucesso!`);
            }
        });
    });
});

const btnContinuar = document.getElementById("btnContinuar");

document.addEventListener("DOMContentLoaded", () => {
    const roleButtons = document.querySelectorAll(".role-button");

    roleButtons.forEach(button => {
        button.addEventListener("click", () => {
            roleButtons.forEach(b => b.classList.remove("selected"));
            
            button.classList.add("selected");

            const tipo = button.getAttribute("data-tipo");
            const radio = document.getElementById(`radio-${tipo}`);
            if (radio) {
                radio.checked = true;
            }
        });
    });
});