document.addEventListener("DOMContentLoaded", () => {
    const botaoAvancar = document.querySelector("#avance");
    const telaCadastro = document.querySelector("#cadastro");
    const botaoVoltar = document.querySelector("#voltarInicio");

    botaoAvancar.addEventListener("click", () => {
        telaCadastro.classList.add("ativo");
    });

    botaoVoltar.addEventListener("click", () => {
        telaCadastro.classList.remove("ativo");
    });
});