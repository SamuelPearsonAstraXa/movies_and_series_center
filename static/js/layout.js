$('.aside-navbar-toggler').click(e=>{
    $('.aside-navbar').toggle(500);
})

sub_links_toggler('movies-link', 'movies-sub-menu', 'movies-link-icon', ['series-sub-menu', 'actors-sub-menu', 'facts-sub-menu', 'affiliates-sub-menu', 'profile-sub-menu'], ['series-link-icon', 'actors-link-icon', 'facts-link-icon', 'affiliate-link-icon', 'profile-link-icon'])
sub_links_toggler('series-link', 'series-sub-menu', 'series-link-icon', ['movies-sub-menu', 'actors-sub-menu', 'facts-sub-menu', 'affiliates-sub-menu', 'profile-sub-menu'], ['movies-link-icon', 'actors-link-icon', 'facts-link-icon', 'affiliate-link-icon', 'profile-link-icon'])
sub_links_toggler('actors-link', 'actors-sub-menu', 'actors-link-icon', ['series-sub-menu', 'movies-sub-menu', 'facts-sub-menu', 'affiliates-sub-menu', 'profile-sub-menu'], ['series-link-icon', 'movies-link-icon', 'facts-link-icon', 'affiliate-link-icon', 'profile-link-icon'])
sub_links_toggler('facts-link', 'facts-sub-menu', 'facts-link-icon', ['series-sub-menu', 'actors-sub-menu', 'movies-sub-menu', 'affiliates-sub-menu', 'profile-sub-menu'], ['series-link-icon', 'actors-link-icon', 'movies-link-icon', 'affiliate-link-icon', 'profile-link-icon'])
sub_links_toggler('affiliate-link', 'affiliates-sub-menu', 'affiliate-link-icon', ['series-sub-menu', 'actors-sub-menu', 'facts-sub-menu', 'movies-sub-menu', 'profile-sub-menu'], ['series-link-icon', 'actors-link-icon', 'facts-link-icon', 'movies-link-icon', 'profile-link-icon'])
sub_links_toggler('profile-link', 'profile-sub-menu', 'profile-link-icon', ['series-sub-menu', 'actors-sub-menu', 'facts-sub-menu', 'movies-sub-menu', 'affiliates-sub-menu'], ['series-link-icon', 'actors-link-icon', 'facts-link-icon', 'movies-link-icon', 'affiliate-link-icon'])

document.addEventListener('scroll', e=>{
    // document.querySelector('.aside-navbar').
    $('.aside-navbar').slideUp(500);
})

function sub_links_toggler(main_link, sub_links, icon, menus_to_hide, icons_to_reset) {
    $(`.${main_link}`).click(e=>{

        console.log($(`.movies-link-icon`))

        for (let i = 0; i < menus_to_hide.length; i++) {
            const menu = menus_to_hide[i];
            $(`.${menu}`).slideUp(500);
        }

        $(`.${sub_links}`).toggle(500);
        $(`.${icon}`).toggleClass('fa-angle-up');

        for (let i = 0; i < icons_to_reset.length; i++) {
            const icon = icons_to_reset[i];
            $(`.${icon}`).removeClass('fa-angle-up');
        }
    })
}