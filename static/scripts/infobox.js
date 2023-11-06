const buttons = document.querySelectorAll(".info-button");
buttons.forEach(button => {
  button.addEventListener("click", function() {
    const infoBoxId = this.getAttribute("data-info-box");
    const infoBox = document.getElementById(infoBoxId);
    infoBox.style.display = infoBox.style.display === 'block' ? 'none' : 'block';
  });
});