
  const ctx = document.getElementById('graficoNivelGlicemico').getContext('2d');

  const gradient = ctx.createLinearGradient(0, 0, 0, 180);
  gradient.addColorStop(0, 'rgba(255, 188, 220, 0.6)');
  gradient.addColorStop(1, 'rgba(101, 90, 124, 0.05)');

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
    document.querySelectorAll('.btn-outline-purple').forEach(btn => btn.classList.remove('active'));
    botaoClicado.classList.add('active');
    meuGrafico.data.labels = dadosFiltros[periodo].labels;
    meuGrafico.data.datasets[0].data = dadosFiltros[periodo].valores;
    meuGrafico.update();
  }

  const ctxPeDiabetico = document.getElementById('graficoPeDiabetico').getContext('2d');
  const itrValores = [0.8, 1.2, 1.9, 2.1, 2.2, 2.5, 1.4];
  const itrCores = itrValores.map(valor => {
    if (valor > 2.2) return 'rgba(255, 188, 220, 0.9)';
    if (valor >= 1.8) return 'rgba(245, 204, 76, 0.9)';
    return 'rgba(101, 90, 124, 0.85)';
  });
  const itrBordas = itrValores.map(valor => {
    if (valor > 2.2) return '#d895b5';
    if (valor >= 1.8) return '#d1aa27';
    return '#655A7C';
  });

  new Chart(ctxPeDiabetico, {
    type: 'bar',
    data: {
      labels: ['01/09', '03/09', '05/09', '08/09', '10/09', '12/09', '15/09'],
      datasets: [{
        label: 'ITR (°C)',
        data: itrValores,
        backgroundColor: itrCores,
        borderColor: itrBordas,
        borderWidth: 1,
        borderRadius: 8,
        barThickness: 22
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: '#8d829e', font: { size: 11 } } },
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(226, 232, 240, 0.6)' },
          ticks: { color: '#8d829e', font: { size: 11 } },
          title: { display: true, text: 'ITR (°C)', color: '#8d829e', font: { size: 10 } }
        }
      }
    }
  });