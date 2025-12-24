// * CREATING INTERSECTION OBSERVER INSTANCE

/**
 * Creates and returns a shared IntersectionObserver instance
 * @param {Object} options IntersectionObserver options
 * @param {Function} onEnter callback when element becomes visible
 * @param {Function} onLeave callback when element leaves viewport
*/
export function createIntersectionObserver(
    {
        root = null,
        rootMargin = "0px",
        threshold = 0.1
    } = {},
    {
        onEnter = () => { },
        onLeave = () => { }
    } = {}
) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                onEnter(entry.target, entry);
            } else {
                onLeave(entry.target, entry);
            }
        });
    }, { root, rootMargin, threshold });

    return {
        observer,

        observe(el) {
            if (el) observer.observe(el);
        },

        unobserve(el) {
            if (el) observer.unobserve(el);
        },

        disconnect() {
            observer.disconnect();
        }
    };
}

// & EVENT LISTENER FOR CONTEXT MENU
/**
 * Adds context menu event listener to an element
 * @param {Element} element 
 * @param {Function} callback 
 * @returns 
 */
export function addContextMenuListener(element, callback) {
    if (!element) {return};
    element.addEventListener("contextmenu", callback);
}