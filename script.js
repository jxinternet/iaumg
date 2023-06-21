const paddle = document.getElementById('paddle');
const ball = document.getElementById('ball');
const bricks = document.getElementsByClassName('bricks');
const scoreValue = document.getElementById('score-value');
const gameOver = document.getElementById('game-over');
let score = 0;
let ballLeft = 230;
let ballBottom = 30;
let ballDirectionX = 1;
let ballDirectionY = 1;
let paddleLeft = 210;

// Move paddle left or right
document.addEventListener('keydown', event => {
	if (event.code === 'ArrowLeft' && paddleLeft > 0) {
		paddleLeft -= 20;
		paddle.style.left = paddleLeft + 'px';
	} else if (event.code === 'ArrowRight' && paddleLeft < 420) {
		paddleLeft += 20;
		paddle.style.left = paddleLeft + 'px';
	}
});

// Move ball
setInterval(() => {
	ballLeft += ballDirectionX * 5;
	ballBottom += ballDirectionY * 5;
	ball.style.left = ballLeft + 'px';
	ball.style.bottom = ballBottom + 'px';

	// Check for collision with walls
	if (ballLeft < 0 || ballLeft > 490) {
		ballDirectionX *= -1;
	}
	if (ballBottom > 390) {
		gameOver.style.display = 'block';
	} else if (