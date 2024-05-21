
const modal = document.getElementById('modal');

function openModal(userId) {
    if (modal.style.display === 'block') {
        closeModal();
    } else {
        modal.style.display = 'block';
    }
    document.getElementById("userId1").value = userId;
    console.log("openModal called")
}

function closeModal() {
    modal.style.display = 'none';
}

function submitNote() {
    // Add your submission logic here
    console.log("submit Note Called");
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

function editPost(id, title, data, status, userId) {
    //closeSettingsModal();
    document.getElementById("modal-edit-header").textContent = title;
    document.getElementById("staticBackdropLabel5").value = title;

    document.getElementById("modal-edit-description").value = data;
    document.getElementById("modal-edit-status").value = status;
    console.log("hello", status)
    document.getElementById("todoId").value = id;
    document.getElementById("userId").value = userId;

    editModal.style.display = 'block';
}

function deletePost(id) {
    document.getElementById("idDelete").value = id;
    deleteModal.style.display = 'block';

    //closeSettingsModal();
}

function closeEditModal() {
    editModal.style.display = 'none';
}

function closeDeleteModal() {
    deleteModal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == settingsModal) {
        console.log("caleld here")
        closeSettingsModal();
    }
    if (event.target == editModal) {
        console.log("caleld here 2")
        closeEditModal();
    }
    if (event.target == deleteModal) {
        console.log("caleld here 3")
        closeDeleteModal();
    }
}



document.querySelectorAll('.draggable_custom').forEach(elem => {
      elem.addEventListener('mousedown', function(e) {
        let offsetX = e.clientX - parseInt(window.getComputedStyle(this).left);
        let offsetY = e.clientY - parseInt(window.getComputedStyle(this).top);

        const onMouseMove = (e) => {
          this.style.left = e.clientX - offsetX + 'px';
          this.style.top = e.clientY - offsetY + 'px';
        };

        const onMouseUp = () => {
          document.removeEventListener('mousemove', onMouseMove);
          document.removeEventListener('mouseup', onMouseUp);
        };

        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
      });
    });