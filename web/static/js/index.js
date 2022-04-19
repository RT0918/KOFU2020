jQuery(function($){
    var navFlg = true;
    var clickflug = true;//最初はtrue(クリック受け付ける)
    $('.menu').on('click',function(){
        if(clickflug){
            clickflug = false;
            $('.menu__line').toggleClass('active');
            $('.gnav').fadeToggle();
            if(navFlg){
                $('.gnav__menu__item').each(function(i){
                    $(this).delay(i).animate({
                        'margin-left' : 0,
                        'opacity' : 1,
                    },200,'easeOutBack');
                });
                navFlg = false;

                setTimeout(function(){
                    clickflug = true;
                },400);//200ミリ秒立ったらtrueになる

            }
            else{
                $('.gnav__menu__item').css({
                    'margin-left' : 100,
                    'opacity' : 0,
                });
                navFlg = true;
                clickflug = true;//初期値に戻したらtrue(初期化完了,一瞬)
            }
        }else{
            return false;
        }
    });
});
