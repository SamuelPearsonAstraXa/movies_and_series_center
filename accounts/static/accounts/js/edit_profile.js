const image_input = document.getElementById('id_profile_img');
const preview_container = document.getElementById('preview_container');
const form = document.getElementById('edit-user-profile-form');
const loader = document.querySelector('.loader');

loader.style.display = 'none';

form.addEventListener('submit', e=>{
    e.preventDefault();
    loader.style.display = 'block';

    fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: {
            'X-Requested-with': 'XMLHttpRequest'
        }
    })

    .then(response => response.json())

    .then(data => {
        if (data.success) {
            loader.style.display = 'none';
            document.getElementById('response_msg').innerHTML = `<p style='color:green;'>Your profile has been updated successfully!</p>`
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
        document.getElementById('response_msg').innerHTML = `<p style='color:red;'>There was an error while updating your profile.</p>`
    })
})

image_input.addEventListener('change', e=>{
    const img_file = image_input.files[0];
    if(img_file){
        const reader = new FileReader();
        reader.onload = e=>{
            preview_container.innerHTML = `
                <h5>New profile image</h5>
                <img src="${e.target.result}" alt="New image preview">
                <p>${img_file.name}</p>
            `;
        };
        reader.readAsDataURL(img_file);
    }
});

