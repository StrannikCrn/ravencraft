function check_arrows(left_pos) {
    var width_wr = $(".bottles_wr").width();
    var width = $(".bottles").width();
    var left_pos_wr = $(".bottles_wr").offset().left;
    var right_pos = width + left_pos;
    var right_pos_wr = width_wr + left_pos_wr;
    if (right_pos < right_pos_wr) {
        $(".arr_right").hide();
    }
    else {
        $(".arr_right").show();
    }
    if (left_pos >= left_pos_wr) {
        $(".arr_left").hide();
    }
    else {
        $(".arr_left").show();
    }
}
$(document).ready(function () {

    $(".arr_left").click(function () {
        var width = $(".bottles_wr").width();
        var left_offset = $(".bottles").offset().left;
        var left_pos = $(".bottles").position().left;
        $(".bottles").css("left", left_pos + width);
        check_arrows(left_offset + width);
    });
    $(".arr_right").click(function () {
        var width = $(".bottles_wr").width();
        var left_offset = $(".bottles").offset().left;
        var left_pos = $(".bottles").position().left;
        $(".bottles").css("left", left_pos - width);
        check_arrows(left_offset - width);
    });
    var left_pos = $(".bottles").offset().left;
    check_arrows(left_pos);
    $(".bottle:not(.bottle_fake)").hover(function () {


            var id = $(this).attr("id");
            var desc_item = $("#desc_" + id);
            if (!desc_item.hasClass("op1")) {
                $(".bottle_desc_item").removeClass("op1");
                    $(".bottle_desc_item").addClass("hidden");
                desc_item.removeClass("hidden");
                setTimeout(function () {
                    desc_item.addClass("op1");
                }, 1)
            }
            $(".bottle:not(#{id})".replace("{id}", id)).removeClass("hovered");
            $(this).addClass("hovered")
        }
    )
    $(".bottles").find(".bottle:not(.bottle_fake)").first().trigger('mouseenter');
    ;
});