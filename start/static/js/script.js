$('.checkbox_example input:checkbox').click(function(){
    if ($(this).is(':checked')) {
         $('.checkbox_example input:checkbox').not(this).prop('checked', false);
    }
});


var names = ["#checkbox1", "#checkbox2", "#checkbox3"];

function checkbox_on(x){
  $(x).prop('checked', true);
}


function checkbox_off(x){
  $(x).prop('checked', false);
}


function infinite(){
  while (true) {
    for (var i = 0; i < names.length; i++) {
          checkbox_on(names[i]);
          checkbox_off(names[i]);
        }
  }
}




// $(document).ready(function() {
//   while (true) {
//     for (var i = 0; i < names.length; i++) {
//       checkbox_on(names[i]);
//       checkbox_off(names[i]);
//     }
//   }

});
