document.addEventListener('DOMContentLoaded', function () {
    const calendarEl = document.getElementById('calendario');

    const calendar = new FullCalendar.Calendar(calendarEl, {
        themeSystem: 'monarch', 
        initialView: 'dayGridMonth',
        locale: 'pt-br', 
        headerToolbar: {
            left: 'prev',
            center: 'title',
            right: 'next'
        },
        height: 'auto',
        contentHeight: 320,
        fixedWeekCount: false,
        events: [
            {
                title: 'Exame',
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