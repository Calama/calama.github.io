$("#more-research a").click(function() {
    $("#research").toggleClass('show-all');
    return false;
});

$("#products .meta a").click(function(e) {
    e.preventDefault();
    $("#products .substance li, #products .meta li a").removeClass('selected');
    $("#products .substance li" + $(this).attr('href')).addClass('selected');
    $(this).addClass('selected');
});
