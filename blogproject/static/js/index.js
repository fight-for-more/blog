$(function(){
	var $totop = $('.totop');
	$(window).scroll(function(){
		var iNum = $(document).scrollTop();
		if(iNum>64){
			$totop.fadeIn();
		}
		else{
			$totop.fadeOut();
		}
	})

	$totop.click(function(){
		$('html,body').animate({'scrollTop':0});
	})
})