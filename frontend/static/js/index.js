document.addEventListener('DOMContentLoaded', function() {
    // Проверка наличия eel
    if (typeof eel === 'undefined') {
        console.error('Eel is not defined. Make sure eel.js is loaded correctly.');
        return;
    }

    // Все элементы загружены и отображаются
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

    elementsToCheck.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.style.display = 'block';
        }
    });

    // Обработчики событий
    const button = document.getElementById('imageButton');
    const image = document.getElementById('image');
    const imageButton2 = document.getElementById('imageButton2');

    if (button && image) {
        let previousImageSource = image.src;

        button.addEventListener('click', function() {
            if (image.src.endsWith('True_m.png')) {
                image.src = 'web/Folse_m.png';
                previousImageSource = 'web/True_m.png';
                eel.toggle_sound('Выключение звука')();
            } else {
                image.src = previousImageSource;
                eel.toggle_sound('Включение звука')();
            }
        });
    }

    let microphoneState = true;

    function toggleMicrophone() {
        const image2 = document.getElementById('image2');
        if (imageButton2 && image2) {
            if (microphoneState) {
                image2.src = 'web/Folse_micro.png';
            } else {
                image2.src = 'web/True_micro.png';
            }
            microphoneState = !microphoneState;
            eel.enableMicrophone(microphoneState)();
        }
    }

    if (imageButton2) {
        imageButton2.addEventListener('click', toggleMicrophone);
    }

    // Вызов функции для отправки сообщения после загрузки страницы
    eel.on_load();  // вызов функции после загрузки страницы
});

// Экспонируем функцию display_message_in_chat для использования в Python
function display_message_in_chat(message) {
    const messageBox = document.getElementById('message-box');
    if (!messageBox) {
        console.error('Message box element not found');
        return;
    }

    const newMessage = document.createElement('div');
    newMessage.textContent = message;
    newMessage.className = 'message';
    messageBox.appendChild(newMessage);
    messageBox.scrollTop = messageBox.scrollHeight;
}

// Убедитесь, что эта строка не вызывает ошибок
eel.expose(display_message_in_chat);
