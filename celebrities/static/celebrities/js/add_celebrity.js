const add_celebrity_form = document.getElementById('add-celebrity-form');
const loader = document.querySelector('.loader');

const celebrity_name = document.getElementById('id_name');
const occupation = document.getElementById('id_occupation');
const biography = document.getElementById('id_biography');
const religion = document.getElementById('id_religion');
const academic_history = document.getElementById('id_academic_history');
const home_town = document.getElementById('id_home_town');

// title.focus();
loader.style.display = 'none';

celebrity_name.setAttribute('placeHolder', 'Name');
occupation.setAttribute('placeHolder', 'Occupation');
biography.setAttribute('placeHolder', 'Biography');
religion.setAttribute('placeHolder', 'Religion');
academic_history.setAttribute('placeHolder', 'Academic history');
home_town.setAttribute('placeHolder', 'Home town');

document.querySelector(`label[for='id_name']`).style.display = 'none';
document.querySelector(`label[for='id_occupation']`).style.display = 'none';
document.querySelector(`label[for='id_biography']`).style.display = 'none';
document.querySelector(`label[for='id_religion']`).style.display = 'none';
document.querySelector(`label[for='id_academic_history']`).style.display = 'none';
document.querySelector(`label[for='id_home_town']`).style.display = 'none';

add_celebrity_form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'flex';
    
    fetch(add_celebrity_form.action, {
        method: 'POST',
        body: new FormData(add_celebrity_form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })

    .then(response => response.json())
    .then(data => {
        if (data.success){
            loader.style.display = 'none';
            document.getElementById('response_msg').innerHTML = `<p style='color:green;'>The celebrity has been added.</p>`
            setTimeout(() => {
                window.location = data.success_url;
            }, 2000);
        }else{
            loader.style.display = 'none';

            let error_html = `<ul style='color:red;'>`;
            for (let field in data.error){
                error_html += `<li><strong> ${field.toUpperCase()}:</strong> ${data.error[field]} </li>`;
            }
            error_html += '</ul>';
            document.getElementById('response_msg').innerHTML = error_html;
        }
    })
    .catch(error => {
        console.error('Error ', error);
        loader.style.display = 'none';
        document.getElementById('response_msg').innerHTML = `<p style='color:red;'>There was an error while uploading your movie.</p>`
    })
})