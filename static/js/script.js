
// Submit the form when the priority is changed
document.getElementById('sortBy').addEventListener('change', function () {
    document.getElementById('filterForm').submit();
});

//Own filter automation
document.getElementById('own_tickets').addEventListener('change', function () {
    document.getElementById('ownTicketsForm').submit();
    console.log('Submitted')
});
