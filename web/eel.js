document.getElementById('nameInput').addEventListener('input', function() {
    var name = this.value;
    if(name.trim()) {  // Если что-то введено и это не пробелы, показываем кнопку
        document.getElementById('nextButton').style.display = 'block';
    } else {  // Если поле пустое или содержит только пробелы, скрываем кнопку
        document.getElementById('nextButton').style.display = 'none';
    }
});

async function showRectangle() {
    var name = document.getElementById('nameInput').value;
    if(name.trim()) {
        await eel.process_name(name); // Предполагаем, что функция process_name определена в Python
        document.getElementById('innerRectangle').style.display = 'block';
        document.getElementById('secondRectangle').style.display = 'block';
        document.getElementById('nameInput').disabled = true;
        document.getElementById('nextButton').style.display = 'none';
    }
}

// Обработчики событий для перетаскивания файлов
var innerRectangle = document.getElementById('innerRectangle');
innerRectangle.addEventListener('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
    e.dataTransfer.dropEffect = 'copy';
});

innerRectangle.addEventListener('drop', function(e) {
    e.preventDefault();
    e.stopPropagation();

    var files = e.dataTransfer.files;
    for (let i = 0; i < files.length; i++) {
        (function(file) {
            var reader = new FileReader();
            reader.onload = function(event) {
                var fileURL = URL.createObjectURL(file);
                console.log(fileURL); // Выводим URL-адрес файла в консоль
                eel.process_file(file.path)(function(returned_data){
                    // Обработка возвращаемого значения
                    console.log(returned_data);
                });
            };
            reader.readAsDataURL(file); // Читаем файл как Data URL
        })(files[i]);
    }
});

// Вызов функции при загрузке страницы для первоначальной проверки
document.addEventListener('DOMContentLoaded', function() {
    var name = document.getElementById('nameInput').value;
    document.getElementById('nextButton').style.display = name.trim() ? 'block' : 'none';
});