function searchWithinDomain() {
  // Получаем значение из текстового поля
  var searchQuery = document.getElementById('searchInput').value;

  // Выполняем поиск внутри домена 127.0.0.1:8232
  var searchUrl = 'http://127.0.0.1:8232/search?q=' + encodeURIComponent(searchQuery);

  // Создаем AJAX-запрос для получения результатов поиска
  var xhr = new XMLHttpRequest();
  xhr.open('GET', searchUrl, true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      // Обработка успешного ответа
      var searchResults = JSON.parse(xhr.responseText);
      displaySearchResults(searchResults);
    } else {
      // Обработка ошибки
      console.error('Ошибка при выполнении запроса:', xhr.status);
    }
  };
  xhr.send();
}

function displaySearchResults(results) {
  var searchResultsDiv = document.getElementById('searchResults');
  searchResultsDiv.innerHTML = ''; // Очищаем предыдущие результаты поиска

  if (results.length === 0) {
    searchResultsDiv.textContent = 'Ничего не найдено.';
    return;
  }

  var ul = document.createElement('ul');
  results.forEach(function(result) {
    var li = document.createElement('li');
    li.textContent = result.title;
    ul.appendChild(li);
  });

  searchResultsDiv.appendChild(ul);
}