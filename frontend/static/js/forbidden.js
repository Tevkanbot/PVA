
// Блокировка открытия инструментов разработчика через Ctrl+Shift+I
document.addEventListener('keydown', function(event) {
  if (event.ctrlKey && event.shiftKey && event.code === 'KeyI') {
      event.preventDefault();
      return false;
  }
});

// Блокировка правой кнопки мыши
document.addEventListener('contextmenu', function(event) {
  event.preventDefault();
  return false;
});

// Блокировка F12
document.addEventListener('keydown', function(event) {
 if (event.key === 'F12') {
     event.preventDefault();
     return false;
 }
});


function disableImageDragging() {
  // Получаем все изображения на странице
  const images = document.querySelectorAll('img');
  
  // Добавляем обработчик события для каждого изображения
  images.forEach(img => {
      img.addEventListener('dragstart', (event) => {
          event.preventDefault(); // Отключает перетаскивание
      });
  });
}

document.addEventListener('keydown', function(event) {
  // Разрешаем Ctrl+C, Ctrl+V
  if ((event.ctrlKey || event.metaKey) && (event.key === 'c' || event.key === 'v' )) {
      return; // Разрешаем Ctrl+C, Ctrl+V
  }

  // Блокируем все остальные комбинации с Ctrl, Meta (Cmd), Alt
  if (event.ctrlKey || event.metaKey || event.altKey) {
      event.preventDefault();
      return;
  }

  // Блокировка функциональных клавиш F1-F12
  if (event.key.startsWith('F') && !isNaN(event.key.slice(1))) {
      event.preventDefault();
      return;
  }

  // Блокировка отдельных клавиш, таких как Tab, Esc, и т.д.
  const blockedKeys = ['Tab', 'Escape', 'F5'];
  if (blockedKeys.includes(event.key)) {
      event.preventDefault();
      return;
  }
});

document.addEventListener('DOMContentLoaded', function() {
  // Отключаем автоматический перевод для всей страницы
  document.querySelector('html').setAttribute('translate', 'no');

  // Отключаем перевод для определённых элементов с классом 'no-translate'
  const elements = document.querySelectorAll('.no-translate');
  elements.forEach(function(element) {
      element.setAttribute('translate', 'no');
  });
});
