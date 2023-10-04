/*  clicks on the tag DIV#add_item new element must be: <li>Item</li> */
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>item</li>');
  });
});
