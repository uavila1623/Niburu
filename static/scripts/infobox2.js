const infoButton = document.getElementById('bttn-info');
const infoContent = document.getElementById('info-content');

infoButton.addEventListener('click', () => {
  infoContent.style.display = infoContent.style.display === 'block' ? 'none' : 'block';
});