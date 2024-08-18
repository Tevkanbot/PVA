document.getElementById('backButton2').style.display = 'none';
document.getElementById('saveButton2').style.display = 'none';
document.getElementById('saveButton').style.display = 'none';

document.getElementById('forwardButton2').addEventListener('click', function() {
eel.forward_button_pressed();  // Вызов функции Python
});


document.getElementById('saveButton2').addEventListener('click', function() {
var input_value_12 = document.getElementById('inputField2').value.trim();
var input_value_22 = document.getElementById('newInputField2').value.trim();

if(input_value_12 || input_value_22) {
    // Отправить данные на сервер
    eel.saveData2(input_value_12, input_value_22)()
        .then(() => {
            // Очистить поля ввода
            document.getElementById('inputField2').value = '';
            document.getElementById('newInputField2').value = '';
        });
}


});
eel.expose(saveData2);
function saveData2(input_value_12, input_value_22) {   
console.log('input_value_12:', input_value_12);
console.log('input_value_22:', input_value_22);

}



function handleForwardButton2() {
        document.getElementById('inner6-rectangle').style.display = 'none';
        document.getElementById('inputField').style.display = 'none';
        document.getElementById('newInputField').style.display = 'none';
        document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добро пожаловать!';
        document.getElementById('nextButton').style.display = 'none';
        document.getElementById('saveButton').style.display = 'none';
        document.getElementById('backButton').style.display = 'none';
        document.getElementById('forwardButton').style.display = 'none';
        document.getElementById('inner7-rectangle').style.display = 'none'; // Показываем прямоугольник с id inner7-rectangle
        document.getElementById('inner8-rectangle').style.display = 'none';
        document.getElementById('inner9-rectangle').style.display = 'none';
        document.getElementById('forwardButton2').style.display = 'none';
        document.getElementById('inner10-rectangle').style.display = 'none';
        document.getElementById('inner-rectangle1').style.display = 'none';
        document.getElementById('innerRectangle').style.display = 'none';
        document.getElementById('secondRectangle').style.display = 'none';
        document.getElementById('inner22-rectangle').style.display = 'none';
        document.getElementById('nameInput').value = '';
        document.getElementById('nameInput').style.display = 'none';
        document.getElementById('thirdRectangle').style.display = 'none';
        // сверху уборка старых объектов
        // появление новых объектов
        window.location.replace('index.html');


    }


function handleBackButton2() {
        document.getElementById('inner6-rectangle').style.display = 'none';
        document.getElementById('inputField').style.display = 'none';
        document.getElementById('newInputField').style.display = 'none';
        document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добро пожаловать!';
        document.getElementById('backButton').style.display = 'block';
        document.getElementById('saveButton').style.display = 'none';
        document.getElementById('forwardButton2').style.display = 'block';
        document.getElementById('backButton2').style.display = 'none';
        document.getElementById('inputField2').style.display = 'none';
        document.getElementById('newInputField2').style.display = 'none';
        document.getElementById('saveButton2').style.display = 'none';
    }

document.getElementById('saveButton').style.display = 'none';
document.getElementById('inner8-rectangle').addEventListener('click', function() {
var name = document.getElementById('nameInput').value;
if(name.trim()) {
    document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добавление сайтов!';
    document.getElementById('inner6-rectangle').style.display = 'block';
    document.getElementById('inputField2').style.display = 'block';
    document.getElementById('newInputField2').style.display = 'block';
    document.getElementById('saveButton2').style.display = 'block';
    document.getElementById('forwardButton').style.display = 'none';
    document.getElementById('backButton2').style.display = 'block';
    document.getElementById('forwardButton2').style.display = 'none';
}
});


function handleForwardButton() {
        document.getElementById('inner6-rectangle').style.display = 'none';
        document.getElementById('inputField').style.display = 'none';
        document.getElementById('newInputField').style.display = 'none';
        document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добро пожаловать!';
        document.getElementById('nextButton').style.display = 'none';
        document.getElementById('saveButton').style.display = 'none';
        document.getElementById('backButton').style.display = 'none';
        document.getElementById('forwardButton').style.display = 'none';
        document.getElementById('inner7-rectangle').style.display = 'block'; // Показываем прямоугольник с id inner7-rectangle
        document.getElementById('inner8-rectangle').style.display = 'block';
        document.getElementById('inner9-rectangle').style.display = 'block';
        document.getElementById('forwardButton').style.display = 'none';

        
    }

    
document.getElementById('saveButton').addEventListener('click', function() {
var input_value_1 = document.getElementById('inputField').value.trim();
var input_value_2 = document.getElementById('newInputField').value.trim();

if(input_value_1 || input_value_2) {
    // Отправить данные на сервер
    eel.saveData(input_value_1, input_value_2)()
        .then(() => {
            // Очистить поля ввода
            document.getElementById('inputField').value = '';
            document.getElementById('newInputField').value = '';
        });
}


});

eel.expose(saveData);
function saveData(input_value_1, input_value_2) {   
console.log('input_value_1:', input_value_1);
console.log('input_value_2:', input_value_2);
}





document.getElementById('saveButton').style.display = 'none';
document.getElementById('innerRectangle').addEventListener('click', function() {
var name = document.getElementById('nameInput').value;
if(name.trim()) {
    document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добавление приложений!';
    document.getElementById('inner6-rectangle').style.display = 'block';
    document.getElementById('inputField').style.display = 'block';
    document.getElementById('newInputField').style.display = 'block';
    document.getElementById('saveButton').style.display = 'block';
    document.getElementById('forwardButton').style.display = 'none';
}
});


document.getElementById('nameInput').addEventListener('input', function() {
    var name = this.value;
    if(name.trim()) {  // Если что-то введено и это не пробелы, показываем кнопку
        document.getElementById('nextButton').style.display = 'block';
    } else {  // Если поле пустое или содержит только пробелы, скрываем кнопку
        document.getElementById('nextButton').style.display = 'none';
    }
});
document.getElementById('innerRectangle').addEventListener('click', function() {
var name = document.getElementById('nameInput').value;
if(name.trim()) {
    document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добавление приложений!';
    document.getElementById('inner6-rectangle').style.display = 'block';
    document.getElementById('inputField').style.display = 'block';
    document.getElementById('newInputField').style.display = 'block';
    document.getElementById('saveButton').style.display = 'block';
    
}
});

document.getElementById('newInputField').addEventListener('input', function() {
        // Здесь можно добавить функционал, аналогичный существующему inputField
    });

    function handleBackButton() {
        document.getElementById('inner6-rectangle').style.display = 'none';
        document.getElementById('inputField').style.display = 'none';
        document.getElementById('newInputField').style.display = 'none';
        document.querySelector('.inner-rectangle .welcome-text').textContent = 'Добро пожаловать!';
        document.getElementById('backButton').style.display = 'block';
        document.getElementById('saveButton').style.display = 'none';
        document.getElementById('forwardButton').style.display = 'block';
        
    }


async function showRectangles() {
    var name = document.getElementById('nameInput').value;
    if(name.trim()) {
        await eel.process_name(name); // Предполагаем, что функция process_name определена в Python
        document.getElementById('innerRectangle').style.display = 'block';
        document.getElementById('secondRectangle').textContent = 'Добавьте свои приложения!';
        document.getElementById('secondRectangle').style.display = 'block';
        document.getElementById('thirdRectangle').textContent = '';
        document.getElementById('thirdRectangle').style.display = 'block';
        document.getElementById('nameInput').disabled = true;
        document.getElementById('nextButton').style.display = 'none';
        document.getElementById('inputField').style.display = 'none'; // Скрываем строку ввода, если она была показана
        
}

 
    }



// Вызов функции при загрузке страницы для первоначальной проверки
document.addEventListener('DOMContentLoaded', function() {
    var name = document.getElementById('nameInput').value;
    document.getElementById('nextButton').style.display = name.trim() ? 'block' : 'none';
});