function bjfunc()
{
  document.getElementById("myDiv").style.backgroundImage = "url('1.jpg')";
  document.getElementById("myDiv").style.backgroundSize = "cover";
  setTimeout(bj2,2000)
}

function bj2()
{
document.getElementById("myDiv").style.backgroundImage = "url('2.jpg')";
document.getElementById("myDiv").style.backgroundSize = "cover";
setTimeout(bj3,2000)
}

function bj3()
{
document.getElementById("myDiv").style.backgroundImage = "url('3.jpg')";
document.getElementById("myDiv").style.backgroundSize = "cover";
setTimeout(bj4,2000)
}

function bj4()
{
document.getElementById("myDiv").style.backgroundImage = "url('4.jpg')";
document.getElementById("myDiv").style.backgroundSize = "cover";
setTimeout(bj5,2000)
}

function bj5()
{
document.getElementById("myDiv").style.backgroundImage = "url('5.jpg')";
document.getElementById("myDiv").style.backgroundSize = "cover";
setTimeout(bjfunc,2000)
}
