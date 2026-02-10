const loader = document.querySelector('.loader');
const add_series_review_form = document.getElementById('add_series_review_form');
const text = document.getElementById('id_text');

loader.style.display = 'none';
text.setAttribute('placeholder', 'Review text here...');

add_series_review_form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'block';
    
    fetch(add_series_review_form.action, {
        method: 'POST',
        body: new FormData(add_series_review_form),
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })

    .then(response => response.json())
    .then(data => {
        if (data.success){
            loader.style.display = 'none';
            document.getElementById('response_msg').innerHTML = `<p style='color:green;'>Your review has been posted.</p>`
            setTimeout(() => {
                document.getElementById('response_msg').style.display = 'none';
            }, 2000);
        }else{
            loader.style.display = 'none';
            if (data.error){
                document.getElementById('response_msg').innerHTML = data.error;
            }else{
                const icon = '<i class="fas fa-hand-point-up"></i>'
                document.getElementById('response_msg').innerHTML = `<p style='color:red;'>${data.errors['text']} ${icon} ${icon} ${icon}</p>`;
                text.focus();
            }
        }
    })
    .catch(error => {
        console.error('Error ', error);
        loader.style.display = 'none';
        document.getElementById('response_msg').innerHTML = `<p style='color:red;'>There was an error while adding your review. Make sure you're <a href="/accounts/user-login/?next=${window.location}">logged in!</a></p>`
    })
})