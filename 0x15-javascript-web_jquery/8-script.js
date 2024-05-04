$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function(data) {
    $.each(data.results, function(index, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  },
  error: function(xhr, status, error) {
    console.error('Error:', error);
  }
});
