$(document).ready(function(){
	var niveis = ['.primeiro_nivel','.segundo_nivel','.terceiro_nivel','.quarto_nivel'];

	// hide onload
	for (var j = 0; niveis.length>j; j++){
		$(niveis[j]).children('ul').addClass('nav_hide');
	}

	// toggle hide
	for (var i = 0; niveis.length>i; i++){
		$(niveis[i]).click(function(){
			$(this).children('ul').toggleClass('nav_hide');
		});
	}
});