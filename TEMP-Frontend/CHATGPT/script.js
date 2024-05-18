// script.js
const notes = document.querySelectorAll('.note');


// add event listeners to task input fields
const taskInput = document.querySelectorAll('#task-input');
const taskLists = document.querySelectorAll('#task-list');

taskInput.forEach((input) => {
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const task = input.value.trim();
            if (task) {
                const taskList = input.nextElementSibling;
                const taskHTML = `
                    <li class="task">
                        <input type="checkbox">
                        <span>${task}</span>
                        <a href="#" class="edit">Edit</a>
                        <a href="#" class="delete">Delete</a>
                    </li>
                `;
                taskList.innerHTML += taskHTML;
                input.value = '';
            }
        }
    });
});

// add event listeners to task list items
taskLists.forEach((taskList) => {
    taskList.addEventListener('click', (e) => {
        if (e.target.classList.contains('edit')) {
            // todo: implement edit functionality
            console.log('Edit task');
        } else if (e.target.classList.contains('delete')) {
            // todo: implement delete functionality
            console.log('Delete task');
        }
    });
});


const ball = document.getElementById('ball');

ball.onmousedown = function(event) {
  const shiftX = event.clientX - ball.getBoundingClientRect().left;
  const shiftY = event.clientY - ball.getBoundingClientRect().top;

  ball.style.position = 'absolute';
  document.body.append(ball);
  moveAt(event.pageX, event.pageY);

  function moveAt(pageX, pageY) {
    ball.style.left = pageX - shiftX + 'px';
    ball.style.top = pageY - shiftY + 'px';
  }

  function onMouseMove(event) {
    moveAt(event.pageX, event.pageY);
  }

  document.addEventListener('mousemove', onMouseMove);

  ball.onmouseup = function() {
    document.removeEventListener('mousemove', onMouseMove);
    ball.onmouseup = null;
  };

  ball.ondragstart = function() {
    return false;
  };

  ball.style.zIndex = 1000;
};

ball.ondragstart = function() {
  return false;
};