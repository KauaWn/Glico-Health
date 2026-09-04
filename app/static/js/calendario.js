document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendario');

    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br', // Define o idioma para Português
        headerToolbar: {
            left: 'prev',
            center: 'title',
            right: 'next'
        },
        height: 'auto',
        contentHeight: 320,
        fixedWeekCount: false,
        // Exemplo de eventos/registros marcados no calendário
        events: [
            {
                title: 'Glicemia',
                start: '2026-09-10',
                color: '#655A7C'
            },
            {
                title: 'Consulta',
                start: '2026-09-18',
                color: '#FFBCDC',
                textColor: '#655A7C'
            }
        ]
    });

    calendar.render();
});