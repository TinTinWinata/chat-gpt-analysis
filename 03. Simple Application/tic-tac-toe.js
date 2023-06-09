// Tic Tac Toe game
let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameOver = false;

// Possible winning combinations
const winCombinations = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8], // Rows
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8], // Columns
  [0, 4, 8],
  [2, 4, 6], // Diagonals
];

// Cell click event handler
function cellClicked(cell) {
  if (gameOver || cell.innerText !== "") return;
  cell.innerText = currentPlayer;
  board[cell.dataset.index] = currentPlayer;

  if (checkWin(currentPlayer)) {
    gameOver = true;
    setTimeout(() => {
      alert(`Player ${currentPlayer} wins!`);
      resetGame();
    }, 100);
    return;
  }

  if (isBoardFull()) {
    gameOver = true;
    setTimeout(() => {
      alert("It's a draw!");
      resetGame();
    }, 100);
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  if (currentPlayer === "O") {
    setTimeout(makeBotMove, 500);
  }
}

// Check if a player has won
function checkWin(player) {
  for (let combination of winCombinations) {
    if (
      board[combination[0]] === player &&
      board[combination[1]] === player &&
      board[combination[2]] === player
    ) {
      return true;
    }
  }
  return false;
}

// Check if the board is full
function isBoardFull() {
  return board.every((cell) => cell !== "");
}

// Reset the game
function resetGame() {
  board = ["", "", "", "", "", "", "", "", ""];
  currentPlayer = "X";
  gameOver = false;
  const cells = document.getElementsByClassName("cell");
  Array.from(cells).forEach((cell) => (cell.innerText = ""));
}

// Make a move for the bot
function makeBotMove() {
  const bestMove = findBestMove();
  const cell = document.querySelector(`[data-index='${bestMove}']`);
  cellClicked(cell);
}

// Find the best move for the bot using the minimax algorithm
function findBestMove() {
  let bestScore = -Infinity;
  let bestMove;

  for (let i = 0; i < 9; i++) {
    if (board[i] === "") {
      board[i] = "O";
      let score = minimax(board, 0, false);
      board[i] = "";
      if (score > bestScore) {
        bestScore = score;
        bestMove = i;
      }
    }
  }

  return bestMove;
}

// Minimax algorithm for determining the best move
function minimax(board, depth, isMaximizing) {
  if (checkWin("X")) return -1;
  if (checkWin("O")) return 1;
  if (isBoardFull()) return 0;

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < 9; i++) {
      if (board[i] === "") {
        board[i] = "O";
        let score = minimax(board, depth + 1, false);
        board[i] = "";
        bestScore = Math.max(score, bestScore);
      }
    }
    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < 9; i++) {
      if (board[i] === "") {
        board[i] = "X";
        let score = minimax(board, depth + 1, true);
        board[i] = "";
        bestScore = Math.min(score, bestScore);
      }
    }
    return bestScore;
  }
}
