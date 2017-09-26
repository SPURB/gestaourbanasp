jQuery(document).ready(function(){
	var nav_menu = $('.nav-menu');
	if( nav_menu.length > 0 ) {
		nav_menu.each(function(){
			var accordion = $(this);
			//detecta alterações em input[type="checkbox"]

			accordion.on('change', 'input[type="checkbox"]', function(){
				var checkbox = $(this);
				// console.log(checkbox.prop('checked'));
				( checkbox.prop('checked') ) ? checkbox.siblings('ul').attr('style', 'display:none;').slideDown(300) : checkbox.siblings('ul').attr('style', 'display:block;').slideUp(300);
				// if (checkbox.prop('checked')){
				// 	checkbox.siblings('ul').attr('style', 'display:none;').slideDown(300);
				// }
				// else{
				// 	checkbox.siblings('ul').attr('style', 'display:block;').slideUp(300);
				// }
			});
		});
	}
});