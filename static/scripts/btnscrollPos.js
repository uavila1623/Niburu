// Save the scroll position before reloading the page
window.onbeforeunload = function() {
    window.scrollTo(0, window.scrollY);
  }
  
  // Restore the scroll position after the page reloads
  window.onload = function() {
    var scrollY = localStorage.getItem("scrollY");
    if (scrollY) {
      window.scrollTo(0, scrollY);
      localStorage.removeItem("scrollY");
    }
  }
  
  // Save the scroll position and reload the page
  function reloadPage() {
    localStorage.setItem("scrollY", window.scrollY);
    window.location.reload();
  }