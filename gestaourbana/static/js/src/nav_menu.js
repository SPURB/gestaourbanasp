$(document).ready(function(){
	if ($('#nav-menu')) {
		$('.expansor').each(function(){
			$(this).on('click', function() {
				if ($(this).next('ul').hasClass('expanded')) {
					$(this).next('ul').toggleClass('expanded').slideUp(300);
				}
				else {
					$(this).next('ul').attr('style', 'display:none;').slideDown(300);
					$(this).next('ul').toggleClass('expanded');
				};
			});
		});
	};
});