let btn = document.getElementById('cta-btn')
let overlay = document.getElementById('overlay')

function disableOverlay(){
    overlay.style.display = 'none'
    overlay.classList.remove('animate-overlay')
}

btn.addEventListener('click', () => {
    overlay.style.display = 'grid';
    overlay.classList.add('animate-overlay');
<<<<<<< HEAD
    await delay(3000);
    overlay.classList.remove('animate-overlay');
=======
    setTimeout(disableOverlay, 2800)
>>>>>>> 7756c6f29d1a94ae8447db28fe958580c82e62dd
})