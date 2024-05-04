$(document).ready(function() {
  $('#btn_translate').click(function() {
    fetchHello();
  });

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchHello();
    }
  });

  function fetchHello() {
    var langCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/' + langCode,
      type: 'GET',
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function(xhr, status, error) {
        console.error('Error:', error);
      }
    });
  }
});
