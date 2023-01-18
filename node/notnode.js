
        // Nacini ispisa u consoli
/*
console.warn("what the fuck is this");//yellow
console.error(5 === 5);//red
console.log("what the fuck is this");//noramal
*/



//window.open() otvori novi tab


        // nacin dohvata podataka
//document.getElementById('tekst').innerText = 'Kurac';

// let za imenovanje varijabli
let rijec = "kurac";
document.getElementById("tekst").innerText = rijec;


// $ znak mozemo koristiti u stringu  ali miramo koristiti ove navodnike -> ``

recenica = `Imam masivan ${rijec} `;
console.log(recenica);


        // mogu se koristiti == i ===
if ("kurac" === "kurac")
{
    console.log("hmm...");
}


//OKE OVO JE VIRUS

    /*
    for (let x =0;x<1000;x++)
{
    window.open("opis");
}

    */


// objekti

let automobil =
{
    audi :  ['1000' ,'1000','Q7'],
    audi2 :  ['2000' ,'500','Q6'],
    audi3 :  ['3000' ,'250','Q5'],
    audi4 :  ['4000' ,'150','Q4']

}

for (auto in automobil)
{
    console.log(auto)
    console.warn(automobil[auto])
}

    console.error(automobil.audi4)



function fuck (brPuta)
{
    console.log(`i want to fuck you ${brPuta} times!`)
}

fuck(69)


// uzimanje elementa preko tag name
polje = document.getElementsByTagName('div')
    console.log(polje[0]);
    console.log(polje[1].innerText);



polje = document.getElementsByClassName('div')
    console.log(polje[0]);
    console.log(polje[1].innerText);



function fuckOff()
{

}

function leftFuck()
{
    
}