$(document).ready(function(){
	var niveis = ['.primeiro_nivel','.segundo_nivel','.terceiro_nivel','.quarto_nivel'];

	for (var i = 0; niveis.length>i; i++){
		$(niveis[i]).click(function(){
			if ($(this).children('ul').is(':hidden')){
				$(this).children('ul').show(300);
			}
			else{
				$(this).children('ul').hide(300);
			}
		});
	}

});

