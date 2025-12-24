// ? GETTING DOC ELEMENTS
const headerMenuBtn = document.querySelector('.header .menu');
const navBtn = document.querySelector('.nav .menu');
const closeNavBtn = document.querySelector('.nav .close-nav');
const nav = document.querySelector('.nav');
const topBar = document.querySelector('.header .bar1');
const bottomBar = document.querySelector('.header .bar2');

// & EVENT LISTENER FOR MENU BTN CLICK
headerMenuBtn.addEventListener('click', () => {
    headerMenuBtn.style.gap = '0';
    topBar.style.transform = 'rotate(45deg)';
    bottomBar.style.transform = 'rotate(-45deg)';
    
    setTimeout(() => {
        nav.style.display = 'flex';
        
        setTimeout(() => {
            nav.classList.toggle('active');
        }, 100);

    }, 300);
});

// & EVENT LISTENER FOR NAV BTN CLICK
navBtn.addEventListener('click', () => {
    nav.classList.toggle('active');

    setTimeout(() => {
        nav.style.display = 'none';
        headerMenuBtn.style.gap = '10px';
        topBar.style.transform = 'rotate(0deg)';
        bottomBar.style.transform = 'rotate(0deg)';
    }, 300);
});

// & EVENT LISTENER FOR CLOSE NAV BTN CLICK
closeNavBtn.addEventListener('click', () => {
    nav.classList.toggle('active');

    setTimeout(() => {
        nav.style.display = 'none';
        headerMenuBtn.style.gap = '10px';
        topBar.style.transform = 'rotate(0deg)';
        bottomBar.style.transform = 'rotate(0deg)';
    }, 300);
});