// Quest 1
function answer1(key) {
  if (key == "yes") {
    document.getElementById("quest2").style.display = "block";
    document.getElementById("quest4").style.display = "none";
  } else {
    document.getElementById("quest4").style.display = "block";
    document.getElementById("quest2").style.display = "none";
  }
}

// Quest 2
function answer2(key) {
  if (key == "yes") {
    document.getElementById("quest5").style.display = "block";
    document.getElementById("output1").style.display = "none";
  } else {
    document.getElementById("output1").style.display = "block";
    document.getElementById("quest5").style.display = "none";
  }
}
// Quest 3
function answer3(key) {
  if (key == "yes") {
    document.getElementById("output3").style.display = "block";
    document.getElementById("output4").style.display = "block";
    document.getElementById("quest5").style.display = "block";
    document.getElementById("output2").style.display = "none";
  } else {
    document.getElementById("output2").style.display = "block";
    document.getElementById("output3").style.display = "none";
    document.getElementById("output4").style.display = "none";
    document.getElementById("quest5").style.display = "none";
  }
}
// Quest4
function answer4(key) {
  if (key == "positif") {
    document.getElementById("quest6").style.display = "block";
    document.getElementById("output5").style.display = "block";
    document.getElementById("output6").style.display = "none";
  } else {
    document.getElementById("output6").style.display = "block";
    document.getElementById("quest6").style.display = "block";
    document.getElementById("output5").style.display = "none";
  }
}
// Quest 6
function answer5(key) {
  if (key == "yes") {
    document.getElementById("quest7").style.display = "block";
    document.getElementById("output7").style.display = "none";
  } else {
    document.getElementById("output7").style.display = "block";
    document.getElementById("quest7").style.display = "none";
  }
}

function answer6(key) {
  if (key == "yes") {
    document.getElementById("output8").style.display = "block";
    document.getElementById("output7").style.display = "none";
  } else {
    document.getElementById("output7").style.display = "block";
    document.getElementById("output8").style.display = "none";
  }
}
