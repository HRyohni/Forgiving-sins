
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