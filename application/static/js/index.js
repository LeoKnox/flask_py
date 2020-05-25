function myFunction(x, y, l, w, doors) {
    document.getElementById("pi").innerHTML = "three ";
    wall = doors.wall;
    position = doors.position;
    for (j = w-1; j < w+x+1; j++) {
        document.getElementById(j + "." + (y-1)).innerHTML = "X" // vertical
        document.getElementById(j + "." + (y+l)).innerHTML = "X"
    }
    for (i = l-1; i < l+y+1; i++) {
        document.getElementById(x-1+"."+i).textContent = "X"
        document.getElementById((x+w)+"."+i).innerHTML = "X"
    }
    document.getElementById((x+position)+"."+(y+w)).innerHTML = "*";
    console.log(doors)
}
