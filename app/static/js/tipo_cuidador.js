document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".tipoCuidador-button");

    buttons.forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault();
            
            // Remove a classe "selecao" de todos os botões
            buttons.forEach(btn => btn.classList.remove("selecao"));
            
            // Adiciona a classe "selecao" ao botão clicado
            button.classList.add("selecao");

            // Marca o radio correspondente
            const tipo = button.getAttribute("data-role");
            const radio = document.getElementById(`check-${tipo}`);
            if (radio) {
                radio.checked = true;
                console.log(`Radio 'check-${tipo}' selecionado com sucesso!`);
            }
        });
    });
});
