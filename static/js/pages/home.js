// ? IMPORTING FUNCTIONS FROM BASE JS
import { createIntersectionObserver, addContextMenuListener } from '../base/base.js';

// | INITIALIZING INTERSECTION OBSERVER FOR HOME PAGE SECTIONS
const observer = createIntersectionObserver(
    { threshold: 0.2 },
    {
        onEnter: (el) => {
            el.classList.add('in-view');
        },
        onLeave: (el) => {
            el.classList.remove('in-view');
        }
    }
);

// & OBSERVING SECTIONS
const sections = document.querySelectorAll('.section');
sections.forEach((section) => {observer.observe(section);});

// | ADDING CUSTOM CONTEXT MENU LISTENER
addContextMenuListener(
    document.body,
    (e) => { 
        e.preventDefault();
        e.stopPropagation();
        alert('Right click is disabled on this website.');
    }
)