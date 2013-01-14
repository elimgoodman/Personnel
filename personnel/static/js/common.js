$(function() {
    $('a.communicated').click(function(){
        var self = this;
        var feedback_id = $(this).attr('data-feedback-id');
        var csrf = $("[name=csrfmiddlewaretoken]").val();

        var params = {
            csrfmiddlewaretoken: csrf,
            feedback_id: feedback_id
        };

        $.post("/feedback/communicated", params, function(data){
            $(self).parents("li").fadeOut();
        }, "json");

        return false;
    });

    $('a.closed-loop').click(function(){
        var self = this;
        var feedback_id = $(this).attr('data-feedback-id');
        var csrf = $("[name=csrfmiddlewaretoken]").val();

        var params = {
            csrfmiddlewaretoken: csrf,
            feedback_id: feedback_id
        };

        $.post("/feedback/closed_loop", params, function(data){
            $(self).parents("li").fadeOut();
        }, "json");

        return false;
    });

    $('a.checked-in').click(function(){
        var self = this;
        var checkin_id = $(this).attr('data-checkin-id');
        var csrf = $("[name=csrfmiddlewaretoken]").val();

        var params = {
            csrfmiddlewaretoken: csrf,
            checkin_id: checkin_id
        };

        $.post("/checkin/checked_in", params, function(data){
            $(self).parents("li").fadeOut();
        }, "json");

        return false;
    });
});
