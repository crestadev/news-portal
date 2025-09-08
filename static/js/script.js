/**
 * Dark Mode Toggle Functionality
 */
const darkModeSwitch = document.getElementById('darkModeSwitch');
const htmlElement = document.documentElement; // Target the <html> element
const currentTheme = localStorage.getItem('theme');

// Function to set the theme
const setTheme = (theme) => {
  htmlElement.setAttribute('data-bs-theme', theme);
  localStorage.setItem('theme', theme);
  // Update switch state (optional, if you want the switch to reflect the loaded theme)
  if (darkModeSwitch) {
    darkModeSwitch.checked = theme === 'dark';
  }
};

// Apply the saved theme on initial load
if (currentTheme) {
  setTheme(currentTheme);
} else {
  // Default to light theme if no preference is saved
  setTheme('light');
}

// Add event listener to the switch
if (darkModeSwitch) {
  darkModeSwitch.addEventListener('change', () => {
    if (darkModeSwitch.checked) {
      setTheme('dark');
    } else {
      setTheme('light');
    }
  });
}

/**
 * Optional: Add active class to current nav link based on URL
 * This is a simple example; more robust routing might be needed for complex apps.
 */
document.addEventListener('DOMContentLoaded', () => {
  const currentPath = window.location.pathname.split('/').pop(); // Get the current file name
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href').split('/').pop();
    // Remove existing active class from all links first
    link.classList.remove('active');
    link.removeAttribute('aria-current'); // Remove aria-current as well

    // Add active class if the link's href matches the current path
    if (linkPath === currentPath || (currentPath === '' && linkPath === 'index.html')) { // Handle root path case
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
});