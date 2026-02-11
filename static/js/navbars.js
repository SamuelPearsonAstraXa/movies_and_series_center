const open_search_div_btn = document.getElementById('open-search-div-btn');
const close_search_div_btn = document.getElementById('close-search-div-btn');
const search_div = document.getElementById('search-div');
const dark_theme_toggler = document.getElementById('dark-theme-toggler');
const aside_navbar_toggler = document.getElementById('aside-navbar-toggler');
const main_navbar = document.getElementById('main-navbar');
const logo = document.getElementById('logo');

try {
    const login_link = document.querySelector('.login-link');

    login_link.addEventListener('click', e=>{
        e.preventDefault();
        window.location = `/accounts/user-login/?next=${window.location}`
    })
} catch (error) {
    console.log('No login link')
}

// dark_theme_toggler.addEventListener('click', e=>{
//     main_navbar.setAttribute('class', 'dark-mode block-element');
//     search_div.setAttribute('class', 'dark-mode block-element');
//     open_search_div_btn.setAttribute('class', 'mini-btns  dark-mode inline-element');
//     dark_theme_toggler.setAttribute('class', 'mini-btns  dark-mode inline-element');
//     aside_navbar_toggler.setAttribute('class', 'aside-navbar-toggler  dark-mode inline-element mini-btns');
//     logo.setAttribute('class', 'logo dark-mode inline-element');
// })

$('#logout-btn').click(e=>{
    setTimeout(() => {
        $('.logout-confirm').fadeIn(500);
    }, 500);
})

$('#cancel-logout-btn').click(e=>{
    $('.logout-confirm').fadeOut(500);
})
// search_div.style.display = 'none';

$('#open-search-div-btn').click(e=>{
    $('#search-div').fadeIn(500);
})

$('#close-search-div-btn').click(e=>{
    $('#search-div').fadeOut(500);
})