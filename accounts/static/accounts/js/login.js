const username = document.getElementById('id_username');
const password = document.getElementById('id_password');
const show_password_btn = document.getElementById('show-password');
const show_password_btn_icon = document.querySelector('#show-password i');

const username_icon = document.querySelector('.username-icon');
const password_icon = document.querySelector('.password-icon');

username.setAttribute('placeHolder', 'Email address')
username.setAttribute('title', 'Email address')
password.setAttribute('placeHolder', 'Password')
password.setAttribute('title', 'Password')
show_password_btn.setAttribute('title', 'Show Password')

focus_input_field(password_icon, password)
focus_input_field(username_icon, username)

password.addEventListener('focusout', e=>{
    password.type = 'password';
    show_password_btn_icon.setAttribute('class', 'fas fa-eye');
    show_password_btn.setAttribute('title', 'Show Password');
})


function focus_input_field(element, input_field) {
    element.addEventListener('click', e=>{
        input_field.focus();
    })
}

show_password_btn.addEventListener('click', e=>{
    switch (password.type) {
        case 'text':
            password.type = 'password';
            password.focus();
            show_password_btn_icon.setAttribute('class', 'fas fa-eye');
            show_password_btn.setAttribute('title', 'Show Password');
            break;
        default:
            password.type = 'text';
            password.focus();
            show_password_btn_icon.setAttribute('class', 'fas fa-eye-slash');
            show_password_btn.setAttribute('title', 'Hide Password');
            break;
    }
})