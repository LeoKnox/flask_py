function myFunction() {
    document.getElementById("pi").innerHTML = "three ";
    x = 5;
    y = 5;
    l = 5;
    w = 5;
    wall = 1;
    position = 3;
    for (j = w-1; j < w+x+1; j++) {
        document.getElementById(j + "." + (y-1)).innerHTML = "X" // vertical
        document.getElementById(j + "." + (y+l)).innerHTML = "X"
    }
    for (i = l-1; i < l+y+1; i++) {
        document.getElementById(x-1+"."+i).textContent = "X"
        document.getElementById((x+w)+"."+i).innerHTML = "X"
    }
    document.getElementById((x+position)+"."+(y+w)).innerHTML = "*";
}
