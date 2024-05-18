
const modal = document.getElementById('modal');

function openModal() {
    if (modal.style.display === 'block') {
        closeModal();
    } else {
        modal.style.display = 'block';
    }
}

function closeModal() {
    modal.style.display = 'none';
}

function submitNote() {
    // Add your submission logic here
    closeModal();
}
