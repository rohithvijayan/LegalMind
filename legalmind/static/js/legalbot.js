// Function to toggle between light and dark mode
function toggleTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');

    // Toggle dark mode class on the body
    body.classList.toggle('dark-mode');

    // Save the user's preference in localStorage
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('theme', 'dark');
        themeToggle.checked = true; // Update the toggle switch state
    } else {
        localStorage.setItem('theme', 'light');
        themeToggle.checked = false; // Update the toggle switch state
    }
}

// Function to load the user's theme preference on page load
function loadTheme() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');

    // Get the saved theme from localStorage
    const savedTheme = localStorage.getItem('theme');

    // Apply the saved theme
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        themeToggle.checked = true;
    } else {
        body.classList.remove('dark-mode');
        themeToggle.checked = false;
    }
}

// Load the theme when the page loads
document.addEventListener('DOMContentLoaded', loadTheme);