//loop through all of the spans and add in the class old after they are done falling
$(document).ready(function(){
    var count = 0;

    const interval = setInterval(function() {
        for(var i = 0; i <= count; i++){
           $("."+i+"").addClass("old");
        }
      }, 5000);

    $("#thoughts").keyup(function(e){

      if(e.keyCode == 32){
        count++;
        var drop = findNextWord($("#thoughts").val());
        $(".fallarea").append("<span class = \"fall "+ count +"\">"+drop+"</span>");
      }


      if((e.keyCode == 8 && $("#thoughts").val() == "") || e.keyCode == 13){
        console.log("cleared");
        $("#thoughts").val("");
        $(".fallarea").text("");
      }


    })




  });

function findNextWord(s){
  let space = 0;
  let word = "";
  for (var i = s.length-2; i >= 0; i--){
    if(s[i] == " " ){
      space = i;
      word = s.substring(space + 1, s.length-1);
      return word;
    }
  }
  if(space == 0){
      word = s.substring(0, s.length-1);
      return word;
  }

}
