let btn = document.getElementById('cta-btn')
let overlay = document.getElementById('overlay')

btn.addEventListener('click', () => {
    overlay.style.display = 'grid';
    overlay.classList.add('animate-overlay');
    await delay(3000);
    overlay.classList.remove('animate-overlay');
})