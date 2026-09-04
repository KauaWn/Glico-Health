
  const ctx = document.getElementById('graficoNivelGlicemico').getContext('2d');

  // Gradiente de fundo
  const gradient = ctx.createLinearGradient(0, 0, 0, 180);
  gradient.addColorStop(0, 'rgba(255, 188, 220, 0.6)');
  gradient.addColorStop(1, 'rgba(101, 90, 124, 0.05)');

  // Conjunto de dados fictícios para cada filtro
  const dadosFiltros = {
    dia: {
      labels: ['06:00', '09:00', '12:00', '15:00', '18:00', '21:00'],
      valores: [90, 125, 95, 140, 100, 85]
    },
    semana: {
      labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
      valores: [110, 98, 135, 105, 115, 90, 102]
    },
    mes: {
      labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4'],
      valores: [108, 112, 99, 105]
    }
  };

  // Instância Inicial do Gráfico
  const meuGrafico = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dadosFiltros.dia.labels,
      datasets: [{
        label: 'mg/dL',
        data: dadosFiltros.dia.valores,
        borderColor: '#655A7C',
        borderWidth: 2.5,
        backgroundColor: gradient,
        fill: true,
        tension: 0.45,
        pointRadius: 3,
        pointBackgroundColor: '#655A7C'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#8d829e', font: { size: 11 } } },
        y: { grid: { color: 'rgba(226, 232, 240, 0.6)' }, ticks: { color: '#8d829e', font: { size: 11 } } }
      }
    }
  });

  // Função acionada ao clicar nos botões de filtro
  function filtrarGrafico(periodo, botaoClicado) {
    // 1. Atualiza a classe 'active' nos botões
    document.querySelectorAll('.btn-outline-purple').forEach(btn => btn.classList.remove('active'));
    botaoClicado.classList.add('active');

    // 2. Atualiza os dados e rótulos do gráfico
    meuGrafico.data.labels = dadosFiltros[periodo].labels;
    meuGrafico.data.datasets[0].data = dadosFiltros[periodo].valores;

    // 3. Renderiza a animação de transição
    meuGrafico.update();
  }