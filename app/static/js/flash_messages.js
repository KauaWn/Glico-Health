(() => {
    const initializeNotice = (aviso) => {
        let timer;
        const dismiss = () => {
            window.clearTimeout(timer);
            aviso.classList.add("is-leaving");
            window.setTimeout(() => aviso.remove(), 250);
        };

        aviso.querySelector("[data-dismiss-notice]")?.addEventListener("click", dismiss);
        window.requestAnimationFrame(() => aviso.classList.add("is-visible"));
        timer = window.setTimeout(dismiss, 4500);
    };

    window.showNotice = (message, category = "danger") => {
        let container = document.querySelector(".avisos-flutuantes");
        if (!container) {
            container = document.createElement("div");
            container.className = "avisos-flutuantes";
            container.setAttribute("aria-live", "polite");
            container.setAttribute("aria-relevant", "additions");
            document.body.appendChild(container);
        }

        const aviso = document.createElement("div");
        aviso.className = `alert aviso-flutuante alert-${category}`;
        aviso.setAttribute("role", "alert");
        aviso.dataset.autoDismiss = "true";

        const texto = document.createElement("span");
        texto.textContent = message;
        const fechar = document.createElement("button");
        fechar.type = "button";
        fechar.className = "aviso-fechar";
        fechar.dataset.dismissNotice = "";
        fechar.setAttribute("aria-label", "Fechar aviso");
        fechar.textContent = "×";

        aviso.append(texto, fechar);
        container.appendChild(aviso);
        initializeNotice(aviso);
    };

    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll("[data-auto-dismiss='true']").forEach(initializeNotice);
    });
})();
