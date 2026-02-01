const open_search_div_btn = document.getElementById('open-search-div-btn');
const close_search_div_btn = document.getElementById('close-search-div-btn');
const search_div = document.getElementById('search-div');
const logout_toggler = document.getElementById('logout-toggler');
const logout_form = document.getElementById('logout-form');
const cancel_logout_btn = document.querySelector('.cancle-logout-btn');
const logout_btn = document.getElementById('logout-btn');


// logout_toggler.addEventListener('click', e=>{

// })


$('#logout-toggler').click(e=>{
    $('#logout-form').fadeIn(500)
})

$('#logout-btn').click(e=>{
    setTimeout(() => {
        $('#logout-form-div').fadeOut(500);
    }, 500);
})

$('.cancle-logout-btn').click(e=>{
    e.preventDefault();
    $('#logout-form-div').fadeOut(500);
})
// search_div.style.display = 'none';

$('#open-search-div-btn').click(e=>{
    $('#search-div').fadeIn(500);
})

$('#close-search-div-btn').click(e=>{
    $('#search-div').fadeOut(500);
})