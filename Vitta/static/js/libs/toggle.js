function menu() {
		$('.menubar-toggle').click(function() {
			if($(".menubar").hasClass("side-fechado")) {
				$('.menubar').animate({
				    left: "0px",
				}, 100, function() {
				    $(".menubar").removeClass("side-fechado");
				});
				$('.general-content').animate({
				    left: "175px",
				}, 100);
			}
			else {
				$('.menubar').animate({
				    left: "-175px",
				}, 100, function() {
				    $(".menubar").addClass("side-fechado");
				});
				$('.general-content').animate({
				    left: "0px",
				}, 100);
			}
		});
	}
	
	$(window).resize(function() {
		var tamanhoJanela = $(window).width();
		$(".menubar-toggle").remove();
		
		if (tamanhoJanela < 800) { 
			$('.menubar').css('left', '-175px').addClass('side-fechado');
			$('.menubar').append( "<div class='menubar-toggle'>Perfil</div>" );
      $('.general-content').css("left", 0);
		} else {
			$('.menubar').css('left', '0px').addClass('side-fechado');
		}
		
		menu();
	});
	
	$(document).ready(function() {
		var tamanhoJanela = $(window).width();
		$(".menubar-toggle").remove();
		
		if (tamanhoJanela < 800) { 
			$('.menubar').css('left', '-175px').addClass('side-fechado');;
			$('.menubar').append( "<div class='menubar-toggle'>Menu</div>" );
		} else {
			$('.menubar').css('left', '0px').addClass('side-fechado');
		}
		
		menu();
	});