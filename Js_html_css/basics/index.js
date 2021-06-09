let btn = document.getElementById('cta-btn')
let overlay = document.getElementById('overlay')

function disableOverlay(){
    overlay.style.display = 'none'
    overlay.classList.remove('animate-overlay')
}

btn.addEventListener('click', () => {
    overlay.style.display = 'grid';
    overlay.classList.add('animate-overlay');
    setTimeout(disableOverlay, 2800)
})