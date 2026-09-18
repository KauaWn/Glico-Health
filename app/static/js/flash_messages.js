document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-auto-dismiss='true']").forEach((mensagem) => {
        window.requestAnimationFrame(() => {
            mensagem.classList.add("show");
        });

        window.setTimeout(() => {
            mensagem.classList.remove("show");
            window.setTimeout(() => {
                mensagem.remove();
            }, 300);
        }, 4000);
    });
});
