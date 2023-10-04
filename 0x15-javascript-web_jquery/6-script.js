/* script that updates the text of the <header> element to New Header!!! */

$(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
