// ? GETTING ALL ELEMENTS
const alerts = document.querySelectorAll('.alert');

// * FUNCTION TO SHOW ALERTS
function showAlerts(index=0) {
    if (index >= alerts.length) return;

    alerts[index].classList.add('show');

    setTimeout(() => {
        alerts[index].classList.remove('show');
        showAlerts(index + 1);
    }, 3000);
}

// | INITIAL CALL TO SHOW ALERTS
setTimeout(() => {showAlerts();}, 100);