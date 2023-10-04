/* fetches and prints how to say “Hello” depending on the language */

$(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').val();
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + code;
    $.get(url, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
