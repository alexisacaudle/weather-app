// static/js/weather.js

document.addEventListener("DOMContentLoaded", function () {
    const weatherCondition = document.body.className;
    const animationContainer = document.querySelector(".weather-animation");

    if (weatherCondition === "rainy") {
        createRainEffect();
    } else if (weatherCondition === "snowy") {
        createSnowEffect();
    }
});

// Function to create falling raindrops
function createRainEffect() {
    for (let i = 0; i < 50; i++) {
        let drop = document.createElement("div");
        drop.classList.add("raindrop");
        drop.style.left = Math.random() * 100 + "vw";
        drop.style.animationDuration = Math.random() * 2 + 1 + "s";
        document.body.appendChild(drop);
    }
}

// Function to create falling snowflakes
function createSnowEffect() {
    for (let i = 0; i < 50; i++) {
        let snowflake = document.createElement("div");
        snowflake.classList.add("snowflake");
        snowflake.style.left = Math.random() * 100 + "vw";
        snowflake.style.animationDuration = Math.random() * 5 + 2 + "s";
        document.body.appendChild(snowflake);
    }
}

// Add CSS for rain and snow
const style = document.createElement("style");
style.innerHTML = `
  .raindrop {
    position: fixed;
    top: -10px;
    width: 2px;
    height: 10px;
    background: rgba(255, 255, 255, 0.7);
    animation: fall linear infinite;
  }

  .snowflake {
    position: fixed;
    top: -10px;
    width: 5px;
    height: 5px;
    background: white;
    border-radius: 50%;
    opacity: 0.8;
    animation: fall linear infinite;
  }

  @keyframes fall {
    to {
      transform: translateY(100vh);
    }
  }
`;
document.head.appendChild(style);
