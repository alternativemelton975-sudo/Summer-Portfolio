const phrase = "Our World Is Looping";

function runCycle() {
  const startTime = Date.now();
  const duration = 30000; // 30 seconds in milliseconds
  const demoElement = document.getElementById("demo");
  let output = "";

  const interval = setInterval(() => {
    output += phrase + "<br>";
    demoElement.innerHTML = output;

    // Check if 30 seconds have elapsed
    if (Date.now() - startTime >= duration) {
      clearInterval(interval);
      output += "<strong>Resetting...</strong><br>";
      demoElement.innerHTML = output;
      setTimeout(() => {
        demoElement.innerHTML = "";
        runCycle(); // Reset and run again
      }, 1000);
    }
  }, 100); // Log approximately every 100ms
}

document.addEventListener("DOMContentLoaded", runCycle);
