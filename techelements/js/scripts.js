const divider = document.getElementById('divider');
const left = document.getElementById('left');
const right = document.getElementById('right');
const container = document.getElementById('container');

divider.addEventListener('mousedown', () => {
    document.addEventListener('mousemove', resize);
    document.addEventListener('mouseup', () => {
        document.removeEventListener('mousemove', resize);
        });
    });

function resize(e) {
    const containerWidth = container.offsetWidth;
    const leftWidth = e.clientX / containerWidth * 100;
    left.style.flex = leftWidth;
    right.style.flex = 100 - leftWidth;
}
