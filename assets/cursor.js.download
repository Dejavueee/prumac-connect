;(function ($) {
  	"use strict";
  
    if($(document).find('.pxl-cursor-icon').length > 0){ 
		var cursor_icon  = $(".pxl-cursor-icon");
		var follower     = $(".pxl-cursor-follower");
		var cursor_img   = $(".cursor-img");
	    var posX = 0,
	        posY = 0,
	        posX1 = 0,
	        posY1 = 0;
         
	    var mouseX = 0,
	        mouseY = 0;

	    if( cursor_img.length > 0){
	        gsap.set(cursor_img, {
	            scale: 0
	        });
	    }
  
        $(document).on("mousemove", function(e) {
	        mouseX = e.clientX;
	        mouseY = e.clientY;
	    });

	    var tl = gsap.timeline({
            paused: true
        });

	    if( cursor_img.length > 0){
	        tl.to(cursor_img, {
	            scale: 1,
	            opacity: 1,
	            duration: 0.5,
	            ease: "expo.inOut"
	        });
	    }

		initCursor();
		extraCursor();

	    function initCursor() {
	    	var cursor_icon_width = cursor_icon.width();
	    	var cursor_follower_width = follower.width();
	    	if( cursor_img.length > 0){
		    	var cursor_img_width = cursor_img.width();
		    }
	    	TweenMax.to({}, 0.01, {
				repeat: -1,
				onRepeat: function() {
					posX += (mouseX - posX) / 1;
					posY += (mouseY - posY) / 1;
					posX1 += (mouseX - posX1) / 9;
					posY1 += (mouseY - posY1) / 9;
					if($(".pxl-cursor-icon.active").length > 0){
						TweenMax.set($(".pxl-cursor-icon.active"), {
						    css: {
							    left: posX - (cursor_icon_width / 2),
							    top: posY - (cursor_icon_width / 2)
						    }
						});
					}
					if(cursor_img.length > 0){
						TweenMax.set(cursor_img, {
						    css: {
							    left: posX1 - (cursor_img_width / 2) - 2,
							    top: posY1 - (cursor_img_width / 2) - 2
						    }
						});
					}
				}
		    });
		    
	    }

      	function show_cursor(cur, bool){  
			cur.addClass("active");   
  			if(bool == true){
  				cursor.removeClass("active").addClass('hide');  
  				follower.removeClass("active").addClass('hide');  
  			} 
      	}
      	function hide_cursor(cur, bool){
			cur.removeClass("active");     
  			if(bool == true){
  				cursor.removeClass("hide");  
  				follower.removeClass("hide");  
  			}  
      	}
       
      	 
      	function extraCursor(){
      		
	      	$('.product-main-img.pxl-light-gallery .zoom').on("mouseenter", function() {  
		        show_cursor(cursor_icon, false);   
		        cursor_icon.removeClass('hide'); 
		    });
		    $('.product-main-img.pxl-light-gallery .zoom').on("mouseleave", function() {
		        hide_cursor(cursor_icon, false);   
		        cursor_icon.css({
	      			top: '24px',
	      			left: 'auto',
	      			right: '36px'
	      		});
		    }); 
 
		    $('.pxl-page-overlay').on("mouseenter", function() {
		        show_cursor(cursor_icon, false);    
		        $('.product-main-img .pxl-cursor-icon').removeClass('active');
		    });
		    $('.pxl-page-overlay').on("mouseleave", function() {  
		        hide_cursor(cursor_icon, false);    
		    });

		    $('.pxl-hidden-template.pos-center').on("mouseenter", function() {  
		        show_cursor(cursor_icon, false);    
		    });
		    $('.pxl-hidden-template.pos-center').on("mouseleave", function() {  
		        hide_cursor(cursor_icon, false);    
		    });

		    $('.pxl-hidden-template.menu-page-popup').on("mouseenter", function() {  
		        show_cursor(cursor_icon, false);    
		    });
		    $('.pxl-hidden-template.menu-page-popup').on("mouseleave", function() {  
		        hide_cursor(cursor_icon, false);    
		    });

		    $('.pxl-hidden-template.pos-center .pxl-hidden-template-wrap').on("mouseenter", function() {  
		        hide_cursor(cursor_icon, false);    
		    });
		    $('.pxl-hidden-template.pos-center .pxl-hidden-template-wrap').on("mouseleave", function() {  
		        show_cursor(cursor_icon, false);    
		    });
		    $('.pxl-hidden-template.menu-page-popup .pxl-hidden-template-wrap').on("mouseenter", function() {  
		        hide_cursor(cursor_icon, false);    
		    });
		    $('.pxl-hidden-template.menu-page-popup .pxl-hidden-template-wrap').on("mouseleave", function() {  
		        show_cursor(cursor_icon, false);    
		    });
 
		    $('.pxl-tabs-list.hover-img-yes .content-item .item-title').on("mouseenter", function() {
		        var target = $(this).closest('.content-item').attr('data-target');
		        var item_cls = target.substring(1, target.length);
		        cursor_img.find('.'+item_cls).addClass('active');
		        tl.play();
		    });
		    $('.pxl-tabs-list.hover-img-yes .content-item .item-title').on("mouseleave", function() {
		        var target = $(this).closest('.content-item').attr('data-target');
		        var item_cls = target.substring(1, target.length);
		        cursor_img.find('.'+item_cls).removeClass('active');
		        tl.reverse();
		    });
  			 
      	}
    } 
    
     
})(jQuery);