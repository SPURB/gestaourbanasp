$(document).ready(function(){
	//menu toggle itens
	function menuToggle(el){
		if ($(el).next('ul').hasClass('expanded')) {
			$(el).next('ul').toggleClass('expanded').slideUp(300);
		}
		else {
			$(el).next('ul').attr('style', 'display:none;').slideDown(300);
			$(el).next('ul').toggleClass('expanded');
		};
	}

	function indexLevel(){
		return document.activeElement.tabIndex.toString().length;
	}

	$('.expansor').each(function(){
		$(this).on('click', function() {
			menuToggle(this);
		});
	});

	//acessibility shift and enter key control
	$(document).keypress(function(e) {
		if(e.which == 13) {
			var index_number = document.activeElement.tabIndex;
			var collpased_children = $(document.activeElement).next('ul').children('li');

			collpased_children.each(function() {
				index_number = index_number+1;
				$(this).attr('tabindex', index_number);
			});
			menuToggle($(document.activeElement));
		}
	});

	//menu toggle itself for screens smaller than 750px
	$('button.menu_btn').click(function() {
		$(this).children('span').each(function() {
			$(this).toggleClass('open');
		});
		$('header, #rodape').slideToggle(280);
		$('#nav-menu').slideToggle(300);
	});
});
console.log('A');