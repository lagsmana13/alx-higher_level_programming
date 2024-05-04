$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  success: function(data) {
    $('#hello').text(data.hello);
  },
  error: function(xhr, status, error) {
    console.error('Error:', error);
  }
});
