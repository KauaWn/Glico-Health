document.querySelectorAll('.mostrarSenha').forEach((togglePasswordButton) => {
    const passwordInput = togglePasswordButton.closest('.campoLogin')?.querySelector('input[type="password"], input[type="text"]');
    if (!passwordInput) return;

    const passwordIcon = togglePasswordButton.querySelector('i');

    togglePasswordButton.addEventListener('click', () => {
        const isVisible = passwordInput.type === 'text';
        passwordInput.type = isVisible ? 'password' : 'text';
        togglePasswordButton.setAttribute('aria-label', isVisible ? 'Mostrar senha' : 'Ocultar senha');
        togglePasswordButton.setAttribute('aria-pressed', String(!isVisible));

        if (passwordIcon) {
            passwordIcon.classList.toggle('fa-eye-slash', isVisible);
            passwordIcon.classList.toggle('fa-eye', !isVisible);
        }
    });
});