const buttons = document.querySelectorAll(".role-button");

// true  = permite selecionar vários papéis
// false = permite selecionar apenas um papel
const multipleSelection = true;

buttons.forEach(button => {

    button.addEventListener("click", () => {

        // Seleção única
        if (!multipleSelection) {
            buttons.forEach(otherButton => {
                otherButton.classList.remove("selecao");
            });

            button.classList.add("selecao");
        }

        // Múltipla seleção
        else {
            button.classList.toggle("selecao");
        }

        const selectedRoles = [];
        document
            .querySelectorAll(".role-button.selecao")
            .forEach(selectedButton => {

                selectedRoles.push(selectedButton.dataset.role);

            });
        console.log("Papéis selecionados:", selectedRoles);
    });

});