document.addEventListener("DOMContentLoaded", () => {
  const recordBoxMiddle = document.querySelector(".recordbox_middle");
  const trashcanIcon = document.querySelector("#trashcan-icon");
  const recordBoxTopCircle = document.querySelector(".recordbox_top_circle");

  recordBoxMiddle.addEventListener("click", (event) => {
    const circle = event.target.closest(".recordbox_middle_circle");

    if (circle) {
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
    }

    const circles = document.querySelectorAll(".recordbox_middle_circle");
    const allChecked = Array.from(circles).every((circle) => circle.querySelector("img"));
    const topCheckImage = recordBoxTopCircle.querySelector("img");

    if (allChecked && !topCheckImage) {
      const img = document.createElement("img");
      img.src = "./check.svg";
      img.width = 25;
      img.height = 25;
      img.style.margin = "auto";
      recordBoxTopCircle.appendChild(img);
    } else if (!allChecked && topCheckImage) {
      topCheckImage.remove();
    }
  });

  if (recordBoxTopCircle) {
    recordBoxTopCircle.addEventListener("click", () => {
      const checkImage = recordBoxTopCircle.querySelector("img");
      const circles = document.querySelectorAll(".recordbox_middle_circle");

      if (checkImage) {
        checkImage.remove();
        circles.forEach((circle) => {
          const circleCheckImage = circle.querySelector("img");
          if (circleCheckImage) circleCheckImage.remove();
        });
      } else {
        const img = document.createElement("img");
        img.src = "./check.svg";
        img.width = 25;
        img.height = 25;
        img.style.margin = "auto";
        recordBoxTopCircle.appendChild(img);

        circles.forEach((circle) => {
          if (!circle.querySelector("img")) {
            const newImg = document.createElement("img");
            newImg.src = "./check.svg";
            newImg.width = 25;
            newImg.height = 25;
            newImg.style.margin = "auto";
            circle.appendChild(newImg);
          }
        });
      }
    });
  }

  /* 쓰레기통 관련 js */
  if (trashcanIcon) {
    trashcanIcon.addEventListener("click", () => {
      const records = document.querySelectorAll(".recordbox_middle_box");

      records.forEach((record) => {
        const circle = record.querySelector(".recordbox_middle_circle");
        const checkImage = circle.querySelector("img");

        if (checkImage) {
          record.remove();
        }
      });
    });
  }
});
