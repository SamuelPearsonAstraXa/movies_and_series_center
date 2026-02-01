const username = document.getElementById('id_username');
const first_name = document.getElementById('id_first_name');
const last_name = document.getElementById('id_last_name');
const email = document.getElementById('id_email');
const password1 = document.getElementById('id_password1');
const password2 = document.getElementById('id_password2');
const show_password_btn_1 = document.getElementById('show-password1');
const show_password_btn_2 = document.getElementById('show-password2');
const show_password_btn_icon_1 = document.querySelector('#show-password1 i');
const show_password_btn_icon_2 = document.querySelector('#show-password2 i');

const username_icon = document.querySelector('.username-icon');
const email_icon = document.querySelector('.email-icon');
const firstname_icon = document.querySelector('.firstname-icon');
const lastname_icon = document.querySelector('.lastname-icon');
const password1_icon = document.querySelector('.password1-icon');
const password2_icon = document.querySelector('.password2-icon');

email.setAttribute('placeHolder', 'Email address')
email.setAttribute('title', 'Email address')
username.setAttribute('placeHolder', 'Username')
username.setAttribute('title', 'Username')
first_name.setAttribute('placeHolder', 'First name')
first_name.setAttribute('title', 'First name')
last_name.setAttribute('placeHolder', 'Last name')
last_name.setAttribute('title', 'Last name')
password1.setAttribute('placeHolder', 'Password')
password2.setAttribute('placeHolder', 'Confirm Password')
password1.setAttribute('title', 'Password')
password2.setAttribute('title', 'Confirm Password')

show_hide_password(show_password_btn_1, password1, show_password_btn_icon_1)
show_hide_password(show_password_btn_2, password2, show_password_btn_icon_2)

password_input_defaulter(password1, show_password_btn_icon_1, show_password_btn_1)
password_input_defaulter(password2, show_password_btn_icon_2, show_password_btn_2)

focus_input_field(username_icon, username)
focus_input_field(email_icon, email)
focus_input_field(firstname_icon, first_name)
focus_input_field(lastname_icon, last_name)
focus_input_field(password1_icon, password1)
focus_input_field(password2_icon, password2)

function focus_input_field(element, input_field) {
    element.addEventListener('click', e=>{
        input_field.focus();
    })
}

function password_input_defaulter(input, icon, btn) {
    input.addEventListener('focusout', e=>{
    input.type = 'password';
    icon.setAttribute('class', 'fas fa-eye');
    btn.setAttribute('title', 'Show Password');
})
}

function show_hide_password(btn, input, icon) {
    btn.addEventListener('click', e=>{
        switch (input.type) {
            case 'text':
                input.type = 'password';
                input.focus();
                icon.setAttribute('class', 'fas fa-eye');
                btn.setAttribute('title', 'Show Password');
                break;
            default:
                input.type = 'text';
                input.focus();
                icon.setAttribute('class', 'fas fa-eye-slash');
                btn.setAttribute('title', 'Hide Password');
                break;
        }
    })
}