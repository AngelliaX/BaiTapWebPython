
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

const settingsModal = document.getElementById('modal-settings');
const editModal = document.getElementById('modal-edit');
const deleteModal = document.getElementById('modal-delete');

function openSettingsModal(event) {
    event.stopPropagation();
    settingsModal.style.display = 'block';
}

function closeSettingsModal() {
    settingsModal.style.display = 'none';
}

function editPost() {
    closeSettingsModal();
    editModal.style.display = 'block';
}

function deletePost() {
    closeSettingsModal();
    deleteModal.style.display = 'block';
}

function closeEditModal() {
    editModal.style.display = 'none';
}

function closeDeleteModal() {
    deleteModal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == settingsModal) {
        closeSettingsModal();
    }
    if (event.target == editModal) {
        closeEditModal();
    }
    if (event.target == deleteModal) {
        closeDeleteModal();
    }
}

