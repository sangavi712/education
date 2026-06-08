// app/static/js/theme.js

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Check localStorage for theme preference
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply initial theme
    if (currentTheme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
        if (themeToggleBtn) {
            themeToggleBtn.checked = true;
        }
    } else {
        htmlElement.setAttribute('data-theme', 'light');
        if (themeToggleBtn) {
            themeToggleBtn.checked = false;
        }
    }

    // Toggle event listener
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('change', function() {
            if (this.checked) {
                htmlElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
            } else {
                htmlElement.setAttribute('data-theme', 'light');
                localStorage.setItem('theme', 'light');
            }
        });
    }
});
