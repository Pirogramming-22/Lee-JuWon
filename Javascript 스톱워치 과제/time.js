let timer = null;
let milliseconds = 0;

function updateStopwatch() {
  milliseconds += 10; // 10ms 단위로 증가

  const totalSeconds = Math.floor(milliseconds / 1000);
  const displaySeconds = String(totalSeconds % 60).padStart(2, "0");
  const displayMilliseconds = String(Math.floor((milliseconds % 1000) / 10)).padStart(2, "0");

  const stopwatchDisplay = document.querySelector(".stopwatch_number");
  stopwatchDisplay.textContent = `${displaySeconds}:${displayMilliseconds}`;
}

// Start 버튼
document.querySelector(".start").addEventListener("click", () => {
  if (!timer) {
    timer = setInterval(updateStopwatch, 10);
  }
});

// Stop 버튼
document.querySelector(".stop").addEventListener("click", () => {
  if (timer) {
    clearInterval(timer);
    timer = null;
    addRecord();
  }
});

// Reset 버튼
document.querySelector(".reset").addEventListener("click", () => {
  clearInterval(timer);
  timer = null;
  milliseconds = 0;

  const stopwatchDisplay = document.querySelector(".stopwatch_number");
  stopwatchDisplay.textContent = "00:00";

  clearRecords();
});

// 기록 추가
function addRecord() {
  const stopwatchDisplay = document.querySelector(".stopwatch_number").textContent;

  const recordBoxMiddle = document.querySelector(".recordbox_middle");

  const recordBox = document.createElement("div");
  recordBox.classList.add("recordbox_middle_box");

  const circleButton = document.createElement("button");
  circleButton.classList.add("recordbox_middle_circle");

  const recordTime = document.createElement("div");
  recordTime.classList.add("recordbox_middle_time");
  recordTime.textContent = stopwatchDisplay;

  // recordbox_middle_box에 추가
  recordBox.appendChild(circleButton);
  recordBox.appendChild(recordTime);

  // recordbox_middle에 추가
  recordBoxMiddle.appendChild(recordBox);
}

// 기록 초기화
function clearRecords() {
  const recordBoxMiddle = document.querySelector(".recordbox_middle");
}
