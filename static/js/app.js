// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

$(document).ready(function(){
    
    function reHeight() {
        $('.my-grid > li').each(function() {
                $(this).height($(this).width() * 0.65);
        });
    }
    
    reHeight();
    
    $(window).resize(reHeight);
    
});
