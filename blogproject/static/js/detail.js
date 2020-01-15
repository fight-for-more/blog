$(function () {
    var $catalog = $('.catalog');
    var $note =  $('.note');
    $(window).scroll(function() {
        var $top = $(document).scrollTop();
        if($top>230){
            $catalog.css({
                'position': 'fixed',
                'top': '0',
                'width': '195px',
            });
            $note.removeClass('col-lg-offset-1');
            $note.addClass('col-lg-offset-3');
        }
        else{
            $catalog.css({
                'position': 'static',
            });
            $note.removeClass('col-lg-offset-3');
            $note.addClass('col-lg-offset-1');
        }
    })
})