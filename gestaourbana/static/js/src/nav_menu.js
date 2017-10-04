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
	$('.expansor').each(function(){
		$(this).on('click', function() {
			menuToggle(this);
		});
	});
	//navegação por tab, shift+tab e enter
	$(document).keypress(function(e) {
		if (e.which == 13) {
			var active = document.activeElement;
			var index_number = active.tabIndex;
			var collpased_children = $(active).next('ul').children('li');
			var level = index_number.toString();		 // 1000 - primeiro nível / 1100 - segundo nível / 1110 - terceiro nível
			var level_count = level.split("0").length-1; //    3 - primeiro nível /    2 - segundo nível /    1 - terceiro nível
			collpased_children.each(function() {
				switch (level_count) {
					case 3: index_number = index_number+100; break;
					case 2: index_number = index_number+10; break;
					case 1: index_number = index_number+1; break;
				}
				$(this).attr('tabindex', index_number);
			});
			if (active.nodeName!=="BUTTON"){ //ignora ação de enter em botão - sobrepõe-se a default
				menuToggle($(active));
			}
			if (active.firstChild.localName == 'a') { //se é link redireciona para link
				window.location.href = active.firstChild.href;
			}
		}
	});
	//menu toggle para telas menores que 750px
	$('button.menu_btn').click(function() {
		$(this).children('span').each(function() {
			$(this).toggleClass('open');
		});
		$('header, #rodape').slideToggle(280);
		$('#nav-menu').slideToggle(300);
	});
});
console.log('A');
