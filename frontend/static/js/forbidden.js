window.onload = function() {
    const resizeWindow = () => {
      window.resizeTo(700, 500);
      window.moveTo(0, 0); // Переместить окно в левый верхний угол
    };
    
    // Установить размеры при загрузке и при попытке изменения
    resizeWindow();
    window.onresize = resizeWindow;
  };

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
//document.addEventListener('keydown', function(event) {
//  if (event.key === 'F12') {
//      event.preventDefault();
//      return false;
//  }
//});

