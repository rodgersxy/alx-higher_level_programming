/* the CSS class of the <header> elements will toggle between 'red' and 'green' */
$(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
