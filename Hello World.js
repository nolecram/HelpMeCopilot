document.write("Hello, world!");

function addrandomnumber(min,max){
    var x = Math.floor(Math.random() * (max - min + 1)) + min;
    return x;
}
// Build a test for the previous function
function test_addrandomnumber(){
    var x = addrandomnumber(1,10);
    if (x >= 1 && x <= 10){
        return true;
    }
    else{
        return false;
    }
}