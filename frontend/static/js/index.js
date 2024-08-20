document.addEventListener('DOMContentLoaded', function() {
    if (typeof eel === 'undefined') {
        return;
    }

    // Список элементов, которые должны быть видимыми
    const elementsToCheck = [
        'menu1-rectangle',
        'imageButton',
        'imageButton2',
        'chat-window',
        'menu5-rectangle',
        'menu6-rectangle',
        'menu7-rectangle',
        'menu8-rectangle',
        'menu9-rectangle'
    ];

eel.on_load(); // вызов функции после загрузки страницы
function infiniteLoopFunction() {// Функция, которая будет выполняться в бесконечном цикле
    eel.search_and_send_message();
    
    requestAnimationFrame(infiniteLoopFunction);// Запрашиваем следующий кадр
  }
  requestAnimationFrame(infiniteLoopFunction);// Запускаем функцию

  function otherFunction() {// Эта функция тоже может работать одновременно
        elementsToCheck.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.style.display = 'block';
        } else {
            console.error(`Element with id '${id}' not found.`);
        }
    });

    const button = document.getElementById('imageButton');
    const image = document.getElementById('image');
    const imageButton2 = document.getElementById('imageButton2');
    if (button && image) {
        let previousImageSource = image.src;
        button.addEventListener('click', function() {
            if (image.src.endsWith('True_m.png')) {
                image.src = 'web/False_m.png'; // Исправлена опечатка
                previousImageSource = 'web/True_m.png';
                eel.toggle_sound('Выключение звука') // Удалил .then и .catch, так как сообщения об ошибке не нужны
            } else {
                image.src = previousImageSource;
                eel.toggle_sound('Включение звука') // Удалил .then и .catch, так как сообщения об ошибке не нужны
            }
        });
    } 
    let microphoneState = true;   
    function toggleMicrophone() {
        const image2 = document.getElementById('image2');
        if (imageButton2 && image2) {
            if (microphoneState) {
                image2.src = 'web/False_micro.png';
            } else {
                image2.src = 'web/True_micro.png';
            }
            microphoneState = !microphoneState;
            
            eel.enableMicrophone(microphoneState) // Удалил .then и .catch, так как сообщения об ошибке не нужны
        }
    }
    if (imageButton2) {
        imageButton2.addEventListener('click', toggleMicrophone);
    }  
  }
  otherFunction(); // Вызов другой функции


});

function display_message_in_chat(message) {
    const messageBox = document.getElementById('message-box');
    if (!messageBox) {
        console.error("Message box not found.");
        return;
    }

    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    newMessage.className = 'message';
    messageBox.appendChild(newMessage);
    messageBox.scrollTop = messageBox.scrollHeight; // Немедленно прокручиваем до конца
}
eel.expose(display_message_in_chat);