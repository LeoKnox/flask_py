function myFunction() {
    document.getElementById("pi").innerHTML = "three ";
    x = 5;
    y = 5;
    l = 5;
    w = 5;
    for (j = w; j < w+x+1; j++) {
        document.getElementById(j + "." + y).innerHTML = "X"
        document.getElementById(j + "." + (y+l)).innerHTML = "X"
    }
    for (i = l; i < l+y+1; i++) {
        document.getElementById(x+"."+i).textContent = "X"
        document.getElementById((x+w)+"."+i).innerHTML = "X"
    }
}
