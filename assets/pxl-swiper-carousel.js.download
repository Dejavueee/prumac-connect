( function( $ ) {
    if( typeof Swiper == 'undefined') return;
    $( window ).on( 'elementor/frontend/init', function() {
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_clients.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_post_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_testimonial_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_team_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_image_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_fancy_box_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_history_carousel.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_slider.default', function( $scope ) {
            pxl_swiper_handler($scope);
        } );
    } );
    $( document ).ready( function() {
        $('.pxl-theme-carousel').each(function() {
            pxl_swiper_handler($(this));
        });
        
        pxl_swiper_handler( $('.pxl-product-swiper-slider') );
        
        pxl_swiper_handler( $('.pxl-product-loop-carousel .pxl-product-carousel') );
          
    });
    $(document).ajaxComplete(function(event, xhr, settings){  
        "use strict";
    });
    function pxl_swiper_handler($scope){
        var $carousel_dom = $scope.find('.pxl-swiper-slider');
        if( $scope.hasClass('pxl-swiper-slider') )
            $carousel_dom = $scope;

        $carousel_dom.each(function(index, element) { 
            var $this = $(this);
            
            var settings = $this.find(".pxl-swiper-container").data().settings;
            
            var next_el = $this.find('.pxl-swiper-arrow-next')[0];
            var prev_el = $this.find('.pxl-swiper-arrow-prev')[0]; 
            var dots_el = $this.find('.pxl-swiper-dots')[0];

            if( $this.hasClass('swiper-parent')){
                settings = $this.find('.pxl-swiper-container.swiper-parent').data().settings;
                next_el = $this.find('.pxl-swiper-arrow-next.swiper-parent')[0];
                prev_el = $this.find('.pxl-swiper-arrow-prev.swiper-parent')[0];
                dots_el = $this.find('.pxl-swiper-dots.swiper-parent')[0];
            }
             
            if( $this.find('.pxl-swiper-slider-thumbs .pxl-swiper-arrows').length > 0){
                next_el = [$this.find('.pxl-swiper-arrow-next')[0], $this.find('.pxl-swiper-arrow-next')[1]];
                prev_el = [$this.find('.pxl-swiper-arrow-prev')[0], $this.find('.pxl-swiper-arrow-prev')[1]]; 
            }
            if( $this.find('.pxl-swiper-slider-thumbs .pxl-swiper-dots').length > 0){
                dots_el = [$this.find('.pxl-swiper-dots')[0], $this.find('.pxl-swiper-dots')[1]];
            }
            var carousel_settings = {
                direction: settings['slide_direction'],
                effect: settings['slide_mode'],
                wrapperClass : 'pxl-swiper-wrapper',
                slideClass: 'pxl-swiper-slide',
                slidesPerView: settings['slides_to_show'],
                slidesPerGroup: settings['slides_to_scroll'],
                slidesPerColumn: settings['slide_percolumn'],
                spaceBetween: parseInt(settings['slides_gutter']),
                autoplayDisableOnInteraction: false,
                lazy: true,
                navigation: {
                    nextEl: next_el,
                    prevEl: prev_el
                }, 
                pagination: {
                    el: dots_el,
                    clickable: true,
                    type: settings['dots_style'] === 'bullets' || settings['dots_style'] == 'bullets-number'
                        ? 'bullets' 
                        : settings['dots_style'],
                    modifierClass: 'pxl-swiper-pagination-',
                    bulletClass: 'pxl-swiper-pagination-bullet',
                },
                
                speed: parseInt(settings['speed']),
                watchSlidesProgress: true,
                watchSlidesVisibility: true,
                //allowTouchMove: false,
                observer: true,
                observeParents: true,
                creativeEffect: {
                    prev: {
                        shadow: true,
                        translate: ["-120%", 0, -500],
                    },
                    next: {
                        shadow: true,
                        translate: ["120%", 0, -500],
                    }
                },
                breakpoints: {
                    0 : {
                        slidesPerView: settings['slides_to_show_xs'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter_xs']
                    },
                    576 : {
                        slidesPerView: settings['slides_to_show_sm'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter_sm']
                    },
                    768 : {
                        slidesPerView: settings['slides_to_show_md'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter_md']
                    },
                    992 : {
                        slidesPerView: settings['slides_to_show_lg'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter_lg']
                    },
                    1200 : {
                        slidesPerView: settings['slides_to_show'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter_xl']
                    },
                    1600 : {
                        slidesPerView: settings['slides_to_show_xxl'],
                        slidesPerGroup: settings['slides_to_scroll'],
                        spaceBetween: settings['slides_gutter']
                    }
                },
                on: {
                    beforeInit: function (swiper){ 
                        $this.addClass('pxl-swiper-initialized');
                    },
                    afterInit: function (swiper){ 
                        if ( typeof settings['active_index'] !== 'undefined' && settings['active_index'] > 0) {
                            var activeIndex = this.activeIndex;
                            this.slideTo( activeIndex + settings['active_index']);
                        }
                    },
                    init : function (swiper){   
                        if (settings['auto_height']) setSlideHeight(this);
                    },
                    slideChangeTransitionStart : function (swiper){
                        $this.find('.pxl-swiper-arrows').addClass('changing');
                        $this.removeClass('slide-transited');
                    },
                    slideChangeTransitionEnd : function (swiper){ 
                        $this.find('.pxl-swiper-arrows').removeClass('changing');
                        $this.addClass('slide-transited');
                        let $activeSlide = $(swiper.slides[swiper.activeIndex]);
                        setTimeout(() => {
                            $(document.body).trigger('pxl_effect_refreshed', [$activeSlide]);
                        }, 100);
                        if (settings['auto_height']) setSlideHeight(this);
                    },
                    slideChange: function (swiper) {
                    },
                },

            };

            if (settings['dots_style'] === 'bullets-number') {
                carousel_settings.pagination = {
                    el: dots_el,
                    clickable: true,
                    type: 'custom',
                    renderCustom: function (swiper, current, total) {

                        const currentFormatted = String(current).padStart(2, '0');
                        const totalFormatted = String(total).padStart(2, '0');

                        let bullets = '';
                        for (let i = 1; i <= total; i++) {
                            bullets += `
                                <span class="pxl-swiper-pagination-bullet ${i === current ? 'swiper-pagination-bullet-active' : ''}">
                                </span>
                            `;
                        }

                        return `
                            <div class="swiper-pagination-custom-wrap">
                                <div class="swiper-pagination-custom-number">${currentFormatted}/${totalFormatted}</div>
                                <div class="swiper-pagination-custom-bullets">
                                    ${bullets}
                                </div>
                            </div>
                        `;
                    }
                };
            }

            

            
              
            if(settings['center_slide'] || settings['center_slide'] == 'true')
                carousel_settings['centeredSlides'] = true;

            if(settings['auto_height'] || settings['auto_height'] == 'true')
                carousel_settings['auto_height'] = true;
            // loop
            if(settings['loop'] || settings['loop'] === 'true'){
                carousel_settings['loop'] = true;
            }
            // auto play
            if (settings['disableAutoplay'] || settings['disableAutoplay'] === 'true') {
                carousel_settings['autoplay'] = false;
            }
            else {
                if(settings['autoplay'] || settings['autoplay'] === 'true'){
                    carousel_settings['autoplay'] = {
                        delay : settings['delay'],
                        disableOnInteraction : settings['pause_on_interaction']
                    };
                } else {
                    carousel_settings['autoplay'] = false;
                }
            }

            //mousewheel
            if (settings['mousewheel'] || settings['mousewheel'] === 'true') {
                carousel_settings['mousewheel'] = {
                    releaseOnEdges: true,
                };
                
            }
            
            if (settings['slide_mode'] === 'gl' && settings['cards_style'] ==='gl1') {
                carousel_settings.modules = [SwiperGL];
                carousel_settings.effect = 'gl';
                carousel_settings.gl = {
                    shader: "squares"
                };
            }

            if (settings['slide_mode'] === 'gl' && settings['cards_style'] === 'gl2') {
                carousel_settings.modules = [SwiperGL];
                carousel_settings.effect = 'gl';
                carousel_settings.gl = {
                    shader: "slices"
                };
            }

  
            if($this.find('.pxl-swiper-thumbs').length > 0){  
                
                var thumb_carousel_settings = pxl_get_thumbs_setting($this.find('.pxl-swiper-thumbs'));
                thumb_carousel_settings['slideThumbActiveClass'] = 'swiper-slide-thumb-active';
                thumb_carousel_settings['thumbsContainerClass'] = 'swiper-container-thumbs';
                var slide_thumbs = new Swiper($this.find('.pxl-swiper-thumbs')[0], thumb_carousel_settings);
 
                slide_thumbs.on('resize', function () {
                    slide_thumbs.changeDirection(getDirection($this.find('.pxl-swiper-thumbs')));
                });
 
                carousel_settings['thumbs'] = { swiper: slide_thumbs, autoScrollOffset: 1 };
                //carousel_settings['loopedSlides'] = 3;
               
            }
            
             
            var swiper = new Swiper($this.find('.pxl-swiper-container')[0], carousel_settings);

            if(settings['autoplay'] && settings['pause_on_hover'] ){
                $( $this.find('.pxl-swiper-container') ).on({
                    mouseenter: function mouseenter() {
                        swiper.autoplay.stop();
                    },
                    mouseleave: function mouseleave() {
                        swiper.autoplay.start();
                    }
                });
            } 

            function setSlideHeight(swiper){
                const $container = $(swiper.el);
                const $wrapper   = $container.find('.pxl-swiper-wrapper');
                const $slides    = $container.find('.pxl-swiper-slide');

                $slides.css({ height: 'auto' });

                const currentSlide = swiper.activeIndex;
                const newHeight = $slides.eq(currentSlide).outerHeight(true);

                $wrapper.css({ height: newHeight });
                $slides.css({ height: newHeight });

                swiper.update();
            }

            swiper.on('slideChangeTransitionEnd', function () {
                let layout1 = document.querySelector('.pxl-testimonial-carousel.layout-1');
            
                if (!layout1) return;
            
                let slides = layout1.querySelectorAll('.pxl-swiper-slide');
                slides.forEach(slide => {
                    slide.classList.remove('custom-prev-before-next', 'custom-next-after-prev', 'custom-next-after-next', 'custom-prev-before-prev');
                });
            
                let nextSlide = layout1.querySelector('.pxl-swiper-slide.swiper-slide-next');
                let prevSlide = layout1.querySelector('.pxl-swiper-slide.swiper-slide-prev');
            
                if (nextSlide && nextSlide.nextElementSibling) {
                    nextSlide.nextElementSibling.classList.add('custom-prev-before-next');
                }
            
                if (prevSlide && prevSlide.previousElementSibling) {
                    prevSlide.previousElementSibling.classList.add('custom-next-after-prev');
                }
            });
            

            
            $this.find(".swiper-filter-wrap .filter-item").on("click", function(){
                var target = $(this).attr('data-filter-target');
                var parent = $(this).closest('.pxl-swiper-slider');
                $(this).siblings().removeClass("active");
                $(this).addClass("active");

                if(target == "all"){
                    parent.find("[data-filter]").removeClass("non-swiper-slide").addClass("swiper-slide");
                    swiper.destroy();
                    swiper = new Swiper($this.find('.pxl-swiper-container')[0], carousel_settings);

                }else {
                     
                    parent.find(".swiper-slide").not("[data-filter^='"+target+"'], [data-filter*=' "+target+"']").addClass("non-swiper-slide").removeClass("swiper-slide");
                    parent.find("[data-filter^='"+target+"'], [data-filter*=' "+target+"']").removeClass("non-swiper-slide").addClass("swiper-slide");
                    
                    swiper.destroy();
                    swiper = new Swiper($this.find('.pxl-swiper-container')[0], carousel_settings);
                }
            });
            
        });  

    }
    
    function getDirection($thumb_node) {
        var windowWidth = window.innerWidth;
        var thumbs_settings = $thumb_node.data().settings;
        var direction = (window.innerWidth <= 991 && typeof thumbs_settings['slide_direction_mobile'] !== 'undefined' ) ? thumbs_settings['slide_direction_mobile'] : thumbs_settings['slide_direction'];
        
        return direction;
    }
    function pxl_get_thumbs_setting($thumb_node){  
        var thumbs_settings = $thumb_node.data().settings, 
            thumbs_settings_params = {
                direction: getDirection($thumb_node),
                effect: thumbs_settings['slide_mode'],
                wrapperClass : 'pxl-thumbs-wrapper',
                slideClass: 'pxl-swiper-slide',
                slidesPerView: thumbs_settings['slides_to_show'],
                slidesPerGroup: thumbs_settings['slides_to_scroll'],
                slidesPerColumn: thumbs_settings['slide_percolumn'],
                spaceBetween: thumbs_settings['slides_gutter'],
                speed: parseInt(thumbs_settings['speed']),
                watchSlidesProgress: true,
                slideToClickedSlide: true,
                watchSlidesVisibility: true,      
                observer: true,
                observeParents: true,

                breakpoints: {
                    0 : {
                        slidesPerView: thumbs_settings['slides_to_show_xs'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                    },
                    576 : {
                        slidesPerView: thumbs_settings['slides_to_show_sm'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                    },
                    768 : {
                        slidesPerView: thumbs_settings['slides_to_show_md'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                    },
                    992 : {
                        slidesPerView: thumbs_settings['slides_to_show_lg'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                    },
                    1200 : {
                        slidesPerView: thumbs_settings['slides_to_show'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                        spaceBetween: thumbs_settings['slides_gutter'],
                    },
                    1400 : {
                        slidesPerView: thumbs_settings['slides_to_show_xxl'],
                        slidesPerGroup: thumbs_settings['slides_to_scroll'],
                        spaceBetween: thumbs_settings['slides_gutter'],
                    }
                },
                  
            }; 
            
            if(thumbs_settings['allow_touch_move'] == false)
                thumbs_settings_params['allowTouchMove'] = false;

            if(thumbs_settings['center_slide'] || thumbs_settings['center_slide'] == 'true')
                thumbs_settings_params['centeredSlides'] = true;

            // loop
            if(thumbs_settings['loop'] || thumbs_settings['loop'] === 'true'){
                thumbs_settings_params['loop'] = true;
            }
            // auto play
            if(thumbs_settings['autoplay'] || thumbs_settings['autoplay'] === 'true'){
                thumbs_settings_params['autoplay'] = {
                    delay : thumbs_settings['delay'],
                    disableOnInteraction : thumbs_settings['pause_on_interaction']
                };
            } else {
                thumbs_settings_params['autoplay'] = false;
            }

            if(thumbs_settings['slides_gutter_lg']){
                thumbs_settings_params['breakpoints'][0]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_lg']);
                thumbs_settings_params['breakpoints'][576]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_lg']);
                thumbs_settings_params['breakpoints'][768]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_lg']);
                thumbs_settings_params['breakpoints'][992]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_lg']);
            }

            if(thumbs_settings['slides_gutter_md']){
                thumbs_settings_params['breakpoints'][0]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_md']);
                thumbs_settings_params['breakpoints'][576]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_md']);
                thumbs_settings_params['breakpoints'][768]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_md']);
            }

            if(thumbs_settings['slides_gutter_sm']){
                thumbs_settings_params['breakpoints'][0]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_sm']);
                thumbs_settings_params['breakpoints'][576]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_sm']);
            }
            if(thumbs_settings['slides_gutter_xs']){
                thumbs_settings_params['breakpoints'][0]['spaceBetween'] = parseInt(thumbs_settings['slides_gutter_xs']);
            }
 
        return thumbs_settings_params;
    }



} )( jQuery );