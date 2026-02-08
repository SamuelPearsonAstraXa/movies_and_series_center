const username = document.getElementById('id_username');
const password = document.getElementById('id_password');
const show_password_btn = document.getElementById('show-password');
const show_password_btn_icon = document.querySelector('#show-password i');

const username_icon = document.querySelector('.username-icon');
const password_icon = document.querySelector('.password-icon');

const form = document.getElementById('user-login-form');
const loader = document.querySelector('.loader');

username.setAttribute('autocomplete', 'new-username')
password.setAttribute('autocomplete', 'new-password')

username.setAttribute('placeHolder', 'Email address')
username.setAttribute('title', 'Email address')
password.setAttribute('placeHolder', 'Password')
password.setAttribute('title', 'Password')
show_password_btn.setAttribute('title', 'Show Password')

focus_input_field(password_icon, password)
focus_input_field(username_icon, username)

// password.addEventListener('focusout', e=>{
//     password.type = 'password';
//     show_password_btn_icon.setAttribute('class', 'fas fa-eye');
//     show_password_btn.setAttribute('title', 'Show Password');
// })

form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'block';

    const form_data = new FormData(form)
    console.log(form_data.values())

    fetch(form.action, {
        method: 'POST',
        body: form_data,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loader.style.display = 'none';
            response_msg.style.display = 'block';
            response_msg.innerHTML = `<p style='color:green; text-align: center;'>Login successful, redirecting...</p>`
            setTimeout(() => {
                window.location = data.success_url;
            }, 2000);
        }else{
            loader.style.display = 'none';
            response_msg.style.display = 'block';

            // let error_html = `<ul style='color:red;'>`;
            // for (let field in data.error){
            //     error_html += `<li><strong> ${field.toUpperCase()}:</strong> ${data.error[field]} </li>`;
            // }
            // error_html += '</ul>';
            // response_msg.innerHTML = error_html;
            console.log(data.error['__all__'])
            response_msg.innerHTML = `<p style='color:red;'>${data.error['__all__']}</p>`;
        }
    })

    .catch(error => {
        console.error('Error >>>>>>', error);
        loader.style.display = 'none';
        response_msg.style.display = 'block';
        response_msg.innerHTML = `<p style='color:red;'>There was an error during the login process.</p>`
    })
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