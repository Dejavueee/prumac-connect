( function( $ ) {
    class Pxl_Global_Handler extends elementorModules.frontend.handlers.Base {
        getWidgetType() {
            return 'global';
        }
        animate() {
            var $element = this.$element,
                animation = this.getAnimation();
             
            if ( 'none' === animation || '' === animation ) {
                $element.removeClass( 'pxl-invisible' );
                $element.css('opacity', '1');
                return;
            }
            if( animation == 'gsap'){
                const elementSettings = this.getElementSettings(),  
                    el_class_apply     = elementSettings.pxl_anm_el_class_apply || '',
                    toggle_actions     = elementSettings.pxl_toggle_actions || elements_data.splittext_toggle_actions,
                    animation_delay    = elementSettings.pxl_animation_delay || 0.01,
                    animation_duration = elementSettings.pxl_animation_duration || 1,
                    pxl_once           = elementSettings.pxl_once || '',
                    pxl_gsap_method    = elementSettings.pxl_gsap_method || '',
                    pxl_ease    = elementSettings.pxl_gsap_method || 'none',
                    pxl_stagger    = elementSettings.pxl_stagger || 0;

                const pxl_from = {
                    opacity: 0
                };
                const pxl_to = {
                    opacity: 1
                };

                var pxl_scroll_trigger = {
                    trigger: $element,
                    toggleActions: toggle_actions
                }
 
                if( typeof elementSettings.pxl_from_opacity !== 'undefined' && elementSettings.pxl_from_opacity !== '' ){
                    pxl_from.opacity = elementSettings.pxl_from_opacity;
                }
                if( typeof elementSettings.pxl_from_offset_x !== 'undefined' && elementSettings.pxl_from_offset_x !== ''){
                    pxl_from.x = elementSettings.pxl_from_offset_x;
                }
                if( typeof elementSettings.pxl_from_offset_y !== 'undefined' && elementSettings.pxl_from_offset_y !== ''){
                    pxl_from.y = elementSettings.pxl_from_offset_y;
                }
                if( typeof elementSettings.pxl_from_rotation !== 'undefined' && elementSettings.pxl_from_rotation !==''){
                    pxl_from.rotation = elementSettings.pxl_from_rotation;
                }
                if( typeof elementSettings.pxl_from_rotationx !== 'undefined' && elementSettings.pxl_from_rotationx !==''){
                    pxl_from.rotationX = elementSettings.pxl_from_rotationx;
                }
                if( typeof elementSettings.pxl_from_rotationy !== 'undefined' && elementSettings.pxl_from_rotationy !==''){
                    pxl_from.rotationY = elementSettings.pxl_from_rotationy;
                }
                if( typeof elementSettings.pxl_from_scale !== 'undefined' && elementSettings.pxl_from_scale !== ''){
                    pxl_from.scale = elementSettings.pxl_from_scale;
                }
                if( typeof elementSettings.pxl_from_scalex !== 'undefined' && elementSettings.pxl_from_scalex !== ''){
                    pxl_from.scaleX = elementSettings.pxl_from_scalex;
                }
                if( typeof elementSettings.pxl_from_scaley !== 'undefined' && elementSettings.pxl_from_scaley !== ''){
                    pxl_from.scaleY = elementSettings.pxl_from_scaley;
                }
                if( typeof elementSettings.pxl_from_skewx !== 'undefined' && elementSettings.pxl_from_skewx !==''){
                    pxl_from.skewX = elementSettings.pxl_from_skewx;
                }
                if( typeof elementSettings.pxl_from_skewy !== 'undefined' && elementSettings.pxl_from_skewy !==''){
                    pxl_from.skewY = elementSettings.pxl_from_skewy;
                }
                
                
                
                if( typeof elementSettings.pxl_to_opacity !== 'undefined' && elementSettings.pxl_to_opacity !== ''){
                    pxl_to.opacity = elementSettings.pxl_to_opacity;
                }
                if( typeof elementSettings.pxl_to_offset_x !== 'undefined'  && elementSettings.pxl_to_offset_x !== ''){
                    pxl_to.x = elementSettings.pxl_to_offset_x;
                }
                if( typeof elementSettings.pxl_to_offset_y !== 'undefined'  && elementSettings.pxl_to_offset_y !== ''){
                    pxl_to.y = elementSettings.pxl_to_offset_y;
                }
                if( typeof elementSettings.pxl_to_rotation !== 'undefined'  && elementSettings.pxl_to_rotation !== ''){
                    pxl_to.rotation = elementSettings.pxl_to_rotation;
                }
                if( typeof elementSettings.pxl_to_rotationx !== 'undefined' && elementSettings.pxl_to_rotationx !==''){
                    pxl_to.rotationX = elementSettings.pxl_to_rotationx;
                }
                if( typeof elementSettings.pxl_to_rotationy !== 'undefined' && elementSettings.pxl_to_rotationy !==''){
                    pxl_to.rotationY = elementSettings.pxl_to_rotationy;
                }
                if( typeof elementSettings.pxl_to_rotationz !== 'undefined' && elementSettings.pxl_to_rotationz !==''){
                    pxl_to.rotationZ = elementSettings.pxl_to_rotationz;
                }
                if( typeof elementSettings.pxl_to_scale !== 'undefined'  && elementSettings.pxl_to_scale !== ''){
                    pxl_to.scale = elementSettings.pxl_to_scale;
                }
                if( typeof elementSettings.pxl_to_scalex !== 'undefined' && elementSettings.pxl_to_scalex !== ''){
                    pxl_to.scaleX = elementSettings.pxl_to_scalex;
                }
                if( typeof elementSettings.pxl_to_scaley !== 'undefined' && elementSettings.pxl_to_scaley !== ''){
                    pxl_to.scaleY = elementSettings.pxl_to_scaley;
                }
                if( typeof elementSettings.pxl_to_skewx !== 'undefined' && elementSettings.pxl_to_skewx !==''){
                    pxl_to.skewX = elementSettings.pxl_to_skewx;
                }
                if( typeof elementSettings.pxl_to_skewy !== 'undefined' && elementSettings.pxl_to_skewy !==''){
                    pxl_to.skewY = elementSettings.pxl_to_skewy;
                }
                 
                if( typeof elementSettings.pxl_scrub !== 'undefined'  && elementSettings.pxl_scrub !== ''){
                    pxl_scroll_trigger.scrub = elementSettings.pxl_scrub;
                }
                if( typeof elementSettings.pxl_once !== 'undefined'  && elementSettings.pxl_once !== ''){
                    pxl_scroll_trigger.once = parseInt(elementSettings.pxl_once);
                }
                if( typeof elementSettings.pxl_scroll_start !== 'undefined'  && elementSettings.pxl_scroll_start !== ''){
                    pxl_scroll_trigger.start = elementSettings.pxl_scroll_start;
                }
                if( typeof elementSettings.pxl_scroll_end !== 'undefined'  && elementSettings.pxl_scroll_end !== ''){
                    pxl_scroll_trigger.end = elementSettings.pxl_scroll_end;
                }
 

                //pxl_scroll_trigger.markers = true;
                 
                pxl_to.scrollTrigger = pxl_scroll_trigger;
                pxl_to.duration = animation_duration;
                pxl_to.delay = animation_delay;
                pxl_to.stagger = pxl_stagger;
                pxl_to.ease = pxl_ease;
  
                if( el_class_apply !== '' ){
                    var $ajax_items = $element.find('.ajax-item'); 
                    $element = $element.find('.'+el_class_apply);

                    if( $element.length > 1 ){
                        delete pxl_to.scrollTrigger;
                        if( $ajax_items.length > 0 ){
                            $element = $ajax_items;
                        }
                        ScrollTrigger.batch($element, {
                            onEnter: elements => {
                                if( pxl_gsap_method === 'from'){
                                    gsap.from(elements, pxl_from);
                                }else if( pxl_gsap_method === 'to'){
                                    gsap.to(elements, pxl_to);
                                }else{
                                    gsap.fromTo(elements, pxl_from, pxl_to);
                                }
                            },
                            once: parseInt(pxl_once)
                        });
 
                    }else{
                        if( pxl_gsap_method === 'from'){
                            pxl_from.scrollTrigger = pxl_scroll_trigger;
                            pxl_from.duration = animation_duration;
                            pxl_from.delay = animation_delay;
                            pxl_from.stagger = pxl_stagger;
                            pxl_from.ease = pxl_ease;
                            gsap.from($element, pxl_from);
                        }else if( pxl_gsap_method === 'to'){
                            gsap.to($element, pxl_to);
                        }else{
                            gsap.fromTo($element, pxl_from, pxl_to);
                        }
                    }
                }else{
                    if( pxl_gsap_method === 'from'){
                        pxl_from.scrollTrigger = pxl_scroll_trigger;
                        pxl_from.duration = animation_duration;
                        pxl_from.delay = animation_delay;
                        pxl_from.stagger = pxl_stagger;
                        pxl_from.ease = pxl_ease;
                        gsap.from($element, pxl_from);
                    }else if( pxl_gsap_method === 'to'){
                        gsap.to($element, pxl_to);
                    }else{
                        gsap.fromTo($element, pxl_from, pxl_to);
                    }
                } 
 
            }else{
                const elementSettings = this.getElementSettings(),
                    animation_delay = parseFloat(elementSettings.pxl_animation_delay * 1000) || 0;

                $element.removeClass( animation );

                if ( this.current_animation ) {
                    $element.removeClass( this.current_animation );
                }

                this.current_animation = animation;

                setTimeout( () => {
                    $element.removeClass( 'pxl-invisible' ).addClass( 'pxl-animated ' + animation );
                }, animation_delay );
                
            }
        }

        getAnimation() {
            return this.getCurrentDeviceSetting( 'pxl_animation' );
        }
        
        onInit() {
            if ( this.getAnimation() ) {
                const observer = elementorModules.utils.Scroll.scrollObserver( {
                    callback: ( event ) => {
                        if ( event.isInViewport ) {
                            this.animate();

                            observer.unobserve( this.$element[ 0 ] );
                        }
                    },
                } );

                observer.observe( this.$element[ 0 ] );
            }/*else{
                this.animate();
            }*/
        }
 
        onElementChange( propertyName ) {
            if ( /^pxl_animation?/.test( propertyName ) ) {
                this.animate();
            }
        }
    }
 
    $( window ).on( 'elementor/frontend/init', function() {
        gsap.registerPlugin(ScrollTrigger); 
          
        const addEffectHandler = ( $element ) => {
            elementorFrontend.elementsHandler.addHandler( Pxl_Global_Handler, { $element } );
        };
        elementorFrontend.hooks.addAction( 'frontend/element_ready/global', addEffectHandler );
        
        $( document.body ).on( 'pxl_effect_refreshed', function(e, el) {
            if(el.closest('.pxl-anm-gsap').length > 0){
                var $element = el.closest('.pxl-anm-gsap'); 
                elementorFrontend.elementsHandler.addHandler( Pxl_Global_Handler, { $element } );
            }
        });
 

    } );
 

} )( jQuery );
 