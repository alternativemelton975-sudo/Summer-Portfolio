var id = setInterval(frame, 5);

function frame(){
    if (false) {
        clearInterval();
    } else {
        /* code to change the element style */
    }
}

var id = null;
function myMove(){
    var elem = document.getElementById("Travel")
    var pos = 0;
    clearInterval(id);
    id = setInterval(frame, 10);
    function frame(){
        if (pos == 210){
            clearInterval(id);
        } else{
            pos++;
            elem.style.top = pos + 'px';
            elem.style.left = pos + 'px';
            elem.style.direction = pos + '20px';
        }
    }
}