const create_celebrity_news_form = document.getElementById('create-celebrity-news-form');
const loader = document.querySelector('.loader');

const celebrity = document.getElementById('id_celebrity');
const title = document.getElementById('id_title');
const news_text = document.getElementById('id_news_text');
const author = document.getElementById('id_author');

// title.focus();
loader.style.display = 'none';

title.setAttribute('placeHolder', 'News title');
news_text.setAttribute('placeHolder', 'News context here.');

document.querySelector(`label[for='id_title']`).style.display = 'none';
document.querySelector(`label[for='id_news_text']`).style.display = 'none';

create_celebrity_news_form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'flex';
    
    fetch(create_celebrity_news_form.action, {
        method: 'POST',
        body: new FormData(create_celebrity_news_form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })

    .then(response => response.json())
    .then(data => {
        if (data.success){
            loader.style.display = 'none';
            document.getElementById('response_msg').innerHTML = `<p style='color:green;'>Your movie has been uploaded.</p>`
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