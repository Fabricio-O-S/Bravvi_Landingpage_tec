document.addEventListener('DOMContentLoaded', () => {
    // 1. Inicializa Efeitos de Revelação por Scroll (Intersection Observer)
    const revealElements = document.querySelectorAll('.scroll-reveal');
    
    if ('IntersectionObserver' in window) {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target); // Revela apenas uma vez
                }
            });
        }, observerOptions);

        revealElements.forEach(el => {
            el.classList.add('scroll-reveal');
            observer.observe(el);
        });
    } else {
        // Fallback para navegadores sem suporte
        revealElements.forEach(el => el.classList.remove('scroll-reveal'));
    }

    // 2. Máscara de WhatsApp / Telefone Dinâmica ((XX) XXXXX-XXXX)
    const phoneInput = document.getElementById('whatsapp');
    if (phoneInput) {
        phoneInput.addEventListener('input', (e) => {
            let value = e.target.value.replace(/\D/g, ''); // Mantém apenas números
            
            if (value.length > 11) {
                value = value.slice(0, 11); // Limita em 11 dígitos
            }

            if (value.length > 6) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7)}`;
            } else if (value.length > 2) {
                e.target.value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else if (value.length > 0) {
                e.target.value = `(${value}`;
            } else {
                e.target.value = '';
            }
        });
    }

    // 3. Envio Assíncrono do Formulário de Leads (AJAX)
    const leadForm = document.getElementById('leadForm');
    if (leadForm) {
        leadForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Resgata os elementos e valores
            const submitBtn = document.getElementById('submitBtn');
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const whatsapp = document.getElementById('whatsapp').value.trim();
            const industry = document.getElementById('industry').value.trim();
            const message = document.getElementById('message').value.trim();

            // Validação client-side inicial
            let clientErrors = [];
            if (!name) clientErrors.push('O Nome é obrigatório.');
            if (!email) {
                clientErrors.push('O E-mail é obrigatório.');
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                clientErrors.push('Digite um E-mail válido.');
            }
            if (!whatsapp) {
                clientErrors.push('O WhatsApp é obrigatório.');
            } else {
                const cleanedPhone = whatsapp.replace(/\D/g, '');
                if (cleanedPhone.length < 10) {
                    clientErrors.push('O WhatsApp deve ter no mínimo 10 dígitos (DDD + Número).');
                }
            }
            if (!industry || industry === 'Selecione sua indústria') {
                clientErrors.push('Selecione uma Indústria.');
            }
            if (!message) clientErrors.push('A Mensagem é obrigatória.');

            if (clientErrors.length > 0) {
                Swal.fire({
                    icon: 'warning',
                    title: 'Atenção!',
                    html: `<div class="text-left font-sans text-sm text-gray-700">${clientErrors.map(err => `• ${err}`).join('<br>')}</div>`,
                    confirmButtonColor: '#001f56'
                });
                return;
            }

            // Inicia estado de carregamento do botão
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = `
                <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg> Enviando Solicitação...
            `;

            try {
                const response = await fetch('/submit-lead', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: name,
                        email: email,
                        whatsapp: whatsapp,
                        industry: industry,
                        message: message
                    })
                });

                const data = await response.json();

                if (response.ok && data.status === 'success') {
                    // Feedback de sucesso
                    Swal.fire({
                        icon: 'success',
                        title: 'Tudo certo!',
                        text: data.message,
                        confirmButtonColor: '#bc0000',
                        confirmButtonText: 'Excelente'
                    });
                    
                    // Reseta o formulário
                    leadForm.reset();
                } else {
                    // Trata respostas de erro enviadas pelo back-end
                    const errorMsg = data.errors ? data.errors.join('<br>') : data.message;
                    Swal.fire({
                        icon: 'error',
                        title: 'Falha no cadastro',
                        html: `<div class="text-left font-sans text-sm text-gray-700">${errorMsg}</div>`,
                        confirmButtonColor: '#001f56'
                    });
                }
            } catch (err) {
                console.error("Erro na comunicação AJAX:", err);
                Swal.fire({
                    icon: 'error',
                    title: 'Erro de Conexão',
                    text: 'Não foi possível se comunicar com o servidor. Verifique sua conexão e tente novamente.',
                    confirmButtonColor: '#001f56'
                });
            } finally {
                // Restaura botão de envio
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            }
        });
    }
});
