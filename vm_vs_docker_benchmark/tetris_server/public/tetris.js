const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');
context.scale(20, 20);

function draw() {
  context.fillStyle = '#000';
  context.fillRect(0, 0, canvas.width, canvas.height);

  context.fillStyle = '#f00';
  context.fillRect(1, 1, 1, 1);
}

function update() {
  draw();
  requestAnimationFrame(update);
}

update();
