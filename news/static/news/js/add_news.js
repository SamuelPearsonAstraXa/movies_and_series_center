const add_news_form = document.getElementById('add-news-form');
const loader = document.querySelector('.loader');

const title = document.getElementById('id_title');
const content = document.getElementById('id_content');

title.focus();
loader.style.display = 'none';

title.setAttribute('placeHolder', 'News title');
content.setAttribute('placeHolder', 'News content');

document.querySelector(`label[for='id_title']`).style.display = 'none';
document.querySelector(`label[for='id_content']`).style.display = 'none';
document.querySelector(`label[for='id_featured_img']`).textContent = 'Featured image';
document.querySelector(`label[for='id_tags']`).textContent = 'Tags';
document.querySelector(`label[for='id_author']`).textContent = 'Author';

add_news_form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'flex';
    
    fetch(add_news_form.action, {
        method: 'POST',
        body: new FormData(add_news_form),
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