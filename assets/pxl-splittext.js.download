( function( $ ) {
    class Pxl_Splittext_Handler extends elementorModules.frontend.handlers.Base {
        split_text(){
            var $this = this,
                $element = this.$element,
                $items      = $element.find('.pxl-split-text');
               
            if ( $items.length <= 0 ) {
                return;
            }

            const elementSettings = this.getElementSettings();  
             
            $items.each(function(index, el) {
                var type = '',
                    sp_opacity = '0',
                    sp_offset_x = '',
                    sp_offset_y = '',
                    sp_rotation = '',
                    sp_rotationx = '',
                    sp_rotationy = '',
                    sp_scale = '',
                    sp_scalex = '',
                    sp_scaley = '',
                    toggle_actions = elements_data.splittext_toggle_actions,
                    transform_origin = '',
                    sp_ease    = 'power1.in',
                    sp_animation_duration = 0.8,
                    sp_stagger = 0.02,
                    sp_animation_delay = '',
                    sp_scrub = '',
                    sp_once = '';
                    
                 
                if( $(el).hasClass('pxl_title_split_text') ){
                    type = $this.getCurrentDeviceSetting( 'title_sp_type' ) || '';
                     
                    if( typeof elementSettings.title_sp_opacity !== 'undefined' && elementSettings.title_sp_opacity !== '' ){
                        sp_opacity = elementSettings.title_sp_opacity;
                    }
                    if( typeof elementSettings.title_sp_offset_x !== 'undefined' && elementSettings.title_sp_offset_x !== '' ){
                        sp_offset_x = elementSettings.title_sp_offset_x;
                    }
                    if( typeof elementSettings.title_sp_offset_y !== 'undefined' && elementSettings.title_sp_offset_y !== '' ){
                        sp_offset_y = elementSettings.title_sp_offset_y;
                    }
                    if( typeof elementSettings.title_sp_rotation !== 'undefined' && elementSettings.title_sp_rotation !== '' ){
                        sp_rotation = elementSettings.title_sp_rotation;
                    }
                    if( typeof elementSettings.title_sp_rotationx !== 'undefined' && elementSettings.title_sp_rotationx !== '' ){
                        sp_rotationx = elementSettings.title_sp_rotationx;
                    }
                    if( typeof elementSettings.title_sp_rotationy !== 'undefined' && elementSettings.title_sp_rotationy !== '' ){
                        sp_rotationy = elementSettings.title_sp_rotationy;
                    }
                    if( typeof elementSettings.title_sp_scale !== 'undefined' && elementSettings.title_sp_scale !== '' ){
                        sp_scale = elementSettings.title_sp_scale;
                    }
                    if( typeof elementSettings.title_sp_scalex !== 'undefined' && elementSettings.title_sp_scalex !== '' ){
                        sp_scalex = elementSettings.title_sp_scalex;
                    }
                    if( typeof elementSettings.title_sp_scaley !== 'undefined' && elementSettings.title_sp_scaley !== '' ){
                        sp_scaley = elementSettings.title_sp_scaley;
                    }
                    if( typeof elementSettings.title_sp_toggle_actions !== 'undefined' && elementSettings.title_sp_toggle_actions !== '' ){
                        toggle_actions = elementSettings.title_sp_toggle_actions;
                    }
                    if( typeof elementSettings.title_sp_once !== 'undefined'  && elementSettings.title_sp_once !== ''){
                        sp_once = parseInt(elementSettings.title_sp_once);
                    }
                    if( typeof elementSettings.title_sp_ease !== 'undefined'  && elementSettings.title_sp_ease !== ''){
                        sp_ease = parseInt(elementSettings.title_sp_ease);
                    }
                    if( typeof elementSettings.title_sp_animation_duration !== 'undefined'  && elementSettings.title_sp_animation_duration !== ''){
                        sp_animation_duration = elementSettings.title_sp_animation_duration;
                    }
                    if( typeof elementSettings.title_sp_animation_delay !== 'undefined'  && elementSettings.title_sp_animation_delay !== ''){
                        sp_animation_delay = elementSettings.title_sp_animation_delay;
                    }
                    if( typeof elementSettings.title_sp_scrub !== 'undefined'  && elementSettings.title_sp_scrub !== ''){
                        sp_scrub = elementSettings.title_sp_scrub;
                    }
                    if( typeof elementSettings.title_sp_stagger !== 'undefined'  && elementSettings.title_sp_stagger !== ''){
                        sp_stagger = elementSettings.title_sp_stagger;
                    }

                    if( typeof elementSettings.title_sp_transform_origin !== 'undefined' && elementSettings.title_sp_transform_origin !== '' ){
                        transform_origin = elementSettings.title_sp_transform_origin;
                    }
                }else if( $(el).hasClass('pxl_subtitle_split_text') ){
                    type = $this.getCurrentDeviceSetting( 'subtitle_sp_type' ) || '';
                   
                    if( typeof elementSettings.subtitle_sp_opacity !== 'undefined' && elementSettings.subtitle_sp_opacity !== '' ){
                        sp_opacity = elementSettings.subtitle_sp_opacity;
                    }
                    if( typeof elementSettings.subtitle_sp_offset_x !== 'undefined' && elementSettings.subtitle_sp_offset_x !== '' ){
                        sp_offset_x = elementSettings.subtitle_sp_offset_x;
                    }
                    if( typeof elementSettings.subtitle_sp_offset_y !== 'undefined' && elementSettings.subtitle_sp_offset_y !== '' ){
                        sp_offset_y = elementSettings.subtitle_sp_offset_y;
                    }
                    if( typeof elementSettings.subtitle_sp_rotation !== 'undefined' && elementSettings.subtitle_sp_rotation !== '' ){
                        sp_rotation = elementSettings.subtitle_sp_rotation;
                    }
                    if( typeof elementSettings.subtitle_sp_rotationx !== 'undefined' && elementSettings.subtitle_sp_rotationx !== '' ){
                        sp_rotationx = elementSettings.subtitle_sp_rotationx;
                    }
                    if( typeof elementSettings.subtitle_sp_rotationy !== 'undefined' && elementSettings.subtitle_sp_rotationy !== '' ){
                        sp_rotationy = elementSettings.subtitle_sp_rotationy;
                    }
                    if( typeof elementSettings.subtitle_sp_scale !== 'undefined' && elementSettings.subtitle_sp_scale !== '' ){
                        sp_scale = elementSettings.subtitle_sp_scale;
                    }
                    if( typeof elementSettings.subtitle_sp_scalex !== 'undefined' && elementSettings.subtitle_sp_scalex !== '' ){
                        sp_scalex = elementSettings.subtitle_sp_scalex;
                    }
                    if( typeof elementSettings.subtitle_sp_scaley !== 'undefined' && elementSettings.subtitle_sp_scaley !== '' ){
                        sp_scaley = elementSettings.subtitle_sp_scaley;
                    }
                    if( typeof elementSettings.subtitle_sp_toggle_actions !== 'undefined' && elementSettings.subtitle_sp_toggle_actions !== '' ){
                        toggle_actions = elementSettings.subtitle_sp_toggle_actions;
                    }
                    if( typeof elementSettings.subtitle_sp_once !== 'undefined'  && elementSettings.subtitle_sp_once !== ''){
                        sp_once = parseInt(elementSettings.subtitle_sp_once);
                    }
                    if( typeof elementSettings.subtitle_sp_ease !== 'undefined'  && elementSettings.subtitle_sp_ease !== ''){
                        sp_ease = parseInt(elementSettings.subtitle_sp_ease);
                    }
                    if( typeof elementSettings.subtitle_sp_animation_duration !== 'undefined'  && elementSettings.subtitle_sp_animation_duration !== ''){
                        sp_animation_duration = elementSettings.subtitle_sp_animation_duration;
                    }
                    if( typeof elementSettings.subtitle_sp_animation_delay !== 'undefined'  && elementSettings.subtitle_sp_animation_delay !== ''){
                        sp_animation_delay = elementSettings.subtitle_sp_animation_delay;
                    }
                    if( typeof elementSettings.subtitle_sp_scrub !== 'undefined'  && elementSettings.subtitle_sp_scrub !== ''){
                        sp_scrub = elementSettings.subtitle_sp_scrub;
                    }
                    if( typeof elementSettings.subtitle_sp_stagger !== 'undefined'  && elementSettings.subtitle_sp_stagger !== ''){
                        sp_stagger = elementSettings.subtitle_sp_stagger;
                    }
                    if( typeof elementSettings.subtitle_sp_transform_origin !== 'undefined' && elementSettings.subtitle_sp_transform_origin !== '' ){
                        transform_origin = elementSettings.subtitle_sp_transform_origin;
                    }
                }else{
                    type = $this.getCurrentDeviceSetting( 'sp_type' ) || '';

                    if( typeof elementSettings.sp_opacity !== 'undefined' && elementSettings.sp_opacity !== '' ){
                        sp_opacity = elementSettings.sp_opacity;
                    }
                    if( typeof elementSettings.sp_offset_x !== 'undefined' && elementSettings.sp_offset_x !== '' ){
                        sp_offset_x = elementSettings.sp_offset_x;
                    }
                    if( typeof elementSettings.sp_offset_y !== 'undefined' && elementSettings.sp_offset_y !== '' ){
                        sp_offset_y = elementSettings.sp_offset_y;
                    }
                    if( typeof elementSettings.sp_rotation !== 'undefined' && elementSettings.sp_rotation !== '' ){
                        sp_rotation = elementSettings.sp_rotation;
                    }
                    if( typeof elementSettings.sp_rotationx !== 'undefined' && elementSettings.sp_rotationx !== '' ){
                        sp_rotationx = elementSettings.sp_rotationx;
                    }
                    if( typeof elementSettings.sp_rotationy !== 'undefined' && elementSettings.sp_rotationy !== '' ){
                        sp_rotationy = elementSettings.sp_rotationy;
                    }
                    if( typeof elementSettings.sp_scale !== 'undefined' && elementSettings.sp_scale !== '' ){
                        sp_scale = elementSettings.sp_scale;
                    }
                    if( typeof elementSettings.sp_scalex !== 'undefined' && elementSettings.sp_scalex !== '' ){
                        sp_scalex = elementSettings.sp_scalex;
                    }
                    if( typeof elementSettings.sp_scaley !== 'undefined' && elementSettings.sp_scaley !== '' ){
                        sp_scaley = elementSettings.sp_scaley;
                    }
                    if( typeof elementSettings.sp_toggle_actions !== 'undefined' && elementSettings.sp_toggle_actions !== '' ){
                        toggle_actions = elementSettings.sp_toggle_actions;
                    }
                    if( typeof elementSettings.sp_once !== 'undefined'  && elementSettings.sp_once !== ''){
                        sp_once = parseInt(elementSettings.sp_once);
                    }
                    if( typeof elementSettings.sp_ease !== 'undefined'  && elementSettings.sp_ease !== ''){
                        sp_ease = parseInt(elementSettings.sp_ease);
                    }
                    if( typeof elementSettings.sp_animation_duration !== 'undefined'  && elementSettings.sp_animation_duration !== ''){
                        sp_animation_duration = elementSettings.sp_animation_duration;
                    }
                    if( typeof elementSettings.sp_animation_delay !== 'undefined'  && elementSettings.sp_animation_delay !== ''){
                        sp_animation_delay = elementSettings.sp_animation_delay;
                    }
                    if( typeof elementSettings.sp_scrub !== 'undefined'  && elementSettings.sp_scrub !== ''){
                        sp_scrub = elementSettings.sp_scrub;
                    }
                    if( typeof elementSettings.sp_stagger !== 'undefined'  && elementSettings.sp_stagger !== ''){
                        sp_stagger = elementSettings.sp_stagger;
                    }

                    if( typeof elementSettings.sp_transform_origin !== 'undefined' && elementSettings.sp_transform_origin !== '' ){
                        transform_origin = elementSettings.sp_transform_origin;
                    }
                }
                $(el).css('--title_opacity', '1');
                $(el).css('--subtitle_opacity', '1');
                if( '' === type || 'none' === type){
                    return;
                }
                    
                var els = $(el).find('p').length > 0 ? $(el).find('p') : el;

                var pxl_split = new SplitText(els, { 
                    type: 'chars, words, lines',
                    lineThreshold: 0.5,
                    charsClass: "split-char",
                    wordsClass: "split-word",
                    linesClass: "split-line"
                });

                var pxl_scroll_trigger = {
                    trigger: els,
                    toggleActions: toggle_actions,
                    start: "top 86%"
                    //markers: true
                }

                var split_type_set = pxl_split.chars;
 
                gsap.set(els, { perspective: 400 });

                if( sp_once !== '')
                    pxl_scroll_trigger.once = sp_once;

                if( sp_scrub !== '')
                    pxl_scroll_trigger.scrub = sp_scrub;

                var settings = {
                    scrollTrigger: pxl_scroll_trigger,
                    duration: sp_animation_duration, 
                    stagger: sp_stagger,
                    ease: sp_ease,
                };

                if( 'chars' === type || 'words' === type || 'lines' === type ){
                    if( sp_opacity !== '')
                        settings.opacity = sp_opacity;

                    if( sp_offset_x !== '')
                        settings.x = sp_offset_x;

                    if( sp_offset_y !== '')
                        settings.y = sp_offset_y;

                    if( sp_rotation !== '')
                        settings.rotation = sp_rotation;

                    if( sp_rotationx !== '')
                        settings.rotationX = sp_rotationx;

                    if( sp_rotationy !== '')
                        settings.rotationY = sp_rotationy;

                    if( sp_scale !== '')
                        settings.scale = sp_scale;

                    if( sp_scalex !== '')
                        settings.scaleX = sp_scalex;

                    if( sp_scaley !== '')
                        settings.scaleY = sp_scaley;

                    if( sp_animation_delay !== '')
                        settings.delay = sp_animation_delay;

                    if( transform_origin !== '')
                        settings.transformOrigin = transform_origin;
                }

                 
                if( type == 'words'){
                    split_type_set = pxl_split.words;
                }
                if( type == 'lines'){
                    split_type_set = pxl_split.lines;
                }

                if( type == 'words-scale'){
                    pxl_split.split({type:"words"}); 
                    split_type_set = pxl_split.words;
                   
                    $(split_type_set).each(function(index,elw) { 
                        gsap.set(elw, {
                            opacity: 0,
                            scale:index % 2 == 0  ? 0 : 2,
                            force3D:true,
                            duration: 0.1,
                            ease: sp_ease,
                            stagger: sp_stagger,
                        },index * 0.01);
                    });

                    var pxlwc_scroll_trigger = {
                        trigger: el,
                        toggleActions: toggle_actions,
                        start: "top 86%"
                        //markers: true
                    }

                    if( sp_once !== '')
                        pxlwc_scroll_trigger.once = sp_once;

                    if( sp_scrub !== '')
                        pxlwc_scroll_trigger.scrub = sp_scrub;

                    var pxl_anim = gsap.to(split_type_set, {
                            scrollTrigger: pxlwc_scroll_trigger,
                            rotateX: "0",
                            scale: 1,
                            opacity: 1,
                        });
                }else{
                    var pxl_anim = gsap.from(split_type_set, settings);  
                      
                }
 
            });    
              
        }
         
        onInit() {
            this.split_text();
        }
        onElementChange( propertyName ) {
            /*if ( /(.)_sp_type?/.test( propertyName ) ) {
                this.split_text();
            }*/
            /*if ( propertyName === 'title_sp_type' || propertyName === 'subtitle_sp_type') {
                this.split_text();
            }*/
            /*if ( propertyName === 'title_sp_type') {
                this.split_text();
            }*/
        }
    }

    function apexus_split_text($scope){
         
        if( $scope.closest('.split-text-off-scroll').length > 0) return false;

        var st = $scope.find(".pxl-split-text");
        if(st.length == 0) return;

        gsap.registerPlugin(SplitText);
        
        st.each(function(index, el) {
           var els = $(el).find('p').length > 0 ? $(el).find('p')[0] : el;
            const pxl_split = new SplitText(els, { 
                type: "lines, words, chars",
                lineThreshold: 0.5,
                linesClass: "split-line"
            });
            var split_type_set = pxl_split.chars;
           
            gsap.set(els, { perspective: 400 });
 
            var settings = {
                scrollTrigger: {
                    trigger: els,
                    toggleActions: "play none none none", //play reset play reset 
                    start: "top 86%",
                },
                duration: 0.8, 
                stagger: 0.02,
                ease: "power3.out",
            };
            if( $(el).hasClass('split-in-fade') ){
                settings.opacity = 0;
            }
            if( $(el).hasClass('split-in-right') ){
                settings.opacity = 0;
                settings.x = "50";
            }
            if( $(el).hasClass('split-in-left') ){
                settings.opacity = 0;
                settings.x = "-50";
            }
            if( $(el).hasClass('split-in-up') ){
                settings.opacity = 0;
                settings.y = "80";
            }
            if( $(el).hasClass('split-in-down') ){
                settings.opacity = 0;
                settings.y = "-80";
            }
            if( $(el).hasClass('split-in-rotate') ){
                settings.opacity = 0;
                settings.rotateX = "50deg";
            }
            if( $(el).hasClass('split-in-scale') ){
                settings.opacity = 0;
                settings.scale = "0.5";
            }
 
            if( $(el).hasClass('split-lines-transform') ){
                pxl_split.split({
                    type:"lines",
                    lineThreshold: 0.5,
                    linesClass: "split-line"
                }); 
                split_type_set = pxl_split.lines;
                settings.opacity = 0;
                settings.yPercent = 100;
                settings.autoAlpha = 0;
                settings.stagger = 0.1;
            }
            if( $(el).hasClass('split-lines-rotation-x') ){
                pxl_split.split({
                    type:"lines",
                    lineThreshold: 0.5,
                    linesClass: "split-line"
                }); 
                split_type_set = pxl_split.lines;
                settings.opacity = 0;
                settings.rotationX = -120;
                settings.transformOrigin = "top center -50";
                settings.autoAlpha = 0;
                settings.stagger = 0.1;
            }
             
            if( $(el).hasClass('split-words-scale') ){
                pxl_split.split({type:"words"}); 
                split_type_set = pxl_split.words;
               
                $(split_type_set).each(function(index,elw) {
                    gsap.set(elw, {
                        opacity: 0,
                        scale:index % 2 == 0  ? 0 : 2,
                        force3D:true,
                        duration: 0.1,
                        ease: "power3.out",
                        stagger: 0.02,
                    },index * 0.01);
                });

                var pxl_anim = gsap.to(split_type_set, {
                    scrollTrigger: {
                        trigger: el,
                        toggleActions: "play reverse play reverse",
                        start: "top 86%",
                    },
                    rotateX: "0",
                    scale: 1,
                    opacity: 1,
                });
  
            }else{
                var pxl_anim = gsap.from(split_type_set, settings);
            }
             
            if( $(el).hasClass('hover-split-text') ){
                $(el).mouseenter(function(e) {
                    pxl_anim.restart();
                });
            }
        });
    }


    $( window ).on( 'elementor/frontend/init', function() {
        gsap.registerPlugin(ScrollTrigger); 
        const addSplittextHandler = ( $element ) => {
            gsap.registerPlugin(SplitText);
            elementorFrontend.elementsHandler.addHandler( Pxl_Splittext_Handler, { $element } );
        };
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_heading.default', addSplittextHandler );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_text_editor.default', addSplittextHandler );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_heading.default', function( $scope ) {
            apexus_split_text($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_text_editor.default', function( $scope ) {
            apexus_split_text($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_slider.default', function( $scope ) {
            apexus_split_text($scope);
        } );
        elementorFrontend.hooks.addAction( 'frontend/element_ready/pxl_services_scroll.default', function( $scope ) {
            apexus_split_text($scope);
        } );

    } );
    $(document.body).on('pxl_effect_refreshed', function(e, $scope) {
        apexus_split_text($scope);
    });


} )( jQuery );
 