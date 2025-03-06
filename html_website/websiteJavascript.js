


colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"];

function drawStuff() {

  var obj = document.getElementById("myCanvas");
  var draw = obj.getContext("2d");
  
  // Create gradient
  var grd = draw.createLinearGradient(0, 0, 500, 500);
  grd.addColorStop(0, "red");
  grd.addColorStop(1, "white");

  // Fill with gradient
  draw.fillStyle = grd;
  draw.fillRect(0, 0, 500, 500);
}

drawStuff();

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
  }

function changeColor() {
    document.getElementById("buttonColor").style.backgroundColor = colors[getRandomInt(0, 6)]; 
         
  }

function changeSize() {

    document.getElementById("buttonSize").style.height = getRandomInt(0, 500) + "px";
    document.getElementById("buttonSize").style.width = getRandomInt(0, 500) + "px";
}

function findButtonGame() {
  let score = 0;
  let button = document.getElementById("buttonGame");

  // Randomly generate X and Y positions for the button
  let randomX = getRandomInt(0, window.innerWidth - button.offsetWidth);
  let randomY = getRandomInt(0, window.innerHeight - button.offsetHeight);

  // Set up a click event listener on the button
  button.addEventListener("click", function() {
      // Increment score when the button is clicked
      score += 1;

      // Move the button to a new random position
      button.style.transform = `translate(${randomX}px, ${randomY}px)`; 

      // Update the score display
      document.getElementById("findingGameLabel").innerHTML = "Score: " + score;

      // Optionally, generate new random coordinates for the next click
      randomX = getRandomInt(0, window.innerWidth - button.offsetWidth);
      randomY = getRandomInt(0, window.innerHeight - button.offsetHeight);
  });
}

findButtonGame();