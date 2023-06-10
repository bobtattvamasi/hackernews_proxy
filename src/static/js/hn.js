// hn.js

//// Function to perform a search on Hacker News
//function searchHackerNews() {
//  // Get the search query from the input field
//  var query = document.getElementById('searchInput').value;
//
//  // Construct the search URL
//  var searchUrl = 'http://127.0.0.1:8232/search?q=' + encodeURIComponent(query);
//
//  // Redirect the user to the search URL
//  window.location.href = searchUrl;
//}
//
//// Usage example:
//// Attach an event listener to the search button or form submit event
//document.getElementById('searchForm').addEventListener('submit', function(event) {
//  event.preventDefault();
//  searchHackerNews();
//});

// Function to perform a search on Hacker News
function searchHackerNews() {
  // Get the search query from the input field
  var query = document.getElementById('searchInput').value;

  // Construct the search URL
  var searchUrl = 'http://127.0.0.1:8232/search?q=' + encodeURIComponent(query);

  // Redirect the user to the search URL
  window.location.href = searchUrl;
}

// Usage example:
// Attach an event listener to the form submit event
//document.getElementById('searchForm').addEventListener('submit', function(event) {
//  event.preventDefault();
//  searchHackerNews();
});