/* adds the class red to the <header> element onclick */
$(() => {
  $('DIV#red_header').click(() => {
    $('header').addClass('red');
  });
});
