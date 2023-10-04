/* makes an AJAX GET request to the Star Wars API, retrieves a list of films,
 * and dynamically adds each film's title as a list item to the HTML */

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movie of data.results) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
