const expand_video_btn = document.querySelector('.expand-video-btn');
const expand_video_btn_icon = document.querySelector('.expand-video-btn i');
const play_video_btn = document.querySelector('.play-video-btn');
const play_video_btn_icon = document.querySelector('.play-video-btn i');
const video = document.querySelector('video')
const timer = document.getElementById('timer')
const full_video_duration = document.querySelector('.full-time');
const elapsed_video_duration = document.querySelector('.elapsed-time');
const video_container = document.querySelector('.video-container')
const video_controls = document.querySelector('.video-controls');
const volume_input = document.getElementById('volume-input');
const volume_btn = document.querySelector('.volume-btn');
const volume_icon = document.querySelector('.volume-icon');

// setTimeout(() => {
//     video_controls.style.display = 'none';
// }, 3000);

// video_container.addEventListener('mouseover', e=>{
//     video_controls.style.display = 'block';
// })

// video_container.addEventListener('mouseleave', e=>{
//     setTimeout(() => {
//         video_controls.style.display = 'none';
//     }, 3000);
// })

// video.addEventListener('click', e=>{
//     if(video_controls.style.display == 'none'){
//         video_controls.style.display = 'block';
//     }else{
//         video_controls.style.display = 'none';
//     }
// })

change_volume_icon();

volume_btn.addEventListener('click', e=>{
    if (volume_input.value == 0) {
        volume_input.value = 0.1;
        volume_icon.setAttribute('class', 'fas fa-volume-low volume-icon')
        // change_volume_icon()
    }else{
        volume_input.value = 0;
        volume_icon.setAttribute('class', 'fas fa-volume-mute volume-icon')
        // change_volume_icon()
    }
})

function change_volume_icon() {
    if (Number(video.volume) == 0) {
        volume_icon.setAttribute('class', 'fas fa-volume-mute volume-icon')
    } else if( Number(video.volume) <= 0.5){
        volume_icon.setAttribute('class', 'fas fa-volume-low volume-icon')
    } else {
        volume_icon.setAttribute('class', 'fas fa-volume-high volume-icon')
    }
}

video.volume = Number(volume_input.value);
volume_input.value = video.volume;


document.addEventListener('DOMContentLoaded', e=>{
    timer.max = video.duration;
    if (full_video_duration){
        full_video_duration.textContent = formatTime(video.duration)
    }
    change_volume_icon();
})

video.addEventListener('loadedmetadata', e=>{
    timer.max = video.duration;
    if (full_video_duration){
        full_video_duration.textContent = formatTime(video.duration)
    }
})

volume_input.addEventListener('input', e=>{
    video.volume = Number(volume_input.value);
    change_volume_icon()
})

$('video').click(e=>{
    $('.video-controls').slideToggle(500);
})

video.addEventListener('dblclick', e=>{
    if (video.paused == true) {
        video.play();
        play_video_btn_icon.setAttribute('class', 'fas fa-pause');
    }else{
        video.pause();
        play_video_btn_icon.setAttribute('class', 'fas fa-play');
    }
})

// video_controls.addEventListener('mouseover', e=>{
//     video_controls.style.display = 'block';
// })

expand_video_btn.addEventListener('click', async() =>{
    if(document.fullscreenElement){
        document.exitFullscreen();
        expand_video_btn_icon.setAttribute('class', 'fas fa-expand')
    }else{
        await video_container.requestFullscreen();
        expand_video_btn_icon.setAttribute('class', 'fas fa-minimize')
        if (isSmallScreen() && screen.orientation && screen.orientation.lock) {
            try {
                await screen.orientation.lock('landscape');
            } catch (error) {
                console.warn('Orientation lock failed: ', error)
            }
        }
    }
})

document.addEventListener('fullscreenchange', e=>{
    if (!document.fullscreenElement) {
        if(screen.orientation && screen.orientation.unlock){
            screen.orientation.unlock();
        }
        expand_video_btn_icon.setAttribute('class', 'fas fa-expand')
    }
})

timer.addEventListener('click', e=>{
    if(!Number.isFinite(video.duration)){
        return;
    }else{
        const rect = timer.getBoundingClientRect();
        const postion = (e.clientX - rect.left) / timer.offsetWidth;

        video.currentTime = postion * video.duration;
    }
})

video.addEventListener('timeupdate', e=>{
    updateTime();
    if(!timer.getAttribute('max')){
        timer.setAttribute('max', video.duration)
    }
    timer.value = video.currentTime;
})

timer.addEventListener('input', e=>{
    video.currentTime = timer.value;
})

video.addEventListener('ended', e=>{
    play_video_btn_icon.setAttribute('class', 'fas fa-play');
    timer.value = 0;
})

function isSmallScreen(){
    return window.innerWidth <= 768;
}

function formatTime(seconds){
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes < 10 ? '0' : ''}${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`
}

function updateTime() {
    if (elapsed_video_duration) {
        elapsed_video_duration.textContent = formatTime(video.currentTime)
    }

    if (!isNaN(video.duration) && full_video_duration){
        full_video_duration.textContent = formatTime(video.duration)
    }
}

playVideo(play_video_btn, video, play_video_btn_icon)

function playVideo(btn, vid, icon){
    btn.addEventListener('click', e=>{
        if (vid.paused == true) {
            vid.play();
            icon.setAttribute('class', 'fas fa-pause');
        }else{
            vid.pause();
            icon.setAttribute('class', 'fas fa-play');
        }
    })
}