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

        // Задержка перед показом второго блока
        setTimeout(() => {
            box_text1.style.display = 'none';
            box_text2.style.display = 'block';
            box_text3.style.display = 'none';

            setTimeout(() => {
                box_text2.style.display = 'none';
                box_text3.style.display = 'block';

                setTimeout(() => {
                    box_text3.style.display = 'none';
                    box_text4.style.display = 'block';
                    Button_Politics.style.display = 'block';
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


// Функция для изменения размера окна
function resize_window(width, height) {
    window.resizeTo(width, height);
}

// Экспонируем функцию для вызова из Python
eel.expose(resize_window);


    // Проверка при вводе имени
    nameInput.addEventListener('input', function() {
        if (nameInput.value.trim()) {
            nextButton.style.display = 'block';
        } else {
            nextButton.style.display = 'none';
        }
    });





    // Функция для показа прямоугольников
    async function showRectangles() {
        var name = nameInput.value;
        if (name.trim()) {
            await eel.process_name(name); // Предполагаем, что функция process_name определена в Python
            secondRectangle.textContent = 'Добавьте свои приложения!';
            thirdRectangle.textContent = '';

            secondRectangle.style.display = 'block';
            thirdRectangle.style.display = 'block';
            inner6Rectangle.style.display = 'block';
            nameInput.disabled = true;
            nextButton.style.display = 'none';

            // Анимация для появления второго и третьего прямоугольников
        
        }
    }

    // Назначение обработчика на кнопку "Дальше"
    nextButton.addEventListener('click', showRectangles);

    // Функция для кнопки "Назад"
    function handleBackButton() {
        inner6Rectangle.style.display = 'none';
        secondRectangle.style.display = 'none';
        thirdRectangle.style.display = 'none';
        nameInput.disabled = false;
        nameInput.value = '';
        nextButton.style.display = 'none';
    }
});
