// Toggle form visibility
function toggleForm(formId) {
    const form = document.getElementById(formId);
    if (form.style.display === 'none') {
        form.style.display = 'block';
        form.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } else {
        form.style.display = 'none';
    }
}

// Toggle transaction fields based on type
function toggleTransactionFields() {
    const transType = document.getElementById('transType').value;
    const singleField = document.getElementById('singleAccountField');
    const transferFields = document.getElementById('transferFields');
    const singleAccount = document.getElementById('singleAccount');
    const fromAccount = document.getElementById('fromAccount');
    const toAccount = document.getElementById('toAccount');
    
    // Reset all fields
    singleField.style.display = 'none';
    transferFields.style.display = 'none';
    singleAccount.removeAttribute('required');
    fromAccount.removeAttribute('required');
    toAccount.removeAttribute('required');
    
    // Show relevant fields
    if (transType === 'Deposit' || transType === 'Withdraw') {
        singleField.style.display = 'block';
        singleAccount.setAttribute('required', 'required');
    } else if (transType === 'Transfer') {
        transferFields.style.display = 'block';
        fromAccount.setAttribute('required', 'required');
        toAccount.setAttribute('required', 'required');
    }
}

// Auto-hide flash messages
document.addEventListener('DOMContentLoaded', function() {
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.transition = 'opacity 0.5s, transform 0.5s';
            flash.style.opacity = '0';
            flash.style.transform = 'translateX(100%)';
            setTimeout(() => flash.remove(), 500);
        }, 5000);
    });
});

// Format CNIC input
document.addEventListener('DOMContentLoaded', function() {
    const cnicInputs = document.querySelectorAll('input[name="cnic"]');
    cnicInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 5) {
                value = value.slice(0, 5) + '-' + value.slice(5);
            }
            if (value.length > 13) {
                value = value.slice(0, 13) + '-' + value.slice(13);
            }
            e.target.value = value.slice(0, 15);
        });
    });
});
