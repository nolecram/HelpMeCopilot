document.write("Hello, world!");

function addrandomnumbers(min,Max){
	return Math.floor(Math.random()*(Max-min)+min);
}
// Build a unit test for the previous function
function test_addrandomnumbers(){
    var min = 1;
    var Max = 10;
    var test = addrandomnumbers(min,Max);
    if(test >= min && test <= Max){
        return true;
    }
    return false;
}