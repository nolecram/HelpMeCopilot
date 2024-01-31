function addrandomnumbers(min)
{
    var randnumber = Math.floor(Math.random() * ( - min + 1)) + min;
    return randnumber;
}

// Build a test for the previous function
/**
 * This function tests the addrandomnumbers function by generating a random number within a given range and checking if it falls within the range.
 * @returns {string} The result of the test, either "Test Passed" or "Test Failed".
 */
function test_addrandomnumbers()
{
  var min = 1;
  var max = 100;
  var randnumber = addrandomnumbers(min,max);
  if (randnumber >= min && randnumber <= max)
  {
    return "Test Passed";
  }
  else
  {
    return "Test Failed";
  }
}
    
