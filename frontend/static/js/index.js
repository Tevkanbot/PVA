document.addEventListener('DOMContentLoaded', function() {
    if (typeof eel === 'undefined') {
        return;
    }

    // Список элементов, которые должны быть видимыми
    const elementsToCheck = [
        'Input_container',
        'imageButton',
        'imageButton2',
        'Bloak_button',
        'Account_Name',
        'Name_PVA',
        'Account_Photo',
        'menu4-rectangle',
        'chat-window',
        'Button_Send'
    ];

eel.on_load(); // вызов функции после загрузки страницы
function infiniteLoopFunction() {// Функция, которая будет выполняться в бесконечном цикле
    eel.wait_for_commands();
    
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
    
    let microphoneState = false; // Микрофон выключен по умолчанию
    // Отправка начального статуса микрофона
    // Функция переключения микрофона
    function toggleMicrophone() {
        const image2 = document.getElementById('image2');
        if (imageButton2 && image2) {
            // Обновление изображения в зависимости от текущего состояния микрофона
            if (microphoneState) {
                image2.src = 'web/False_micro.png';
            } else {
                image2.src = 'web/True_micro.png';
            }
            microphoneState = !microphoneState;
            // Отправка нового состояния микрофона на сервер
            eel.enableMicrophone(microphoneState); // Удалил .then и .catch, так как сообщения об ошибке не нужны
        }
    }
    // Добавление обработчика события для кнопки
    if (imageButton2) {
        imageButton2.addEventListener('click', toggleMicrophone);
    }
    

    

// Функция для обработки нажатия кнопки
function handleSendButtonClick() {
    const inputField = document.getElementById('Input_text');// Получаем значение текста из поля ввода
    const inputValue = inputField.value.trim(); // Удаляем пробелы в начале и конце строки
    if (inputValue !== '') {
        send_Message_Input(inputValue);// Запускаем функцию отправки сообщения
        inputField.value = '';// Очищаем поле ввода
    }
}
function handleKeyDown(event) {
    if (event.key === 'Enter') {
        handleSendButtonClick();
    }
}
function send_Message_Input(message) {// Функция для отправки сообщения (добавьте вашу логику здесь)
    eel.send_Message_Input(message);
    // Добавьте здесь логику для отправки сообщения
}
const sendButton = document.getElementById('Button_Send');
sendButton.addEventListener('click', handleSendButtonClick);

const inputField = document.getElementById('Input_text');
inputField.addEventListener('keydown', handleKeyDown);
  }

  otherFunction(); // Вызов другой функции

});

function display_message_in_chat(message) {//Вывод сообщения PVA
    const messageBox = document.getElementById('message-box'); // Получаем контейнер сообщений
    if (!messageBox) { // Проверка наличия контейнера сообщений
        console.error("Message box not found."); // Логируем ошибку, если контейнер не найден
        return; // Выходим из функции
    }
    const messageContainer = document.createElement('div'); // Создаем контейнер для сообщения и иконки
    messageContainer.className = 'message-container'; // Присваиваем класс контейнеру
    const userIcon = document.createElement('div'); // Создаем иконку пользователя
    userIcon.className = 'user-icon'; // Присваиваем класс иконке
    userIcon.textContent = 'PVA'; // Внутри иконки можно разместить любой текст
    const messageContent = document.createElement('div'); // Создаем контейнер для текста сообщения
    messageContent.className = 'message'; // Присваиваем класс контейнеру сообщения
    messageContent.textContent = message; // Устанавливаем текст сообщения
    messageContainer.appendChild(userIcon); // Добавляем иконку в общий контейнер
    messageContainer.appendChild(messageContent); // Добавляем текст сообщения в общий контейнер
    messageBox.appendChild(messageContainer); // Добавляем общий контейнер в основной контейнер
    messageBox.scrollTop = messageBox.scrollHeight; // Прокручиваем до конца
    messageBox.appendChild(messageContainer);
    scrollToBottom(); // Автоматически прокручиваем до конца
}
eel.expose(display_message_in_chat); // Экспонируем функцию для использования с Eel
function display_message_user(message) { // Вывод сообщения пользователя
    const messageBox = document.getElementById('message-box');
    if (!messageBox) {
        console.error("Message box not found.");
        return;
    }
    const messageContainer = document.createElement('div');
    messageContainer.className = 'message-container-user';
    const messageContent = document.createElement('div');
    messageContent.className = 'message-user';
    messageContent.textContent = message;
    const userIcon = document.createElement('div');
    userIcon.className = 'user-icon-message-user';
    // Используем те же инициалы, что и в Account_Photo
    const accountPhoto = document.querySelector('.Account_Photo');
    userIcon.textContent = accountPhoto.textContent; // Устанавливаем инициалы в иконку сообщения
    messageContainer.appendChild(messageContent);
    messageContainer.appendChild(userIcon);
    messageBox.appendChild(messageContainer);
    messageBox.scrollTop = messageBox.scrollHeight;

    scrollToBottom();
}
eel.expose(display_message_user); // Экспонируем функцию для использования с Eel

function scrollToBottom() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
async function updateAccountPhoto() { 
    const screenWidth = window.screen.width;// Получаем размеры экрана
    const screenHeight = window.screen.height;
    const width = 700;// Устанавливаем размеры окна
    const height = 500;
    const left = (screenWidth - width) / 2;// Вычисляем позицию окна
    const top = (screenHeight - height) / 2;
    window.resizeTo(width, height);// Устанавливаем размеры и позицию окна
    window.moveTo(left, top);
    
    const initials = await eel.get_initials_from_json()(); // Получаем инициалы
    const accountPhoto = document.querySelector('.Account_Photo');
    accountPhoto.textContent = initials; // Устанавливаем текст в элементе Account_Photo

}
    window.onload = updateAccountPhoto;// Вызов функции после загрузки страницы


