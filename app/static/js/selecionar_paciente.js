document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("modalTrocarPaciente");
    const openButton = document.getElementById("abrirTrocaPaciente");
    if (!modal || !openButton) return;

    const closeButton = modal.querySelector("[data-fechar-troca]");
    const patientSelect = modal.querySelector("select");

    const closeModal = () => {
        modal.hidden = true;
        openButton.focus();
    };

    openButton.addEventListener("click", () => {
        modal.hidden = false;
        patientSelect.focus();
    });
    closeButton.addEventListener("click", closeModal);
    modal.addEventListener("click", (event) => {
        if (event.target === modal) closeModal();
    });
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && !modal.hidden) closeModal();
    });
});
