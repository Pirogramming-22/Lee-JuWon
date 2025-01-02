let attempts = 9;
let correctNumbers = [];

function initializeGame() {
  correctNumbers = [];
  while (correctNumbers.length < 3) {
    const randomNum = Math.floor(Math.random() * 10);
    if (!correctNumbers.includes(randomNum)) {
      correctNumbers.push(randomNum);
    }
  }

  attempts = 9;
  document.getElementById("attempts").textContent = attempts;

  document.getElementById("results").textContent = "";
  document.getElementById("game-result-img").src = "";

  document.getElementById("number1").value = "";
  document.getElementById("number2").value = "";
  document.getElementById("number3").value = "";

  document.querySelector(".submit-button").disabled = false;
}

function check_numbers() {
  const number1 = document.getElementById("number1").value;
  const number2 = document.getElementById("number2").value;
  const number3 = document.getElementById("number3").value;

  if (number1 === "" || number2 === "" || number3 === "") {
    alert("모든 칸에 숫자를 입력해주세요.");

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

    return;
  }

  const userNumbers = [parseInt(number1), parseInt(number2), parseInt(number3)];
  if (userNumbers.some((num) => isNaN(num) || num < 0 || num > 9)) {
    alert("0~9 사이의 숫자만 입력 가능");
    return;
  }

  attempts--;
  document.getElementById("attempts").textContent = attempts;

  let strikeCount = 0;
  let ballCount = 0;

  for (let i = 0; i < 3; i++) {
    if (userNumbers[i] === correctNumbers[i]) {
      strikeCount++;
    } else if (correctNumbers.includes(userNumbers[i])) {
      ballCount++;
    }
  }

  let resultHTML = `<div class="check-result"><div class="results" style="display: flex; flex-direction: row; justify-content: space-around;">`;

  resultHTML += `<span style="margin-right: 10px;">${number1}</span>`;
  resultHTML += `<span style="margin-right: 10px;">${number2}</span>`;
  resultHTML += `<span style="margin-right: 150px;">${number3}</span>`;

  resultHTML += `</div> : `;

  // "Out" 표시 (모든 숫자가 틀린 경우)
  if (strikeCount === 0 && ballCount === 0) {
    resultHTML += ` <span class="num-result out"><span>O</span></span></div>`;
  } else {
    if (strikeCount === 0) {
      resultHTML += `0 <span class="num-result strike"><span> S</span>&nbsp;</span>`;
    }
    if (ballCount === 0) {
      resultHTML += `0 <span class="num-result ball"><span> B</span>&nbsp;</span>`;
    }

    if (strikeCount > 0) {
      resultHTML += `${strikeCount} <span class="num-result strike"><span> S </span></span>`;
    }
    if (ballCount > 0) {
      resultHTML += `${ballCount} <span class="num-result ball"><span> B </span></span>`;
    }
    resultHTML += `</div>`;
  }

  if (attempts === 0 && strikeCount !== 3) {
    document.getElementById("game-result-img").src = "fail.png";
    document.querySelector(".submit-button").disabled = true;
  } else if (strikeCount === 3) {
    resultHTML += `<span class="circle strike"><span>3 S</span></span></div>`;
    document.getElementById("game-result-img").src = "success.png";
    document.querySelector(".submit-button").disabled = true;
  }

  document.getElementById("results").innerHTML += resultHTML;

  if (strikeCount === 3 || attempts === 0) {
    document.querySelector(".submit-button").disabled = true;
  }
}

initializeGame();
