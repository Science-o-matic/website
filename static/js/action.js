$().ready(function(){
    $('#mobile-menu-button').click(function(){
        $('#menu-mobile > ul').toggle(0)
        $('header').toggleClass('mobile-menu-height');
    })
});
