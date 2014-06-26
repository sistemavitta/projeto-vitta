function menu() {
		$('.nav-toggle').click(function() {
			if($(".vertical").hasClass("side-fechado")) {
				$('.vertical').animate({
				    left: "0px",
				}, 100, function() {
				    $(".vertical").removeClass("side-fechado");
				});
				$('.content').animate({
				    left: "175px",
				}, 100);
			}
			else {
				$('.vertical').animate({
				    left: "-175px",
				}, 100, function() {
				    $(".vertical").addClass("side-fechado");
				});
				$('.content').animate({
				    left: "0px",
				}, 100);
			}
		});
	}
	
	//Menu Sidebar
	$(window).resize(function() {
		var tamanhoJanela = $(window).width();
		$(".nav-toggle").remove();
		
		if (tamanhoJanela <= 800) { 
			$('.vertical').css('left', '-175px').addClass('side-fechado');
			$('.vertical').append( "<div class='nav-toggle'>Perfil</div>" );
      $('.content').css("left", 0);
		} else {
			$('.vertical').css('left', '0px').addClass('side-fechado');
		}
		
		menu();
	});
	
	$(document).ready(function() {
		var tamanhoJanela = $(window).width();
		$(".nav-toggle").remove();
		
		if (tamanhoJanela <= 800) { 
			$('.vertical').css('left', '-175px').addClass('side-fechado');;
			$('.vertical').append( "<div class='nav-toggle'>Perfil</div>" );
		} else {
			$('.vertical').css('left', '0px').addClass('side-fechado');
		}
		
		menu();
	});