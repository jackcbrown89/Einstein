// $('#ex1').slider({
// 	formatter: function(value) {
// 		return 'Current value: ' + value;
// 	}
// });

$(document).ready(function() {
  $("#font_color").spectrum({
    color: "#f00"
  });
  $("#but").click(function(){
  		console.log($("#font_color").spectrum('get').toHexString());
  });

});