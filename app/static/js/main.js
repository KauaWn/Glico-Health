document.addEventListener("DOMContentLoaded", () => {
    const botaoAvancar = document.querySelector("#avance");

    if (botaoAvancar) {
        botaoAvancar.addEventListener("click", () => {
            window.location.href = "/cadastro"; 
        });
    }
});