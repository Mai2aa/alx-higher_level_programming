$(document).ready(function() {
    $.ajax({
      url: "https://swapi-api.alx-tools.com/api/films/?format=json",
      method: "GET",
      success: function(data) {
        const films = data.results;
        films.forEach(function(film) {
        $("#list_movies").append("<li>" + film.title + "</li>");
      });
      }
    });
  });
  