document.addEventListener("DOMContentLoaded", (event) => {
    const barsButton = document.querySelector('.navbar-bars-button')
    const navbarContent = document.querySelector('.navbar-content')
    const navbarFooter = document.querySelector('.navbar-footer')

    barsButton.addEventListener('click', () => {
        if (navbarContent.classList.contains('hidden')){
            navbarContent.classList.remove('hidden')
            navbarFooter.classList.remove('hidden')
        } else {
            navbarContent.classList.add('hidden')
            navbarFooter.classList.add('hidden')
        }
    })
});