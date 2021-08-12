

$(document).ready(function() {
    
    

});

function click123(event){ 
   var elem = document.getElementById("sett");
   var opace = window.getComputedStyle(elem).getPropertyValue("opacity");
   if (opace == 0) {
      elem.style.setProperty("opacity",1);
   } else {
      elem.style.setProperty("opacity",0);
   }   
}


