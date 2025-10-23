// main.js

// Function to fade in an element
function fadeIn(element, duration = 400) {
    element.style.opacity = 0;
    element.style.display = 'block';

    let last = +new Date();
    const tick = function() {
        element.style.opacity = +element.style.opacity + (new Date() - last) / duration;
        last = +new Date();

        if (+element.style.opacity < 1) {
            requestAnimationFrame(tick);
        }
    };

    requestAnimationFrame(tick);
}

// Function to fade out an element
function fadeOut(element, duration = 400) {
    element.style.opacity = 1;

    let last = +new Date();
    const tick = function() {
        element.style.opacity = +element.style.opacity - (new Date() - last) / duration;
        last = +new Date();

        if (+element.style.opacity > 0) {
            requestAnimationFrame(tick);
        } else {
            element.style.display = 'none';
        }
    };

    requestAnimationFrame(tick);
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('myButton');
    const box = document.getElementById('myBox');

    button.addEventListener('click', () => {
        fadeIn(box);
    });

    box.addEventListener('click', () => {
        fadeOut(box);
    });
});
