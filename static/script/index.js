

console.log("Fuck off")

counter=0;

function myFunction() {
    counter= counter +1;
    
    console.log(document.getElementById("provjeri").value)
   
    if (document.getElementById("provjeri").value.length <10)
     {
        document.getElementById("kurac").innerHTML = "neseri ispovjedaj se jos malo";
     }

     else if (document.getElementById("provjeri").value != ""    )
    {
        document.getElementById("kurac").innerHTML = "Grijeh ti je oprosten";
    }
    document.getElementById("counter").innerHTML = counter;
    
  }

  function broji_grijehe() {

    console.log(document.getElementById("counter").value)
  }





var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
