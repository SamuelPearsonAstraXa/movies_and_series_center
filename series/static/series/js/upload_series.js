const upload_series_form = document.getElementById('upload-series-form');
const loader = document.querySelector('.loader');

const title = document.getElementById('id_title');
const description = document.getElementById('id_description');
const production_year = document.getElementById('id_production_year');
const producer = document.getElementById('id_producer');

title.focus();
loader.style.display = 'none';

title.setAttribute('placeHolder', 'Series title');
description.setAttribute('placeHolder', 'Series description');
production_year.setAttribute('placeHolder', 'Year of production');
production_year.setAttribute('min', '1700');
production_year.setAttribute('max', '9999');
producer.setAttribute('placeHolder', 'Series producer');

document.querySelector(`label[for='id_title']`).style.display = 'none';
document.querySelector(`label[for='id_description']`).style.display = 'none';
document.querySelector(`label[for='id_production_year']`).style.display = 'none';
document.querySelector(`label[for='id_producer']`).style.display = 'none';
document.querySelector(`label[for='id_banner_img']`).textContent = 'Series Banner';
document.querySelector(`label[for='id_trailer']`).textContent = 'Series trailer';

upload_series_form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'flex';
    
    fetch(upload_series_form.action, {
        method: 'POST',
        body: new FormData(upload_series_form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })

    .then(response => response.json())
    .then(data => {
        if (data.success){
            loader.style.display = 'none';
            document.getElementById('response_msg').innerHTML = `<p style='color:green;'>Your series has been uploaded.</p>`
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
        document.getElementById('response_msg').innerHTML = `<p style='color:red;'>There was an error while uploading your series.</p>`
    })
})