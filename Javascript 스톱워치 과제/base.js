/* 버튼에 check 이미지 표시 관련 js */
document.addEventListener("DOMContentLoaded", () => {
  const circles = document.querySelectorAll(".recordbox_top_circle, .recordbox_middle_circle");

  circles.forEach((circle) => {
    circle.addEventListener("click", () => {
      const checkImage = circle.querySelector("img");

      if (checkImage) {
        checkImage.remove();
      } else {
        const img = document.createElement("img");
        img.src = "./check.svg";
        img.width = 25;
        img.height = 25;
        img.style.margin = "auto";
        circle.appendChild(img);
      }
    });
  });
});
