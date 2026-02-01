const password1 = document.getElementById('id_new_password1');
const password2 = document.getElementById('id_new_password2');
const show_password_btn_1 = document.getElementById('show-password1');
const show_password_btn_2 = document.getElementById('show-password2');
const show_password_btn_icon_1 = document.querySelector('#show-password1 i');
const show_password_btn_icon_2 = document.querySelector('#show-password2 i');

password1.setAttribute('placeHolder', 'Create new password')
password1.setAttribute('title', 'Create new password')
password2.setAttribute('placeHolder', 'Confirm your new password')
password2.setAttribute('title', 'Confirm your new password')

show_hide_password(show_password_btn_1, password1, show_password_btn_icon_1)
show_hide_password(show_password_btn_2, password2, show_password_btn_icon_2)

function show_hide_password(btn, input, icon) {
    btn.addEventListener('click', e=>{
        switch (input.type) {
            case 'text':
                input.type = 'password';
                icon.setAttribute('class', 'fas fa-eye');
                btn.setAttribute('title', 'Show Password');
                break;
            default:
                input.type = 'text';
                icon.setAttribute('class', 'fas fa-eye-slash');
                btn.setAttribute('title', 'Hide Password');
                break;
        }
    })
}