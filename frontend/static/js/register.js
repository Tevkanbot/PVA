document.addEventListener('DOMContentLoaded', function() {
    const nameInput = document.getElementById('nameInput');
    const nextButton = document.getElementById('nextButton');
    const secondRectangle = document.getElementById('secondRectangle');
    const thirdRectangle = document.getElementById('thirdRectangle');
    const inner6Rectangle = document.getElementById('inner6-rectangle');
    const box_text1 = document.getElementById('box_text1');
    const box_text2 = document.getElementById('box_text2');
    const box_text3 = document.getElementById('box_text3');
    const box_text4 = document.getElementById('box_text4');
    const Button_Politics = document.getElementById('Button_Politics');      
    const box_text_Politics = document.getElementById('box_text_Politics');
    const toggleSwitch = document.querySelector('.toggle-switch');
    const box_text_Confirmation = document.getElementById('box_text_Confirmation');
    const Button_Politics1_Back = document.getElementById('Button_Politics1_Back');
    const box_text5 = document.getElementById('box_text5');

    // Скрываем кнопки и блоки при загрузке страницы
    nextButton.style.display = 'none';
    secondRectangle.style.display = 'none';
    thirdRectangle.style.display = 'none';
    inner6Rectangle.style.display = 'none';
    nameInput.style.display = 'none'; 
    Button_Politics.style.display = 'none';
    box_text_Politics.style.display = 'none';
    toggleSwitch.style.display = 'none';
    box_text_Confirmation.style.display = 'none';
    Button_Politics1_Back.style.display = 'none';
    


    window.onload = function() {
        const centerWindow = () => {
            // Получаем размеры экрана
            const screenWidth = window.screen.width;
            const screenHeight = window.screen.height;
            // Устанавливаем размеры окна
            const width = 400;
            const height = 450;
            // Вычисляем позицию окна
            const left = (screenWidth - width) / 2;
            const top = (screenHeight - height) / 2;
            // Устанавливаем размеры и позицию окна
            window.resizeTo(width, height);
            window.moveTo(left, top);
        };
        // Устанавливаем окно по центру при загрузке и при изменении размеров
        centerWindow();
        window.onresize = centerWindow;
    };
    
    // Функция для показа блоков поочередно
    function showBoxesSequentially() {
        // Показываем первый блок
        box_text1.style.display = 'block';
        box_text2.style.display = 'none';
        box_text3.style.display = 'none';
        box_text4.style.display = 'none';
        box_text5.style.display = 'none'; // Изначально скрытый пятый блок
    
        // Задержка перед показом второго блока
        setTimeout(() => {
            box_text1.style.display = 'none';
            box_text2.style.display = 'block';
            box_text3.style.display = 'none';
            box_text4.style.display = 'none';
            box_text5.style.display = 'none';
            setTimeout(() => {
                box_text2.style.display = 'none';
                box_text3.style.display = 'block';
                box_text4.style.display = 'none';
                box_text5.style.display = 'none';
                setTimeout(() => {
                    box_text3.style.display = 'none';
                    box_text4.style.display = 'block';
                    box_text5.style.display = 'none';
                    Button_Politics.style.display = 'none';
                    setTimeout(() => {
                        box_text4.style.display = 'none';
                        Button_Politics.style.display = 'block'; 
                    }, 1000); // Задержка перед показом пятого блока
                }, 1000); // Задержка перед показом четвёртого блока
            }, 1000); // Задержка перед показом третьего блока
        }, 1000); // Задержка перед показом второго блока
    }
    showBoxesSequentially();

    // Кнопка перенос на политику к.
    document.getElementById('Button_Politics').addEventListener('click', function() {
        box_text1.style.display = 'none';
        box_text2.style.display = 'none';
        box_text3.style.display = 'none';
        box_text4.style.display = 'none';
        Button_Politics.style.display = 'none'; 
        box_text_Politics.style.display = 'block';    
        toggleSwitch.style.display = 'block';      
        box_text_Confirmation.style.display = 'block';


    });

// Переключатель, согласие на обработку п.д.
let isHidden = false; // Переменная для отслеживания состояния видимости
toggleSwitch.addEventListener('click', () => {
    if (isHidden) {
        box_text_Confirmation.style.display = 'block'; // Показываем элемент
        Button_Politics1_Back.style.display = 'none';
        
    } else {
        box_text_Confirmation.style.display = 'none'; // Скрываем элемент
        Button_Politics1_Back.style.display = 'block';
        eel.toggleSwitch(isHidden)
    }
    isHidden = !isHidden;// Переключаем состояние видимости
    toggleSwitch.classList.toggle('active');// Переключаем класс 'active'
});

// Кнопка назад
document.getElementById('Button_Politics1_Back').addEventListener('click', function() {
    box_text_Politics.style.display = 'none';    
    toggleSwitch.style.display = 'none';      
    box_text_Confirmation.style.display = 'none';
    Button_Politics1_Back.style.display = 'none';
    nameInput.style.display = 'block';
});


nameInput.addEventListener('input', function() {// Ввод имени
    if (nameInput.value.trim()) {
        nextButton.style.display = 'block';
    } else {
        nextButton.style.display = 'none';
    }
});
nextButton.addEventListener('click', handleNextButton);// Назначение обработчика на кнопку "Дальше"

function handleNextButton() {// Функция для кнопки "Дальше", имя
    const name = nameInput.value.trim();// Получаем значение имени из input
    if (name) {// Проверяем, чтобы имя не было пустым
        // Вызываем функцию Python через Eel
        eel.process_name(name)();

        nameInput.style.display = 'none'; // Скрываем input и кнопку после отправки
        nameInput.disabled = false;
        nameInput.value = '';
        nextButton.style.display = 'none';

        window.location.replace('../index.html');//открываем index.html
    }
}
});
