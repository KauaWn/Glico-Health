document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modalDesativarRelacao");
    const form = document.getElementById("formDesativarRelacao");
    const texto = document.getElementById("modalDesativarTexto");
    if (!modal || !form || !texto) return;

    let triggerButton = null;
    const closeModal = () => {
        modal.hidden = true;
        triggerButton?.focus();
    };

    document.querySelectorAll("[data-desativar-url]").forEach((button) => {
        button.addEventListener("click", () => {
            triggerButton = button;
            form.action = button.dataset.desativarUrl;
            texto.textContent = `Você deixará de ter acesso aos dados de ${button.dataset.pacienteNome}.`;
            modal.hidden = false;
            modal.querySelector("[data-fechar-modal]").focus();
        });
    });

    modal.querySelector("[data-fechar-modal]").addEventListener("click", closeModal);
    modal.addEventListener("click", (event) => {
        if (event.target === modal) closeModal();
    });
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !modal.hidden) closeModal();
    });
});
